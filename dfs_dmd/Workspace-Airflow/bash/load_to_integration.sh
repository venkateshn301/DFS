#!/usr/bin/env bash
echo ====== executing in airflow==================
ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  /home/ubuntu/dfs_dmd_etl/sqlscripts/load_to_integration.sh
EOF