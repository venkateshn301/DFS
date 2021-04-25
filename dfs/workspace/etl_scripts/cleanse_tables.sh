#!/usr/bin/env bash
echo ========executing this cleanse_tables===============
cd /home/baadmin/Documents/dfs/workspace/dfs_dmd_etl/sqlscripts/tablescripts
#DATABASE_PSQL="psql -d $1 -h $2 -U $3 --set ON_ERROR_STOP=on -e"
DATABASE_PSQL="psql -d extractordb -h dev-extractor-db.cnimcclfnoqr.eu-west-1.rds.amazonaws.com -U masteruser --set ON_ERROR_STOP=on -e"

$DATABASE_PSQL -f $1  