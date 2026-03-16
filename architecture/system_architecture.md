# Cloud Healthcare Analytics Pipeline Architecture

This project implements a cloud-native healthcare analytics system using Google Cloud and BigQuery ML.

## System Architecture

```
Healthcare Dataset
        │
        ▼
Google Cloud Storage (optional staging)
        │
        ▼
BigQuery Raw Table
        │
        ▼
Data Cleaning Pipeline
(SQL transformations)
        │
        ▼
Feature Engineering
(BMI calculation, feature preparation)
        │
        ▼
Exploratory Data Analysis
(Python + Jupyter Notebook)
        │
        ▼
Machine Learning Models (BigQuery ML)
    ├── Regression Model
    │     Predict weight from height
    │
    ├── Classification Model
    │     Predict high BMI category
    │
    └── Time-Series Forecast Model
          Forecast prescription demand
        │
        ▼
Predictions & Forecasting Results
```

## Technology Stack

* Google Cloud Platform
* BigQuery
* BigQuery ML
* Python
* Pandas
* Matplotlib
* Jupyter Notebook
