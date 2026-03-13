-- Extract feature importance from classification model

SELECT *
FROM ML.WEIGHTS(
MODEL `healthcare-analytics-kaust.pharmacy_analytics.bmi_classification_model`
);
