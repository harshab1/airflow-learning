from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'harshab',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
    
}

with DAG(
    dag_id='our_first_dag_v4',
    description='This is the first dag',
    default_args=default_args,
    start_date=datetime(2022,7,13,2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task'

    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo I am the second task"
    )

    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo Iam task3, will be executed after task1 along with task2"
    )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    task1 >> [task2, task3]