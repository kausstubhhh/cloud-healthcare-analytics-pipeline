# Cloud Healthcare Analytics Pipeline

A **cloud-native healthcare and digital pharmacy analytics pipeline** built using Google Cloud, BigQuery ML, and Python.

This project demonstrates how healthcare datasets can be processed at scale, analysed using SQL, and used to train machine learning models for prescription demand forecasting and healthcare insights.

---

# Project Goals

This project was designed to achieve two objectives:

1. Prepare reusable tools for a **Data & AI Hackathon (Healthcare Track)**.
2. Build a **portfolio-grade cloud ML pipeline** demonstrating cloud data engineering and machine learning workflows.

---

# Key Features

• Scalable healthcare data processing using BigQuery
• Cloud storage staging using Google Cloud Storage
• Data transformation and feature engineering using SQL
• Machine learning models built using BigQuery ML
• Forecasting models for prescription demand
• Classification models for high-cost prescriptions
• Python notebooks for analysis and visualisation

---

# System Architecture

Healthcare Dataset
↓
Cloud Storage (data staging)
↓
BigQuery Raw Tables
↓
BigQuery Data Processing (SQL)
↓
BigQuery ML Models
↓
Python Analysis & Visualisation

---

# Machine Learning Tasks

## Classification

Predict whether a prescription is likely to exceed a cost threshold.

Potential use cases:

• healthcare cost monitoring
• anomaly detection
• prescription pattern analysis

---

## Regression & Forecasting

Predict medication demand and prescription volumes over time.

Potential use cases:

• pharmacy supply planning
• healthcare resource management
• seasonal demand forecasting

---

# Technology Stack

• Google Cloud Platform
• BigQuery
• BigQuery ML
• Cloud Storage
• Python
• Pandas
• Matplotlib
• Jupyter Notebooks

---

# Project Structure

```
architecture/   System architecture documentation
data/           Sample datasets
docs/           Project documentation
notebooks/      Data analysis notebooks
scripts/        Pipeline scripts
sql/            BigQuery SQL queries
```

---

# Exploratory Data Analysis

The dataset was analysed using a Python notebook connected to BigQuery.
Below are some key visualisations generated during the analysis.

## Height Distribution

![Height Distribution](figures/height_distribution.png)

This plot shows the distribution of height values in the dataset.

---

## Weight Distribution

![Weight Distribution](figures/weight_distribution.png)

This visualisation shows how weight values are distributed across the dataset.

---

## BMI Distribution

![BMI Distribution](figures/bmi_distribution.png)

BMI values were calculated as part of the feature engineering phase and visualised to understand the spread of health metrics.

---

## Feature Correlation

![Correlation Heatmap](figures/correlation_heatmap.png)

The correlation heatmap highlights relationships between the variables:

* height
* weight
* BMI

---

# Author

**Kaustubh Kaushal**
MSc Advanced Computer Science (Data Analytics)
University of Leeds
