# Information Extraction from Dutch Administrative Decisions: A Comparison of Supervised NLP Techniques and Unsupervised Large Language Models

This repository is part of a TU/e Bachelor End Project (BEP) within the Case-Inclusive Transparency for a Digital and Open Government (CITaDOG) project by Tilburg University. The project aims to enhance transparency in administrative decision-making through the development of scalable and adaptable information extraction (IE) techniques. This repository contains code and datasets used to extract key metadata—such as recipients, dates, legal references, and legal effects—from Dutch administrative decisions issued by the Autoriteit Consument & Markt (ACM). By comparing supervised machine learning models with unsupervised approaches using Large Language Models (implemented via the OpenAI API), this research provides insights into the trade-offs between precision, scalability, and adaptability in information extraction tasks within the context of Dutch administrative decisions.

The supervisors for this project are:
- Prof. Dr. Johan Wolswinkel, LL.M.
- Harry Nan, PhD candidate

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

## Repository Structure and Content <a name="repo-structure"></a>
This repositories consists of five code folders, namely:

- 🗂️ `1,2_data_preprocessing_eda`

  This folder contains the initial data processing steps and exploratory analysis for the research. It includes the following:
    - `original_data` folder: contains the raw, scraped data used for the research (ACM permits) in `.csv` format.
    - `1,2_data_preprocessing_eda.ipynb`: a Jupyter Notebook that performs Exploratory Data Analysis (EDA), preprocessing, and spelling correction of the dataset. It provides insights into the structure and quality of the raw data while preparing it for further analysis.
    - `data_spelling_correction_api_outputs.csv`: a preprocessed dataset with spelling corrections applied using the OpenAI API. This dataset bypasses the need for re-running the API calls in sections 3.1.1 and 3.2.1 of the Jupyter Notebook.

- 🗂️ `3_recipient_extraction`
  
  This folder contains the EDA of the labeled recipients, supervised NER and LLM-based NER for recipient extraction. It includes the following:
    - `3_recipient_extraction.ipynb`: a Jupyter Notebook that performs supervised NER, LLM-based NER and respective evaluations.
    - `data_recipient_extraction.csv`: a preprocessed dataset with LLM-extracted recipient entities using the OpenAI API. This dataset bypasses the need for re-running the API calls in section 2 of the Jupyter Notebook.

- 🗂️ `4_date_extraction`
  
  This folder contains supervised and LLM-based date extraction code. It includes the following:
    - `4_recipient_extraction.ipynb`: a Jupyter Notebook that performs supervised and LLM-based date extration (and respective evaluations).
    - `data_date_extraction.csv`: a preprocessed dataset with LLM-extracted dates using the OpenAI API. This dataset bypasses the need for re-running the API calls in section 2 of the Jupyter Notebook.

- 🗂️ `5_legal_references_extraction`

  This folder contains the code to extract legal references with the LinkExtractor and the OpenAI API, and a thorough comparison of the two approaches. It includes the following:
    - `linkextractor_scripts`: a folder containing the script that calls the LinkExtractor API to extract legal references.
      - `data_lx_script.csv`: the data required for the LX api calls.
      - `script_lx_api.py`: a script performing the LX API calls (POST), structuring the API's output in the desired formt and logging the outcome of each decision processing into a log file.
      - `processing_log.csv`: a processing log file showing the outcome of the single LX API calls.
      - `jupyter_nb.ipynb`: a notebok that loads the LinkExtracted data and helps understand the database/dictionary structure. 
    - `5_legal_references_extraction.ipynb`: a Jupyter Notebook that performs LLM-based legal references extration and compares the results with those of the LinkExtractor.
    - `df_with_legal_references_lx_openai.csv`: a preprocessed dataset with LX and LLM-extracted legal references. This dataset bypasses the need for re-running the API calls in `script_lx_api.py` and section 2.1 of the Jupyter Notebook.

- 🗂️ `6_legal_effect_classification`: 

  This folder contains supervised and LLM-based legal effect classification pipelines. It includes the following:
    - `6_legal_effect_classification.ipynb`: a Jupyter Notebook that performs supervised and  LLM-based legal effect classification and compares the results of the two approaches.
    - `data_giacomo_cleaned_restricted.csv`: a dataset with the manually annotated labels (to be merged with the unlabeled dataset).
    - `df_merged_embeddings.csv`: a dataset with the unlabeled decisions.
    - `df_llm_no_overdracht.csv`: a dataset that bypasses the need for re-running the API calls in section 2.1 and 2.2 of the Jupyter Notebook.