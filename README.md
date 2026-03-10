# Cloud Healthcare Analytics Pipeline

A **cloud-native healthcare and digital pharmacy analytics pipeline** built using **Google Cloud, BigQuery ML, and Python**.

This project demonstrates how large healthcare datasets can be processed, analysed, and used to build machine learning models for **prescription forecasting and healthcare insights**.

---

## Project Goals

This project was created to achieve two objectives:

1. Prepare reusable tools for a **Data & AI Hackathon (Healthcare Track)**.
2. Build a **portfolio-grade cloud machine learning pipeline** using modern data engineering and ML practices.

---

## Key Features

* Scalable healthcare dataset processing using **BigQuery**
* Data transformation and feature engineering with **SQL**
* Machine learning models built using **BigQuery ML**
* Forecasting models for **prescription demand**
* Classification models for **high-cost prescriptions**
* Python notebooks for **analysis and visualisation**

---

## System Architecture

Healthcare Dataset
↓
Cloud Storage (optional staging)
↓
BigQuery Raw Tables
↓
BigQuery Data Processing (SQL)
↓
BigQuery ML Models
↓
Python Analysis & Visualisation

---

## Machine Learning Tasks

### Classification

Predict whether a prescription is likely to exceed a cost threshold.

Potential use cases:

* healthcare cost monitoring
* anomaly detection
* prescription pattern analysis

---

### Regression & Forecasting

Predict medication demand and prescription volumes over time.

Potential use cases:

* pharmacy supply planning
* healthcare resource management
* seasonal demand forecasting

---

## Technology Stack

* Google Cloud Platform
* BigQuery
* BigQuery ML
* Python
* Pandas
* Matplotlib
* Jupyter Notebooks

---

## Project Structure

```
architecture/     System architecture documentation
data/             Dataset documentation
docs/             Project planning and roadmap
notebooks/        Data analysis notebooks
scripts/          Python pipeline scripts
sql/              BigQuery SQL queries
```

---

## Current Status

Project Phase: **Phase 0 — Project Foundation**

Next Steps:

* Configure cloud infrastructure
* Ingest healthcare dataset
* Build BigQuery data pipeline
* Train baseline ML models

---

## Author

Kaustubh Kaushal
MSc Advanced Computer Science (Data Analytics)
University of Leeds
