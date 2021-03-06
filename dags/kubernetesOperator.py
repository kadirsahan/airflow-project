from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import configuration as conf

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

namespace = conf.get('kubernetes', 'NAMESPACE')

# This will detect the default namespace locally and read the
# environment namespace when deployed to Astronomer.
# if namespace =='default':
#     config_file = '/usr/local/airflow/include/.kube/config'
#     in_cluster=False
# else:
#     in_cluster=True
#     config_file=None

dag = DAG('ks-6-example_kubernetes_pod',
          schedule_interval='@once',
          default_args=default_args)



with dag:
    k = KubernetesPodOperator(
        namespace='default',
        image="hello-world",
        labels={"foo": "bar"},
        name="airflow-test-pod",
        task_id="task-one",
        in_cluster=False,  # if set to true, will look in the cluster, if false, looks for file
        #cluster_context='k8s-test', # is ignored when in_cluster is set to True
        #config_file=config_file,
        is_delete_operator_pod=True,
        get_logs=True)
