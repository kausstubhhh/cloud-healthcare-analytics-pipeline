# Phase 2 — Data Ingestion

This phase loads a healthcare dataset into the cloud data warehouse.

## Pipeline Architecture

Local Dataset
↓
Google Cloud Storage
↓
BigQuery Table

## Dataset

File:

prescriptions_dataset.csv

This dataset was used to initialise the cloud data pipeline.

## Cloud Storage

Bucket:

pharmacy-data-kaust

The dataset was uploaded to the bucket as:

prescriptions_dataset.csv

## BigQuery

Dataset:

pharmacy_analytics

Table created:

prescriptions_raw

## Purpose

The `prescriptions_raw` table represents the raw ingestion layer of the data pipeline.

Future phases will transform this dataset into cleaned and feature-engineered tables for analytics and machine learning.
