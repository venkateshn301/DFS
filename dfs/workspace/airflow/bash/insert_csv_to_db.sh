#!/usr/bin/env bash
table_name=$1
prefix_csv_file=$2
date_no_dash=$3
infix_csv_file=$4
suffix_csv_file=$5
delimeter=$6


if [ "$1" == "brand_impression_share_competito" ]
then
    exit
fi

echo $table_name $prefix_csv_file$date_no_dash$infix_csv_file$date_no_dash$suffix_csv_file
#ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  echo $table_name $prefix_csv_file$date_no_dash$infix_csv_file$date_no_dash$suffix_csv_file $delimeter
  cd /home/baadmin/Documents/dfs/workspace/etl_scripts
  ./insert_csvs_to_db.sh $table_name $prefix_csv_file$date_no_dash$infix_csv_file$date_no_dash$suffix_csv_file $delimeter
#EOF

