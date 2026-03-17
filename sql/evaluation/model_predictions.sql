-- Phase 5: Generate Predictions

SELECT
height_inches,
predicted_weight_pounds
FROM
ML.PREDICT(
MODEL `healthcare-analytics-kaust.pharmacy_analytics.weight_prediction_model`,
(
SELECT
height_inches
FROM
`healthcare-analytics-kaust.pharmacy_analytics.prescriptions_features`
LIMIT 20
)
);
