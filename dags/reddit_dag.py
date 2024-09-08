import os
import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.minio_pipeline import upload_minio_pipeline

default_args = {
    'owner': 'Ceyhun Akar',
    'start_date': datetime(2024, 9, 5)
}

adjusted_time = datetime.now() + timedelta(hours=3)
file_postfix = adjusted_time.strftime("%Y%m%d%H%M")

# List of subreddits to be extracted
subreddits = ['dataengineering', 'machinelearning', 'datascience', 'ArtificialInteligence']

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# Define a task group for extraction tasks
with TaskGroup(group_id='reddit_extraction_group', dag=dag) as extract_group:
    extract_tasks = {}
    for subreddit in subreddits:
        extract_task = PythonOperator(
            task_id=f'reddit_extraction_{subreddit}',
            python_callable=reddit_pipeline,
            op_kwargs={
                'file_name': f'reddit_{subreddit}_{file_postfix}',
                'subreddit': subreddit,
                'time_filter': 'day',
                'limit': 100
            },
            dag=dag
        )
        extract_tasks[subreddit] = extract_task

# Define a task group for S3 upload tasks
with TaskGroup(group_id='s3_upload_group', dag=dag) as upload_group:
    for subreddit in subreddits:
        upload_task = PythonOperator(
            task_id=f's3_upload_{subreddit}',
            python_callable=upload_minio_pipeline,
            op_kwargs={'subreddit': subreddit},
            dag=dag
        )
        # Set task dependencies within task groups
        extract_tasks[subreddit] >> upload_task

# Establish dependencies between the TaskGroups
extract_group >> upload_group
