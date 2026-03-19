from google.cloud import bigquery
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Initialize BigQuery client
client = bigquery.Client()

# App title
st.title("Healthcare Analytics Dashboard")
st.write("Cloud-based analytics using BigQuery ML")

# -----------------------------
# Helper function
# -----------------------------
@st.cache_data
def load_data(query):
    return client.query(query).to_dataframe()

# -----------------------------
# EDA Section
# -----------------------------
st.header("Exploratory Data Analysis")

query_eda = """
SELECT height_inches, weight_pounds, bmi
FROM `healthcare-analytics-kaust.pharmacy_analytics.prescriptions_features`
"""

df = load_data(query_eda)

# Height Distribution
st.subheader("Height Distribution")
fig1, ax1 = plt.subplots()
ax1.hist(df['height_inches'], bins=20)
ax1.set_title("Height Distribution")
st.pyplot(fig1)

# Weight Distribution
st.subheader("Weight Distribution")
fig2, ax2 = plt.subplots()
ax2.hist(df['weight_pounds'], bins=20)
ax2.set_title("Weight Distribution")
st.pyplot(fig2)

# BMI Distribution
st.subheader("BMI Distribution")
fig3, ax3 = plt.subplots()
ax3.hist(df['bmi'], bins=20)
ax3.set_title("BMI Distribution")
st.pyplot(fig3)

# -----------------------------
# Regression Predictions
# -----------------------------
st.header("Regression Predictions")

query_pred = """
SELECT *
FROM ML.PREDICT(
MODEL `healthcare-analytics-kaust.pharmacy_analytics.weight_prediction_model`,
(
SELECT height_inches
FROM `healthcare-analytics-kaust.pharmacy_analytics.prescriptions_features`
LIMIT 50
)
)
"""

df_pred = load_data(query_pred)
st.dataframe(df_pred)

# -----------------------------
# Forecast Section
# -----------------------------
st.header("Prescription Forecast")

query_forecast = """
SELECT *
FROM ML.FORECAST(
MODEL `healthcare-analytics-kaust.pharmacy_analytics.prescription_forecast_model`,
STRUCT(30 AS horizon)
)
"""

# IMPORTANT: Load forecast data
df_forecast = load_data(query_forecast)

st.subheader("Forecasted Prescription Demand")

# Convert to datetime
df_forecast['forecast_timestamp'] = pd.to_datetime(df_forecast['forecast_timestamp'])

# Plot forecast
fig, ax = plt.subplots()
ax.plot(df_forecast['forecast_timestamp'], df_forecast['forecast_value'])

ax.set_xlabel("Date")
ax.set_ylabel("Predicted Demand")
ax.set_title("Prescription Demand Forecast")

st.pyplot(fig)