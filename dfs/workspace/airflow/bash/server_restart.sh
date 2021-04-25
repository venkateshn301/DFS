#!/usr/bin/env bash

server_name=$1
echo =======inside restart server.sh =====

#ssh dev.dmd.etl1 << EOF
  echo ========executing this file in ETL!!! ===============
  cd /home/baadmin/Documents/dfs/workspace/dfs_dmd_etl/sqlscripts
  ./restart_server.sh $server_name
#EOF
