import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import csv

# Load your DataFrame
df = pd.read_csv("df_merged_embeddings.csv")  # Replace with your actual file

# Initialize log file
log_file = "processing_log.csv"
with open(log_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["file_number", "id", "message"])  # Add file_number to the header

# API endpoint
url = 'http://localhost:8887/linkextractor/links/as-html-link-table/extract/upload://.txt'

# Function to make the POST request
def extract_links(text: str, row_id, file_number) -> str:
    """
    Sends a POST request to the API to extract links from the provided text.

    :param text: Input text to be sent to the API for link extraction.
    :param row_id: The ID of the row being processed.
    :param file_number: The file number of the row being processed.
    :return: The HTML response as a string, or an error message.
    """
    try:
        # Write the text to a temporary file
        temp_filename = "temp_text.txt"
        with open(temp_filename, "w", encoding="utf-8") as temp_file:
            temp_file.write(text)
        
        # Send the POST request
        with open(temp_filename, "rb") as f:
            response = requests.post(
                url,
                files={'.txt': f},
                data={'show': 'markup'}
            )
        
        # Check if the response is successful
        if response.status_code == 200:
            log_message(file_number, row_id, "Row parsed successfully.")
            return response.text
        else:
            error_message = f"Error: {response.status_code}"
            log_message(file_number, row_id, error_message)
            return error_message
    except Exception as e:
        error_message = f"Error: {str(e)}"
        log_message(file_number, row_id, error_message)
        return error_message

# Function to extract attributes from the HTML response
def extract_attributes_from_html(html_text: str) -> dict:
    """
    Extracts legal references and their attributes from the HTML table.

    :param html_text: HTML content containing legal references.
    :return: A dictionary where keys are law names and values are attribute dictionaries.
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    rows = soup.find_all('tr')  # Find all rows in the table

    legal_references = {}

    for row in rows:
        columns = row.find_all('td')  # Find all columns in the row
        if len(columns) < 3:
            continue  # Skip rows that do not have enough columns

        # Extract the category (e.g., 'wet') and the law name (e.g., 'Wet dieren')
        category = columns[0].get_text(strip=True)
        law_name = columns[1].get_text(strip=True)

        # Extract attributes from the third column
        attributes = {}
        for div in columns[2].find_all('div'):
            key_value = div.get_text(strip=True).split(' = ')
            if len(key_value) == 2:  # Ensure valid key-value pairs
                key, value = key_value
                attributes[key] = value

        # Add the extracted information to the dictionary
        legal_references[law_name] = {
            'category': category,
            'attributes': attributes
        }

    return legal_references

# Logging function
def log_message(file_number, row_id, message):
    """
    Logs a message with the file_number and row ID to the log file.

    :param file_number: The file number of the row.
    :param row_id: The ID of the row.
    :param message: The log message.
    """
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([file_number, row_id, message])

# Function to integrate both steps: POST request and attribute extraction
def process_text_to_legal_references(text: str, row_id, file_number) -> dict:
    """
    Combines the API call and the HTML parsing to return a dictionary of legal references.

    :param text: Input text for the API.
    :param row_id: The ID of the row being processed.
    :param file_number: The file number of the row being processed.
    :return: Extracted legal references from the API response as a dictionary.
    """
    html_response = extract_links(text, row_id, file_number)  # Make the POST request
    if html_response.startswith("Error:"):  # Handle errors in API response
        return {}
    return extract_attributes_from_html(html_response)  # Parse the HTML response

# Add progress bar to the apply function
tqdm.pandas()  # Enable tqdm for pandas

# Apply the function to the DataFrame with logging
df['legal_references'] = df.progress_apply(
    lambda row: process_text_to_legal_references(row['text_pypdf2'], row['id'], row['file_number']), axis=1
)

# Save the updated DataFrame
df.to_csv("df_with_legal_references_last.csv", index=False)
