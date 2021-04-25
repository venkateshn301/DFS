from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
import time
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import yaml
import yml_file_location

conf = yaml.load (open (yml_file_location.file_location))

def dmd_subdag(parent_dag_name, child_dag_name, args, paras, delimeter='","', manipulate_csv=False):
    """
       Returns subdag.
   :param parent_dag_name: Name of the parent DAG
   :type: parent_dag_name: String
   :param child_dag_name: Name of the child DAG(provide task id to prevent confusions)
   :type: child_dag_name: String
   :param args: A dictionary of default parameters
   :type: args: dict
   :param paras: A dictionary of parameters from config.yml
   :type: args: dict
   :param interval: Schedule interval for subdag
   :type: interval: string
   """

    dag_subdag = DAG (
    dag_id='%s.%s' % (parent_dag_name, child_dag_name),
    default_args=args,
    # schedule_interval=paras["interval"],
)

    create_folder_with_current_date = BashOperator (
    task_id='create_folder_with_current_date',
    bash_command=conf['bash_path']['create_folder_with_current_date_location'] + ' ' + paras[
        "folder_api_provider"] + ' ' + '{{ ds_nodash }}',
    dag=dag_subdag)


    fetch_data_from_api = BashOperator (
    task_id='fetch_data_from_api',
    bash_command=conf['bash_path']['fetch_data_from_api_location'] + ' ' + paras["api_provider"] + ' ' + paras[
        "data_set"] + ' ' + paras["csv_file_location"] + ' ' + paras["start_date"] + ' ' + paras[
                     "end_date"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' +
                 paras["csv_file_locationv3"] + ' ' + '{{ds}}',
    dag=dag_subdag)

    cleanse_table = BashOperator (
    task_id='cleanse_table',
    bash_command=conf['bash_path']['cleanse_table_location'] + ' ' + paras["sql_script"],
    dag=dag_subdag)

    insert_csv_to_db = BashOperator (
    task_id='insert_csv_to_db',
    bash_command=conf['bash_path']['insert_csv_to_db_location'] + ' ' + paras["table_name"] + ' ' + paras[
        "csv_file"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' + paras["csv_file_locationv3"]+' '+ delimeter,
    dag=dag_subdag)


    insert_csv_to_s3 = BashOperator(
        task_id='insert_csv_to_s3',
        bash_command=conf['bash_path']['insert_csv_to_s3_location'] + ' ' +paras[
        "csv_file"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' + paras["csv_file_locationv3"] + ' '+paras["folder_api_provider"],
        dag=dag_subdag
    )

    delete_csv_from_local = BashOperator(
        task_id='delete_csv_from_local',
        bash_command=conf['bash_path']['delete_csv_from_local_location'] + ' ' +paras[
        "csv_file"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' + paras["csv_file_locationv3"],
        dag=dag_subdag
    )

    if child_dag_name == 'ad_words_impression_share':
        insert_multiple_csvs = BashOperator(
            task_id='insert_multiple_csv_to_db',
            bash_command=conf['bash_path']['insert_multiple_csv_to_db_location_1'] + ' ' + paras[
                "csv_file"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' + paras[
                             "csv_file_locationv3"],
            dag=dag_subdag

        )

        fetch_data_from_api.set_downstream(cleanse_table)
        cleanse_table.set_downstream(insert_multiple_csvs)
        insert_multiple_csvs.set_downstream(delete_csv_from_local)

    else:
        if manipulate_csv == True:
            manipulate_csv = BashOperator(
                task_id='manipulate_csv',
                bash_command=conf['bash_path']['manipulate_csv_location'] + ' ' +paras["csv_file"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' + paras["csv_file_locationv3"],
                dag=dag_subdag
            )
            cleanse_table.set_downstream (manipulate_csv)
            manipulate_csv.set_downstream (insert_csv_to_db)
        else:
            cleanse_table.set_downstream(insert_csv_to_db)
        create_folder_with_current_date.set_downstream(fetch_data_from_api)
        fetch_data_from_api.set_downstream(cleanse_table)
        insert_csv_to_db.set_downstream(insert_csv_to_s3)
        insert_csv_to_s3.set_downstream(delete_csv_from_local)


    return dag_subdag


