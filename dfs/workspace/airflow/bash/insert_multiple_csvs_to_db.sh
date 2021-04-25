#!/usr/bin/env bash

table_ls=$1
csv_files_ls=$2
path=$3
delimeter=$4


#echo $table_ls $csv_files_ls
#ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  echo $table_ls $csv_files_ls $delimeter
  cd /home/baadmin/Documents/dfs/workspace/dfs_dmd_etl/sqlscripts/

  ./insert_multiple_csvs_to_db.sh "${table_ls}" $path "${csv_files_ls}" $delimeter

#EOF

