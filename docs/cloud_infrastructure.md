# Cloud Infrastructure Setup

This document describes the cloud resources created for the Healthcare Analytics Pipeline project.

## Cloud Platform

Google Cloud Platform (GCP)

Project Name:
Healthcare Analytics Pipeline

Project ID:
healthcare-analytics-kaust

---

## Enabled Services

The following services are enabled in the project:

* BigQuery
* Cloud Storage
* Vertex AI (optional for experimentation)

---

## BigQuery

Dataset created:

pharmacy_analytics

Purpose:

This dataset will store:

* raw healthcare datasets
* cleaned data tables
* machine learning models built using BigQuery ML

Location: EU

---

## Cloud Storage

Bucket created:

pharmacy-data-kaust

Purpose:

* storage for raw datasets
* staging area before loading data into BigQuery

Region:

europe-west2 (London)

---

## Budget Monitoring

A monthly cloud budget has been configured to control project costs.

Budget:

£50/month

Alerts:

* 50%
* 75%
* 90%

This ensures cloud usage remains well within the available free credits.
