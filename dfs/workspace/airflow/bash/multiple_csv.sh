#!/usr/bin/env bash
echo ========executing file in airflow!!!===============
#ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============

  cd /home/baadmin/Documents/dfs/worksapce/dfs_dmd_etl
  source /home/baadmin/.virtualenvs/Airflow_new/bin/activate
    ./multiple_csvs.py
#EOF
