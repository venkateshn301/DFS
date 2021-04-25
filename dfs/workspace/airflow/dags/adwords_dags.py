from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from email_on_failure import send_email_failure
import yaml
import yml_file_location

conf = yaml.load(open(yml_file_location.file_location))
paras = conf['parameters']['ad_words_impression_share']
delimeter = '","'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018,7,16),
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    'AdWords', default_args=default_args, schedule_interval='0 1 * * 2')

dummy_test = DummyOperator(
    task_id='test_dummy',
    dag=dag
)

fetch_data_from_api = BashOperator(
    task_id='fetch_data_from_api',
    dag=dag,
    bash_command=conf['bash_path']['fetch_data_from_api_location'] + ' ' + paras["api_provider"] + ' ' + paras[
        "data_set"] + ' ' + paras["csv_file_location"] + ' ' + paras["start_date"] + ' ' + paras[
                     "end_date"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' +
                 paras["csv_file_locationv3"] + ' ' + '{{ds}}',
)

cleanse_table = BashOperator(
    task_id='cleanse_table',
    dag=dag,
    bash_command=conf['bash_path']['cleanse_table_location'] + ' ' + paras["sql_script"],
)

insert_multiple_csvs = BashOperator(
            task_id='insert_multiple_csv_to_db',
            bash_command=conf['bash_path']['insert_multiple_csv_to_db_location_1'] + ' ' + paras[
                "csv_file"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' + paras[
                             "csv_file_locationv3"],
    dag=dag,

        )

fetch_data_from_api.set_downstream(cleanse_table)
cleanse_table.set_downstream(insert_multiple_csvs)

