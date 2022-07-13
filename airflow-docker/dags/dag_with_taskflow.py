from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner':'harshab',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

@dag(dag_id='dag_with_taskflow_api_v03', 
     default_args=default_args, 
     start_date=datetime(2022, 7, 12), 
     schedule_interval='@daily')

def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Harsha',
            'last_name': 'Bash'
        }
    
    @task()
    def get_age():
        return 25

    @task()
    def greet(first_name, last_name, age):
        print(f"Hi, My name is {first_name} {last_name}, and "
        f"I am {age} years old!")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'],age=age)

greet_dag = hello_world_etl()