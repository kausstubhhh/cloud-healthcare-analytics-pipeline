-- Phase 3: Data Cleaning Pipeline

CREATE OR REPLACE TABLE
`healthcare-analytics-kaust.pharmacy_analytics.prescriptions_clean`
AS

SELECT
CAST(Index AS INT64) AS record_id,
CAST(` Height_Inches__` AS FLOAT64) AS height_inches,
CAST(`Weight_Pounds_` AS FLOAT64) AS weight_pounds

FROM
`healthcare-analytics-kaust.pharmacy_analytics.prescriptions_raw`
WHERE
` Height_Inches__` IS NOT NULL
AND `Weight_Pounds_` IS NOT NULL;
