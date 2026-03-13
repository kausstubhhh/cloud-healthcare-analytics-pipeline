-- Phase 3: Feature Engineering

CREATE OR REPLACE TABLE
`healthcare-analytics-kaust.pharmacy_analytics.prescriptions_features`
AS

SELECT
record_id,
height_inches,
weight_pounds,
(weight_pounds / (height_inches * height_inches)) * 703 AS bmi
FROM
`healthcare-analytics-kaust.pharmacy_analytics.prescriptions_clean`;
