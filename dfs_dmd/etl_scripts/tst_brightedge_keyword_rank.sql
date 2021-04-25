CREATE TABLE IF NOT EXISTS dmd_staging.test_brightedge_keyword_rank
(
  search_engine character varying(255),
  device character varying(50),
  domain character varying(255),
  absolute_domain_rank integer,
  keyword character varying(255),
  keywordid character varying(255),
  domain_name character varying(255),
  absolute_url_rank integer,
  plp_blended_rank integer,
  rank integer,
  plp_rank integer,
  blended_rank integer,
  "time" character varying(100),
  serp_type integer,
  category character varying(100),
  is_mydomain integer,
  accountid character varying(255)
)
