from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from email_on_failure import send_email_failure

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'retries': 0,
    'retry_delay': timedelta (minutes=2),
}

dag = DAG (
    'huhuv12', default_args=default_args, schedule_interval='@once')

dummy_test = DummyOperator(
    task_id='test_dummy',
    dag=dag
)

test_bash = BashOperator (
    task_id='test_Bash',
    dag=dag,
    bash_command=" cd /home/dawd",
    on_failure_callback=send_email_failure
)



