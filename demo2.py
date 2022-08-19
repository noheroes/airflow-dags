import airflow.utils.dates
import datetime as dt
from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id="01_Ejemplo",
    description="01_Ejemplo",
    start_date=dt.datetime(2022, 2, 1),
    schedule_interval="@daily",
)

extraccion = DummyOperator(task_id="extraccion", dag=dag)
transformacion = DummyOperator(task_id="transformacion", dag=dag)
load = DummyOperator(task_id="load", dag=dag)

extraccion >> transformacion >> load