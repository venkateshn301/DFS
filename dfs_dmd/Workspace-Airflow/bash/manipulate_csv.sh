#!/usr/bin/env bash
csv_file=$1
date_no_dash=$2
infix_csv_file=$3
suffix_csv_file=$4
withoutdash=$(echo $infix_csv_file$date_no_dash$suffix_csv_file | cut -d'/' -f 2)


echo $csv_file$date_no_dash$infix_csv_file$date_no_dash$suffix_csv_file
ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  cd $csv_file$date_no_dash
  pwd
   rm -f manipulated_csv.csv
  tail -n +12 $withoutdash |head -n -1 > manipulated_csv.csv
  mv manipulated_csv.csv $withoutdash
EOF
