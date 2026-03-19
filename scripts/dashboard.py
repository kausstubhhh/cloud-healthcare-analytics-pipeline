from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# -----------------------------
# AUTHENTICATION (FIXED)
# -----------------------------
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id
)

# -----------------------------
# APP CONFIG
# -----------------------------
st.set_page_config(page_title="Healthcare Analytics Dashboard", layout="wide")

st.title("Healthcare Analytics Dashboard")
st.write("Cloud-based analytics using BigQuery ML")

# -----------------------------
# HELPER FUNCTION
# -----------------------------
@st.cache_data
def load_data(query):
    try:
        return client.query(query).to_dataframe()
    except Exception as e:
        st.error(f"Query failed: {e}")
        return pd.DataFrame()

# -----------------------------
# EDA SECTION
# -----------------------------
st.header("Exploratory Data Analysis")

query_eda = """
SELECT height_inches, weight_pounds, bmi
FROM `healthcare-analytics-kaust.pharmacy_analytics.prescriptions_features`
"""

df = load_data(query_eda)

if not df.empty:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Height Distribution")
        fig1, ax1 = plt.subplots()
        ax1.hist(df['height_inches'], bins=20)
        st.pyplot(fig1)

    with col2:
        st.subheader("Weight Distribution")
        fig2, ax2 = plt.subplots()
        ax2.hist(df['weight_pounds'], bins=20)
        st.pyplot(fig2)

    with col3:
        st.subheader("BMI Distribution")
        fig3, ax3 = plt.subplots()
        ax3.hist(df['bmi'], bins=20)
        st.pyplot(fig3)

else:
    st.warning("EDA data not available")

# -----------------------------
# REGRESSION PREDICTIONS
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

if not df_pred.empty:
    st.dataframe(df_pred)
else:
    st.warning("Prediction data not available")

# -----------------------------
# FORECAST SECTION
# -----------------------------
st.header("Prescription Forecast")

query_forecast = """
SELECT *
FROM ML.FORECAST(
MODEL `healthcare-analytics-kaust.pharmacy_analytics.prescription_forecast_model`,
STRUCT(30 AS horizon)
)
"""

df_forecast = load_data(query_forecast)

if not df_forecast.empty:
    st.subheader("Forecasted Prescription Demand")

    # Ensure datetime
    df_forecast['forecast_timestamp'] = pd.to_datetime(df_forecast['forecast_timestamp'])

    # Sort (important for proper line plotting)
    df_forecast = df_forecast.sort_values('forecast_timestamp')

    fig, ax = plt.subplots()
    ax.plot(df_forecast['forecast_timestamp'], df_forecast['forecast_value'])

    ax.set_xlabel("Date")
    ax.set_ylabel("Predicted Demand")
    ax.set_title("Prescription Demand Forecast")

    st.pyplot(fig)

else:
    st.warning("Forecast data not available")
