#!/bin/bash
echo ========executing create_table sh!!!===============
para1=$1
#ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  cd /home/baadmin/Documents/dfs/workspace/etl_scripts
	./cleanse_tables.sh $para1
  echo =====create_table_success=========
#EOF            