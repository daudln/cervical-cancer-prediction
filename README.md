# Cervical Cancer Prediction

## Description

This project aims to develop a machine learning model for predicting the likelihood of cervical cancer based on various demographic and medical factors. The model is trained on a dataset containing information such as age, number of sexual partners, medical history, and diagnostic tests results.

## Dataset

The dataset used for training the model includes the following columns:

1. Age
2. Number of sexual partners
3. First sexual intercourse
4. Number of pregnancies
5. Smoking history
6. Hormonal contraceptives usage
7. Intrauterine device (IUD) usage
8. History of sexually transmitted diseases (STDs)

## Project Components

1. Data Preprocessing: Cleaning the dataset, handling missing values, and encoding categorical variables.
2. Exploratory Data Analysis (EDA): Analyzing the distribution of features, identifying correlations, and visualizing patterns in the data.
3. Model Development: Training machine learning models (such as RandomForestClassifier, AdaBoostClassifier) to predict the likelihood of cervical cancer based on input features.
4. Model Evaluation: Assessing the performance of the trained models using metrics like accuracy, precision, recall, and F1-score.
5. Deployment: Integrating the trained model into a FastAPI endpoint to enable real-time predictions.

## Setup Instructions

1. Clone the repository to your local machine (ask for Dataset via <daudnamayala@gmail.com>).
2. Install the required dependencies using pip or conda.
3. Run the data preprocessing script to clean and prepare the dataset.
4. Execute the model training script to train the predictive models.
5. Deploy the trained model using the provided FastAPI endpoint.

## Usage

Use the FastAPI endpoint to make predictions by sending input data in JSON format.
Test the endpoint using tools like Postman or by sending HTTP requests programmatically.

## Contributors

1. Daud Namayala
