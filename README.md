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

Open your browser and navigate to http://127.0.0.1:5000/ to access the web interface.

Classify Text via API
You can classify text using the /classify endpoint.

Example request:



curl -X POST -F "text=Your text here" http://127.0.0.1:5000/classify
Training the Model
Load your dataset in DiscriminatoryText.csv.
Run the training script:
bash

python train.py
Preprocessing
Removing URLs
Removing non-alphabet characters
Converting to lowercase
Handling negation
Model Training
The BERT model is trained on your dataset and saved in the saved_model2 directory.

Deploying with Docker
Dockerfile
Create a Dockerfile in the project root:

dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]
Building and Running the Docker Container
Build the Docker image:

bash

docker build -t flask-bert-classifier .
Run the Docker container:

bash

docker run -p 5000:5000 flask-bert-classifier
API Endpoints
GET /
Description: Renders the home page.
Response: HTML page.
POST /classify
Description: Classifies the provided text as "Racist" or "Non-Racist".
Parameters:
text: The text to classify (form data).
Response: JSON with the classification result.
json

{
    "result": "Non-Racist. It is good to post."
}
