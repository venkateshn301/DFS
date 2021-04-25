from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from CustomBigquerySensor import CustomBigquerySensor


args = {
    'owner': 'airflow',
    'start_date': datetime(2017,12,22),
    'email_on_failure': True,
    'email_on_retry':True,
    'depends_on_past':False,
    'email': 'aulpathakumbura@mitrai.com',
    'retries':3,
    'retry_delay':timedelta(minutes=1),
}


dag = DAG (dag_id='Test_bigquery_sensorv14', schedule_interval='@monthly', default_args=args)




test_big = CustomBigquerySensor(
    task_id='test_big',
    dataset_id='109512292',
    project_id='nice-road-184014',
    table_id='ga_sessions_',
    poke_interval=1800,
    dag=dag)





test = DummyOperator (
    task_id='test_dummy',
    dag=dag
)

test_2 = DummyOperator(
    task_id='dummy_start',
    dag=dag
)
test_2.set_downstream(test_big)
test_big.set_downstream (test)
