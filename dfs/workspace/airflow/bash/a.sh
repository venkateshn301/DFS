#!/usr/bin/env bash
para1=$1
para2=$2
ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  cd /home/ubuntu/etl_scripts
  ./insert_csvs_to_db.sh $para1 $para2
EOF

