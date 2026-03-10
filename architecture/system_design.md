# System Architecture

This project implements a **cloud-native healthcare analytics pipeline** using Google Cloud.

## Data Flow

Healthcare Dataset
↓
Cloud Storage (optional staging)
↓
BigQuery Raw Tables
↓
BigQuery Data Processing (SQL)
↓
BigQuery ML Models

Models implemented:

* Classification — High-cost prescription detection
* Regression — Prescription demand prediction
* Forecasting — Medication demand forecasting

## Technology Stack

* Google Cloud Platform
* BigQuery
* BigQuery ML
* Python
* Pandas
* Matplotlib
