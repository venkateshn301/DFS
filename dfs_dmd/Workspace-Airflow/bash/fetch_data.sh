#!/bin/bash
echo ========executing file in airflow!!!===============
api_provider=$1
data_set=$2
csv_file_location=$3
start_date=$4
end_date=$5
date_no_dash=$6
csv_file_locationv2=$7
csv_file_locationv3=$8
date_with_dash=$9
reorder_file_location=${10}
reorder_file_name=${11}
export api_provider
export data_set
export csv_file_location
export start_date
export end_date
export date_no_dash
export csv_file_locationv2
export csv_file_locationv3
export date_with_dash
export reorder_file_location
export reorder_file_name
echo $api_provider $data_set $csv_file_location$date_no_dash$csv_file_locationv2$date_no_dash$csv_file_locationv3 $start_date$date_with_dash $end_date$date_with_dash
ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  cd /home/ubuntu/dfs_dmd_etl
  source /home/ubuntu/.virtualenvs/dmd_etl/bin/activate
  
  if  [ -z "$reorder_file_location" ]; then
  
     ./fetch_api_data.py $api_provider $data_set $csv_file_location$date_no_dash$csv_file_locationv2$date_no_dash$csv_file_locationv3 $start_date$date_with_dash $end_date$date_with_dash
    
  elif [ -z "$reorder_file_name" ]; then

     ./fetch_api_data.py $api_provider $data_set $csv_file_location$date_no_dash$csv_file_locationv2$date_no_dash$csv_file_locationv3 $start_date$date_with_dash $end_date$date_with_dash $reorder_file_location$date_no_dash/

  else

    ./fetch_api_data.py $api_provider $data_set $csv_file_location$date_no_dash$csv_file_locationv2$date_no_dash$csv_file_locationv3 $start_date$date_with_dash $end_date$date_with_dash $reorder_file_location$date_no_dash$reorder_file_name$date_no_dash$csv_file_locationv3
  fi


  #./fetch_api_data.py $api_provider $data_set $csv_file_location$date_no_dash$csv_file_locationv2$date_no_dash$csv_file_locationv3 $start_date$date_with_dash $end_date$date_with_dash
EOF

