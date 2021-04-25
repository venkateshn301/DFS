import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yaml
import yml_file_location
import sys


conf = yaml.load(open(yml_file_location.file_location))

def send_email_failure(params):
    task_id=params['ti'].task_id
    dag_id=params['ti'].dag_id
    start_time=params['ti'].start_date
    end_time=params['ti'].end_date
    duration=params['ti'].duration
    log=getattr(params['ti'], 'log_filepath')
    url=getattr(params['ti'], 'log_url')

    body_for_mail = open("/home/ubuntu/workspace/airflow/dags/failure_DMD_template.html").read().format(name='Administrator DMD Data Sources', emailbody='You are receiving this email due to a failure of one of your data extraction jobs for DMD Production,Please log in to Airflow for more details.\n \n Following are some information related to the failed job.', dag_id=dag_id, task_id=task_id, start_time=start_time, end_time=end_time, duration=duration, log=log, url=url)


    fromaddr = conf['email']['from_email']
    toaddr = conf['email']['to_email']
    msg = MIMEMultipart ()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Job Execution Failed for DMD "

    body = body_for_mail    
    msg.attach (MIMEText (body, 'html'))

    server = smtplib.SMTP (conf['email']['smtp_host'], conf['email']['smtp_port'])
    server.starttls ()
    server.login (fromaddr, conf['email']['from_email_pass'])
    text = msg.as_string ()
    server.sendmail (fromaddr, toaddr.split(','), text)
    server.quit ()





