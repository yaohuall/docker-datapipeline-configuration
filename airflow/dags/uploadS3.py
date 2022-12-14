from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.models import DAG
import datetime as dt

def upload_to_s3(filename: str, key: str, bucket_name: str) -> None:
    s3 = S3Hook('S3_CONN')
    s3.load_file(filename, key=key, bucket_name=bucket_name)

with DAG (dag_id='s3_dag', schedule= "25 15 * * *", start_date= dt.datetime(year=2022, month=12, day=13), catchup=False) as dag:

    # Upload the file
    task_upload_to_s3 = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3,
        op_kwargs={
            'filename': "/opt/bitnami/airflow/data/test.txt",
            'key': "test/my-test-upload-file.txt",
            'bucket_name': "yaohua-tf-test-bucket"
        }
    )

start = EmptyOperator(task_id="start")

start >> task_upload_to_s3