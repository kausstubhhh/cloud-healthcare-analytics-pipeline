# SQL Queries

This directory contains all BigQuery SQL scripts used in the healthcare analytics pipeline.

The queries are organised based on different stages of the data and machine learning pipeline.

---

## Directory Structure

### data_pipeline/

Contains SQL queries for data preparation:

• data cleaning  
• handling missing values  
• feature engineering (BMI calculation)  
• creation of time-series datasets  

---

### models/

Contains SQL queries for training machine learning models using BigQuery ML:

• regression model (weight prediction)  
• classification model (BMI risk classification)  
• time-series forecasting model (ARIMA)  

---

### evaluation/

Contains SQL queries for evaluating models and generating predictions:

• model evaluation metrics  
• prediction outputs  
• feature importance analysis  
• forecast results  

---

## Usage

These queries are designed to be executed in Google BigQuery.

Each file corresponds to a specific stage in the pipeline and can be run independently or as part of a full workflow.

---

## Pipeline Flow

data_pipeline → models → evaluation

This reflects the end-to-end machine learning lifecycle implemented in this project.
