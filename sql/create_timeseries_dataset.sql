CREATE OR REPLACE TABLE
`healthcare-analytics-kaust.pharmacy_analytics.prescription_timeseries`
AS

SELECT
DATE_ADD(DATE '2023-01-01', INTERVAL record_id DAY) AS prescription_date,
weight_pounds AS prescription_volume
FROM
`healthcare-analytics-kaust.pharmacy_analytics.prescriptions_features`
ORDER BY prescription_date;
