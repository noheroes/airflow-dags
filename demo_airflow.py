# Hooks
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
# Utility
from airflow import DAG
from airflow.operators.python import PythonOperator, get_current_context
from airflow.models import Variable
import airflow.utils.dates
# Additional
import json
import datetime as dt
from datetime import timedelta
import logging

def _json_to_s3(ts) -> str:
    data = '{"valor":"hola mundo!"}'
    logging.info('File name {}'.format(ts))
    key = f'json/{ts}.json'
    s3_hook = S3Hook(aws_conn_id='my-tenant')
    print(f's3_hook: {s3_hook}')
    if(s3_hook):
      s3_hook.load_string(
        string_data=json.dumps(data),
        key = key,
        bucket_name = 'airflowpipeline'
      )
    return key

def _init() -> str:
    context = get_current_context()
    print(f'context: {context}')
    ts_nodash = context['ts_nodash']
    print(f'ts_nodash: {ts_nodash}')
    key = _json_to_s3(ts_nodash)
    return key

default_args = {
   'owner': 'noheroes',
   'depends_on_past': False,
   'start_date': dt.datetime(2022,8,17), #airflow.utils.dates.days_ago(1),
   'email': ['rporrasz@hotmail.com'],
   'email_on_failure': False,
   'email_on_retry': False,
   #'retries': 1,
   #'retry_delay': timedelta(minutes = 5),
}

dag = DAG(
        "demo_airflow",
        default_args = default_args,
        description = "demo airflow",
        catchup = False,
        schedule_interval = None, #"@hourly",
      )

t1 = PythonOperator(task_id='demo1', python_callable=_init, dag=dag)

t1