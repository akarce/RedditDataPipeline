from minio import Minio
from minio.error import S3Error
from utils.constants import MINIO_ACCESS_KEY, MINIO_SECRET_KEY

def connect_to_minio():
    try:
        client = Minio("minio:9000",
                       access_key=MINIO_ACCESS_KEY,
                       secret_key=MINIO_SECRET_KEY,
                       secure=False
                       )
        print("Successfully connected to MinIO")
        return client
    except S3Error as e:
        print(f"Failed to connect to MinIO: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_bucket_if_not_exist(client: Minio, bucket: str):
    try:
        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)
            print(f"Bucket '{bucket}' created successfully.")
        else:
            print(f"Bucket '{bucket}' already exists.")
    except S3Error as e:
        print(f"Failed to create bucket: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def upload_to_minio(client: Minio, file_path: str, bucket: str, minio_file_name: str):
    try:
        client.fput_object(bucket, 'raw/' + minio_file_name, file_path)
        print('File uploaded to MinIO')
    except FileNotFoundError:
        print('The file was not found')
    except S3Error as e:
        print(f"Failed to upload file to MinIO: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")