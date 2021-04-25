CREATE TABLE IF NOT EXISTS dmd_staging.test_doubleclick_search_keyword
(
  date date,
  account character varying,
  campaign character varying,
  campaignid character varying,
  campaignstatus character varying,
  keywordid character varying,
  keywordmatchtype character varying,
  keywordtext character varying,
  keywordengineid character varying,
  keywordmaxcpc double precision,
  effectivekeywordmaxcpc double precision,
  keywordlabels character varying,
  effectivelabels character varying,
  avgcpc double precision,
  avgcpm double precision,
  avgpos double precision,
  clicks double precision,
  cost double precision,
  ctr double precision,
  impr double precision,
  adwordsconversions double precision,
  adwordsconversionvalue double precision,
  visits integer,
  cpa double precision,
  aov double precision,
  calls integer,
  cmbs integer,
  uniquelands integer,
  revenue double precision,
  sales integer,
  storelocator integer,
  videochats integer,
  allconversions integer
)
