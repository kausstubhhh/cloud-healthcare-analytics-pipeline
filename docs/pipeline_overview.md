# Data Pipeline Overview

This project implements a cloud-based healthcare analytics pipeline.

## Stage 1 — Data Ingestion

Dataset is uploaded and stored in BigQuery as a raw table.

Table:

```
prescriptions_raw
```

## Stage 2 — Data Cleaning

SQL transformations remove null values and standardise column names.

Table:

```
prescriptions_clean
```

## Stage 3 — Feature Engineering

Derived metrics such as BMI are calculated.

Table:

```
prescriptions_features
```

## Stage 4 — Exploratory Data Analysis

Python notebooks analyse distributions and correlations.

Notebook:

```
notebooks/eda_analysis.ipynb
```

## Stage 5 — Machine Learning

Three ML models are trained using BigQuery ML.

Regression Model

```
weight_prediction_model
```

Classification Model

```
bmi_classification_model
```

Forecasting Model

```
prescription_forecast_model
```

## Stage 6 — Predictions and Forecasts

Model predictions and forecasts are generated using:

* ML.PREDICT
* ML.EVALUATE
* ML.FORECAST
