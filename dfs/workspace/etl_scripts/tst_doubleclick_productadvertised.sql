CREATE TABLE IF NOT EXISTS dmd_staging.test_doubleclick_search_products
(
  date date,
  accountid character varying,
  campaignid character varying,
  productid character varying,
  clicks double precision,
  cost double precision,
  ctr double precision,
  impr double precision,
  revenue double precision,
  sales integer,
  storelocator integer,
  allconversions integer
)
