from pprint import pprint

from airflow import DAG
from datetime import timedelta

from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from pandas import read_csv

PATH = '/mnt/c/Users/FilipaPedrosa/PycharmProjects/AirflowPlayground/sourcecode/src/main/resources/google_playstore.csv'


def playground():
    print("Welcome to the Apache Airflow Playground!")
    define_dag_and_tasks()


def extract(ds, **kwargs):
    playstore_df = read_csv(PATH)
    print("Read google playstore CSV successfully")
    pprint(kwargs)
    print(ds)
    # Whatever you return gets printed in the logs
    return playstore_df.to_string().split('\n')[0] + "\n" + playstore_df.to_string().split('\n')[1]


def define_dag_and_tasks():
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }

    with DAG(
        dag_id='playground',
        default_args=default_args,
        description='A simple ETL pipeline DAG',
        schedule_interval=timedelta(days=1),
        start_date=days_ago(2),
        tags=['example']
    ) as dag:

        dag.doc_md = """
        Extracts data from csv file, applies transformations and writes file
        """

        extract_task = PythonOperator(task_id='extract_step', python_callable=extract)

        # transform_task

        # load_task

        # extract_task >> transform_task >> load_task