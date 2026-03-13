-- Phase 5: Train Regression Model

CREATE OR REPLACE MODEL
`healthcare-analytics-kaust.pharmacy_analytics.weight_prediction_model`
OPTIONS(
model_type='linear_reg',
input_label_cols=['weight_pounds']
)
AS

SELECT
height_inches,
weight_pounds
FROM
`healthcare-analytics-kaust.pharmacy_analytics.prescriptions_features`;
