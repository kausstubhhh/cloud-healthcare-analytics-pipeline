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

# Project Progress

| Phase   | Description                            | Status      |
| ------- | -------------------------------------- | ----------- |
| Phase 0 | Project foundation & environment setup | Complete    |
| Phase 1 | Cloud infrastructure setup             | Complete    |
| Phase 2 | Data ingestion pipeline                | Complete    |
| Phase 3 | Data engineering & cleaning            | In Progress |
| Phase 4 | Exploratory data analysis              | Planned     |
| Phase 5 | Machine learning models                | Planned     |
| Phase 6 | Forecasting models                     | Planned     |

---

# Current Status

Current Phase: **Phase 3 — Data Engineering & Cleaning**

The dataset has been successfully ingested into BigQuery as:

```
pharmacy_analytics.prescriptions_raw
```

Next step is to transform the raw dataset into cleaned and feature-engineered tables for analytics and machine learning.

---

# Author

**Kaustubh Kaushal**
MSc Advanced Computer Science (Data Analytics)
University of Leeds
