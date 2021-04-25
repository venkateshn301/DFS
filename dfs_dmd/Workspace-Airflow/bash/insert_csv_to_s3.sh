#!/usr/bin/env bash
csv_file=$1
date_no_dash=$2
infix_csv_file=$3
suffix_csv_file=$4
api_provider=$5
echo $csv_file$date_no_dash$infix_csv_file$date_no_dash$suffix_csv_file
echo $api_provider/$date_no_dash
ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  aws s3 cp $csv_file$date_no_dash$infix_csv_file$date_no_dash$suffix_csv_file s3://dmd-etl-test/$api_provider/$date_no_dash/
EOF


