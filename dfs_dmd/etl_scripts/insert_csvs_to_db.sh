#!/usr/bin/env bash
echo ========executing this insert_csv_db===============
cd /home/ubuntu/etl_scripts/
#DATABASE_PSQL="psql -d $1 -h $2 -U $3 --set ON_ERROR_STOP=on -e"
DATABASE_PSQL="psql -d extractordb -h dev-extractor-db.cnimcclfnoqr.eu-west-1.rds.amazonaws.com -U masteruser --set ON_ERROR_STOP=on -e"


$DATABASE_PSQL -c "\copy dmd_staging.$1 FROM '$2' CSV HEADER DELIMITER '$3'";
