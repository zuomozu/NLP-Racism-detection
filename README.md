# NLP-Racism-detection

# README

## Table of Contents
- [Introduction](#introduction)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Training the Model](#training-the-model)
- [Deploying with Docker](#deploying-with-docker)
- [API Endpoints](#api-endpoints)

## Introduction
This project is a web application built with Flask that classifies text as "Racist" or "Non-Racist" using a pre-trained BERT model. The application includes text preprocessing steps like handling negation, converting text to lowercase, and removing URLs and non-alphabet characters.

## Setup and Installation

### Prerequisites
- Python 3.7+
- Flask
- Transformers (Hugging Face)
- TensorFlow
- Pandas
- Scikit-learn

### Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Download and set up the pre-trained BERT model and tokenizer:
    ```bash
    mkdir -p saved_model2
    cd saved_model2
    wget <link-to-pretrained-model>  # Replace with the actual link
    wget <link-to-pretrained-tokenizer>  # Replace with the actual link
    cd ..
    ```

## Usage

### Running the Flask Application
Start the Flask app:
```bash
python app.py
