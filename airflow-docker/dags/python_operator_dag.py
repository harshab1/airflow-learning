from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner':'harshab',
    'retries': 5,
    'retry_delay':timedelta(minutes=2)

}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"hello World! My name is {first_name} {last_name},"
           f"and I am {age} years old!")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Harsha'),
    ti.xcom_push(key='last_name', value='Bash')

def get_age(ti):
    ti.xcom_push(key='age', value=25)

with DAG(
    dag_id='python_operator_dag_v7',
    description='Example DAGs using PythonOperator',
    default_args=default_args,
    start_date=datetime(2022,7,12,2),
    schedule_interval='@daily'
) as dag:

    task1 = PythonOperator(
        task_id = 'Greeting',
        python_callable=greet, 
        # op_args=['Harsha', 25]
        # op_kwargs={'age': 25}
    )

    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id = "get_age",
        python_callable=get_age

    )

    [task2, task3] >> task1

