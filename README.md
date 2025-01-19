# Information Extraction from Dutch Administrative Decisions: A Comparison of Supervised NLP Techniques and Unsupervised Large Language Models

This repository is part of the Case-Inclusive Transparency for a Digital and Open Government (CITaDOG) project by Tilburg University. The project aims to enhance transparency in administrative decision-making through the development of scalable and adaptable NLP techniques. This repository contains code and datasets used to extract key metadata—such as recipients, dates, legal references, and legal effects—from Dutch administrative decisions by the *Autoriteit Consument & Markt* (ACM). By comparing supervised machine learning models with unsupervised approaches using Large Language Models (here implemented using the OpenAI api), the research offers insights into the trade-offs between precision, scalability, and adaptability in information extraction tasks in the context of Dutch Adminstrative Decisions.

## Table of Contents
- [Installation](#installation)
- [Repository Structure](#repo-structure)

## Installation <a name="installation"></a>

1. Clone the repository:
    ```bash
    git clone https://github.com/giacomograza/BEP_CITaDOG.git
    ```
2. Navigate to the project directory:
    ```bash
    cd BEP_CITaDOG
    ```
3. Install the dependencies:
    ```bash
    npm install requirements.txt
    ```

## Repository Structure anc Content <a name="repo-structure"></a>
This repositories consists of five code folders, namely:

- 🗂️ `1,2_data_preprocessing_eda`
    This folder contains the initial data processing steps and exploratory analysis for the research. It includes the following:
    - **`original_data` folder**: contains the raw, scraped data used for the research (ACM permits) in `.csv` format.
    - **`1,2_data_preprocessing_eda.ipynb`**: a Jupyter Notebook that performs Exploratory Data Analysis (EDA), preprocessing, and spelling correction of the dataset. It provides insights into the structure and quality of the raw data while preparing it for further analysis.
    - **`data_spelling_correction_api_outputs.csv`**: a preprocessed dataset with spelling corrections applied using the OpenAI API. This dataset bypasses the need for re-running the API calls in sections 3.1.1 and 3.2.1 of the Jupyter Notebook.

- 🗂️ Folder `3_recipient_extraction`
      This folder contains the EDA of the labeled recipients, supervised NER and LLM-based NER for recipient extraction. It includes the following:
      - **`3_recipient_extraction.ipynb`**: a Jupyter Notebook that performs supervised NER, LLM-based NER and respective evaluations.
      - **`data_recipient_extraction.csv`**: a preprocessed dataset with spelling LLM-extracted recipient entities using the OpenAI API. This dataset bypasses the need for re-running the API calls in section 2 of the Jupyter Notebook.

- 🗂️ Folder `4_date_extraction`
  This folder contains the EDA of the labeled recipients, supervised NER and LLM-based NER for recipient extraction. It includes the following:
      - **`3_recipient_extraction.ipynb`**: a Jupyter Notebook that performs supervised NER, LLM-based NER and respective evaluations.
      - **`data_recipient_extraction.csv`**: a preprocessed dataset with spelling LLM-extracted recipient entities using the OpenAI API. This dataset bypasses the need for re-running the API calls in section 2 of the Jupyter Notebook.

- 🗂️ Folder `5_legal_references_extraction`

- 🗂️ Folder `6_legal_effect_extraction`
