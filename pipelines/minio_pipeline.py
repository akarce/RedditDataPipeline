from etls.minio_etl import connect_to_minio, create_bucket_if_not_exist, upload_to_minio
from utils.constants import MINIO_BUCKET_NAME

def upload_minio_pipeline(ti, subreddit):
    # Get file path of the CSV from the corresponding subreddit extraction task
    file_path = ti.xcom_pull(task_ids=f'reddit_extraction_group.reddit_extraction_{subreddit}', key='return_value')

    s3 = connect_to_minio()
    create_bucket_if_not_exist(s3, MINIO_BUCKET_NAME)
    minio_file_name = file_path.split('/')[-1]
    upload_to_minio(s3, file_path, MINIO_BUCKET_NAME, f'{minio_file_name}')  # Subreddit specific path
