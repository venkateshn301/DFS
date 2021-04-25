CREATE TABLE IF NOT EXISTS dmd_staging.test_gapremium_daily_visits
(
  date date,
  country character varying,
  device character varying,
  medium character varying,
  source character varying,
  totaltransactions integer,
  totaltransactionsrevenue double precision,
  totaltime double precision,
  totalbounces integer,
  totalhits integer,
  totalpageviews integer,
  totalnewvisits integer,
  totalvisits integer
)
