from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'insight-dan',
    'depends_on_past': False,
    'start_date': datetime(2019, 3, 28,9,42,0),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('s3RedditPyspark', default_args=default_args, schedule_interval=timedelta(1))

print("executing ")
firstScript= BashOperator(
task_id='first_script_task',
bash_command='python first.py',
dag=dag
)

secondScript=BashOperator(
task_id='second_script_task',
bash_command='python second.py',
dag=dag
)

secondScript.set_upstream(firstScript)