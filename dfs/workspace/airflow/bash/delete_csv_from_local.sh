#!/usr/bin/env bash
csv_file=$1
date_no_dash=$2
infix_csv_file=$3
suffix_csv_file=$4

echo $csv_file$date_no_dash$infix_csv_file$date_no_dash$suffix_csv_file

#ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  rm -f $csv_file$date_no_dash$infix_csv_file$date_no_dash$suffix_csv_file

#EOF
