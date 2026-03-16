SELECT
*
FROM
ML.FORECAST(
MODEL `healthcare-analytics-kaust.pharmacy_analytics.prescription_forecast_model`,
STRUCT(30 AS horizon)
);
