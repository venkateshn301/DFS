import airflow
import time
from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.subdag_operator import SubDagOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.sensors import TimeSensor
from DMD_Subdag import dmd_subdag, dmd_subdag_multiple_csv
from CustomBigquerySensor import CustomBigquerySensor
import yaml
import yml_file_location
import sys
import datetime as dt
from email_on_failure import send_email_failure

conf = yaml.load(open(yml_file_location.file_location))


DAG_NAME = 'Jobsv31'




args = {
    'owner': 'airflow',
    'start_date': datetime(2016,1,1),
    'email_on_failure': True,
    'email_on_retry':True,
    'depends_on_past':False,
    'email': 'aulpathakumbura@mitrai.com',
    'retries':3,
    'retry_delay':timedelta(minutes=1),

}
dag = DAG(
    dag_id=DAG_NAME,
    default_args=args,
    schedule_interval='0 1 * * *',
    catchup=False,
    #concurrency=1,
)


brightedge_keyword_rank_data = SubDagOperator(
    task_id='brightedge_keyword_rank_data',
    subdag=dmd_subdag(DAG_NAME, 'brightedge_keyword_rank_data',args, conf['parameters']['brightedge_keyword_rank_data_paras']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag
)



brightedge_share_of_voice = SubDagOperator(
    task_id='brightedge_share_of_voice',
    subdag=dmd_subdag(DAG_NAME, 'brightedge_share_of_voice',args, conf['parameters']['brightedge_share_of_voice_paras']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)

doubleclick_search_campaign = SubDagOperator(
    task_id='doubleclick_search_campaign',
    subdag=dmd_subdag(DAG_NAME, 'doubleclick_search_campaign',args, conf['parameters']['doubleclick_search_campaign_paras']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)

doubleclick_search_productadvertised = SubDagOperator(
    task_id='doubleclick_search_productadvertised',
    subdag=dmd_subdag(DAG_NAME, 'doubleclick_search_productadvertised',args, conf['parameters']['doubleclick_search_productadvertised_paras']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)



doubleclick_search_keyword = SubDagOperator(
    task_id='doubleclick_search_keyword',
    subdag=dmd_subdag(DAG_NAME, 'doubleclick_search_keyword',args, conf['parameters']['doubleclick_search_keyword_paras']),
    trigger_rule=TriggerRule.ALL_DONE,
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)

doubleclick_dcm_standard_display_uk = SubDagOperator(
    task_id='doubleclick_dcm_standard_display_uk',
    subdag=dmd_subdag(DAG_NAME, 'doubleclick_dcm_standard_display_uk',args, conf['parameters']['doubleclick_dcm_standard_display_uk_paras'], manipulate_csv=True),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)



gapremiuim_dailyaggregatesfull = SubDagOperator(
    task_id='gapremiuim_dailyaggregatesfull',
    subdag=dmd_subdag(DAG_NAME, 'gapremiuim_dailyaggregatesfull',args, conf['parameters']['gapremiuim_dailyaggregatesfull_paras'], delimeter='"|"'),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)

responsetap_full_call_records = SubDagOperator(
    task_id='responsetap_full_call_records',
    subdag=dmd_subdag(DAG_NAME, 'responsetap_full_call_records',args, conf['parameters']['responsetap_full_call_records_paras']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)

partners_display_performance = SubDagOperator(
    task_id='display_performance',
    subdag=dmd_subdag(DAG_NAME, 'display_performance',args, conf['parameters']['partners_display_performance']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)

unique_visitors = SubDagOperator(
    task_id='total_unique_visitors',
    subdag=dmd_subdag(DAG_NAME, 'total_unique_visitors',args, conf['parameters']['total_unique_visitors']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
)

hitwise = SubDagOperator(
    task_id='hitwise',
    subdag=dmd_subdag_multiple_csv(DAG_NAME, 'hitwise', args, conf['parameters']['hitwise_data_paras']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
    )

criteo = SubDagOperator(
    task_id='criteo',
    subdag=dmd_subdag(DAG_NAME, 'criteo', args, conf['parameters']['criteo_campaigns_paras']),
    default_args=args,
    on_failure_callback=send_email_failure,
    dag=dag,
    )

server_restart = BashOperator(
    task_id='restart_server',
    bash_command=conf['bash_path']['restart_server']+' '+'UAT',
    on_failure_callback=send_email_failure,
    dag=dag
)

time_wait_till_6_00am = TimeSensor(
    task_id='time_wait_till_6_00am',
    target_time=dt.time(6,0,0,0),
    on_failure_callback=send_email_failure,
    dag=dag)

sensor_to_check_ga_table_preset = CustomBigquerySensor (
    task_id='sensor_to_check_ga_table_preset',
    dataset_id='109512292',
    project_id='nice-road-184014',
    table_id='ga_sessions_',
    poke_interval=300,
    on_failure_callback=send_email_failure,
    dag=dag)

integration_script = BashOperator(
    task_id='integration_script',
    bash_command=conf['bash_path']['load_to_integration_location']+' ',
    on_failure_callback=send_email_failure,
    dag=dag,)

dwh_script = BashOperator(
    task_id='dwh_script',
    bash_command=conf['bash_path']['load_to_dwh_location']+' ' ,
    on_failure_callback=send_email_failure,
    dag=dag
)


send_email = EmailOperator(
    to='aulpathakumbura@mitrai.com',
    task_id='send_email_after_all_success',
    subject='DAG run for {{ ds }} was successful.',
    html_content= 'All the task for {{ yesterday_ds }} was successful. For more details visit http://172.20.23.251:8080/admin/airflow/tree?num_runs=25&dag_id=Jobs',
    dag=dag)

brightedge_keyword_rank_data.set_downstream(integration_script)
brightedge_share_of_voice.set_downstream(integration_script)
doubleclick_search_campaign.set_downstream(integration_script)
doubleclick_search_productadvertised.set_downstream(integration_script)
doubleclick_search_keyword.set_downstream(integration_script)
doubleclick_dcm_standard_display_uk.set_downstream(integration_script)
partners_display_performance.set_downstream(integration_script)
time_wait_till_6_00am.set_downstream(partners_display_performance)
time_wait_till_6_00am.set_downstream(doubleclick_search_campaign)
time_wait_till_6_00am.set_downstream(doubleclick_dcm_standard_display_uk)
time_wait_till_6_00am.set_downstream(doubleclick_search_productadvertised)
time_wait_till_6_00am.set_downstream(sensor_to_check_ga_table_preset)
time_wait_till_6_00am.set_downstream(doubleclick_search_keyword)
sensor_to_check_ga_table_preset.set_downstream(unique_visitors)
sensor_to_check_ga_table_preset.set_downstream(gapremiuim_dailyaggregatesfull)
gapremiuim_dailyaggregatesfull.set_downstream(integration_script)
unique_visitors.set_downstream(integration_script)
responsetap_full_call_records.set_downstream(integration_script)
time_wait_till_6_00am.set_downstream(hitwise)
hitwise.set_downstream(integration_script)
criteo.set_downstream(integration_script)
integration_script.set_downstream(dwh_script)
dwh_script.set_downstream(server_restart)
server_restart.set_downstream(send_email)
