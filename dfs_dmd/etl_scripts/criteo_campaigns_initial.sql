CREATE TABLE IF NOT EXISTS dmd_staging.criteo_campaigns
(
  "campaignID" serial NOT NULL,
  "campaignName" character varying(500),
  "endDate" date,
  "budgetID" integer,
  "remainingDays" integer,
  "status" character varying(255),
  "categoryBids" character varying(255),

  CONSTRAINT criteo_campaigns_pkey PRIMARY KEY ("campaignID")
);

TRUNCATE TABLE  dmd_staging.criteo_campaigns;

