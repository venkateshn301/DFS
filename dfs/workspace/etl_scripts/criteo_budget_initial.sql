CREATE TABLE IF NOT EXISTS dmd_staging.criteo_budget
(
  "budgetID" serial NOT NULL,
  "budgetName" character varying(500),
  "totalAmount" numeric,
  "remainingBudget" numeric,
  "remainingBudgetUpdated" date,
  CONSTRAINT criteo_budget_pkey PRIMARY KEY ("budgetID")
);

TRUNCATE TABLE dmd_staging.criteo_budget;

