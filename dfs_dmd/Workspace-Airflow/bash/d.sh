#!/bin/bash
echo ========executing file in airflow!!!===============
para1=$1
para2=$2
para3=$3
para4=$4
para5=$5
export para1
export para2
export para3
export para4
export para5
ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  cd /home/ubuntu/dfs_dmd_etl
  source /home/ubuntu/.virtualenvs/dmd_etl/bin/activate
  ./fetch_api_data.py $para1 $para2 $para3 $para4 $para5
EOF

