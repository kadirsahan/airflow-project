from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'docker_ansible_sample',
    default_args=default_args,
    schedule_interval="@once",
    start_date=days_ago(2),
)

t1 = BashOperator(task_id='print_date', bash_command='date', dag=dag)

t2 = BashOperator(task_id='sleep', bash_command='sleep 5', retries=3, dag=dag)

t3 = DockerOperator(
    api_version='1.41',
    docker_url='tcp://192.168.60.11:2375',  # Set your docker URL
    command='',
    image='kadirsahan/masdeploy:v1',
    network_mode='bridge',
    environment={
        'slp': 10
    },
    task_id='docker_ansible_copy_jar',
    dag=dag,
)


t4 = BashOperator(task_id='print_hello', bash_command='echo "hello world!!!"', dag=dag)


t1 >> t2
t1 >> t3
t3 >> t4