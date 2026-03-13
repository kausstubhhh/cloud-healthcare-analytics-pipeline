-- Phase 6: Create classification dataset

CREATE OR REPLACE TABLE
`healthcare-analytics-kaust.pharmacy_analytics.bmi_classification_data`
AS

SELECT
record_id,
height_inches,
weight_pounds,
bmi,
CASE
  WHEN bmi >= 25 THEN 1
  ELSE 0
END AS high_bmi
FROM
`healthcare-analytics-kaust.pharmacy_analytics.prescriptions_features`;
