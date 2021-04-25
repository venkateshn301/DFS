#!/usr/bin/env bash
echo ================test!!!!!!!!==========
para1=$1

ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  echo /home/ubuntu/csv_files/$para1/"$(date +"%Y%m%d")"
  mkdir -p /home/ubuntu/csv_files/$para1/"$(date +"%Y%m%d")"
  
EOF


