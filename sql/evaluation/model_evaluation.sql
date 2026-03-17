-- Phase 5: Evaluate Regression Model

SELECT
*
FROM
ML.EVALUATE(
MODEL `healthcare-analytics-kaust.pharmacy_analytics.weight_prediction_model`
);
