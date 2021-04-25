from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from email_on_failure import send_email_failure
import yaml
import yml_file_location

conf = yaml.load(open(yml_file_location.file_location))
paras = conf['parameters']['hitwise_data_paras']
delimeter = '","'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 1, 1),
    'retries': 3,
    'retry_delay': timedelta (minutes=2),
}

dag = DAG(
    'hitwisev1', default_args=default_args, schedule_interval='0 6 * * *')

dummy_test = DummyOperator(
    task_id='test_dummy',
    dag=dag
)

create_folder = BashOperator(
    task_id='create_folder',
    dag=dag,
    bash_command=conf['bash_path']['create_folder_with_current_date_location'] + ' ' + paras[
        "folder_api_provider"] + ' ' + '{{ ds_nodash }}',
)

fetch_data = BashOperator(
    task_id='fetch_data',
    dag=dag,
    bash_command=conf['bash_path']['fetch_data_from_api_location'] + ' ' + paras["api_provider"] + ' ' +
                     paras["data_set"] + ' ' + paras["csv_file_location"] + ' ' + paras["start_date"] + ' ' +
                     paras["end_date"] + ' ' + ' {{ ds_nodash }} ' + ' ' + paras["csv_file_locationv2"] + ' ' +
                     paras["csv_file_locationv3"] + ' ' + '{{ds}}' + ' ' + paras["csv_file_location_2"])

cleanse_table = BashOperator (
    task_id='cleanse_table',
    dag=dag,
    bash_command=conf['bash_path']['cleanse_table_location'] + ' ' + paras["sql_script"],
)

insert_csv_to_db = BashOperator(
    task_id='insert_csv_to_db',
    dag=dag,
    bash_command=conf['bash_path']['insert_multiple_csv_to_db_location'] + ' ' + paras["table_list"] + ' ' +
                 paras["csv_list"] + ' ' + paras["csv_file"] + '{{ ds_nodash }}' + '/' + ' ' + delimeter
)

# insert_csv_to_s3 = BashOperator (
#     task_id='insert_csv_to_s3',
#     dag=dag,
#     bash_command=,
# )

# delete_csv_from_local = BashOperator (
#     task_id='delete_csv_from_local',
#     dag=dag,
#     bash_command=,
# )

#integration_script = BashOperator(
#    task_id='integration_script',
#    bash_command=conf['bash_path']['load_to_integration_location']+' ',
#    on_failure_callback=send_email_failure,
#    dag=dag,)

#dwh_script = BashOperator(
#    task_id='dwh_script',
#    bash_command=conf['bash_path']['load_to_dwh_location']+' ' ,
#    on_failure_callback=send_email_failure,
#    dag=dag
#)

create_folder.set_downstream(fetch_data)
fetch_data.set_downstream(cleanse_table)
cleanse_table.set_downstream(insert_csv_to_db)
#insert_csv_to_db.set_downstream(integration_script)
#integration_script.set_downstream(dwh_script)
# insert_csv_to_db.set_downstream(insert_csv_to_s3)
# insert_csv_to_s3.set_downstream(delete_csv_from_local)


