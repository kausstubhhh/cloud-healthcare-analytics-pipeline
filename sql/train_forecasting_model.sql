CREATE OR REPLACE MODEL
`healthcare-analytics-kaust.pharmacy_analytics.prescription_forecast_model`
OPTIONS(
model_type='ARIMA_PLUS',
time_series_timestamp_col='prescription_date',
time_series_data_col='prescription_volume'
)
AS

SELECT
prescription_date,
prescription_volume
FROM
`healthcare-analytics-kaust.pharmacy_analytics.prescription_timeseries`;
