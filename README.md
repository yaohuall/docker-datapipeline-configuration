# docker-datapipeline-configuration
docker configuration for minio, postgres, airflow, nifi, spark

## initialize the pipeline
run `docker compose up -d`

### convert jupyter notebook to .py file
run `jupyter nbconvert --to=script [yourfilename]`

### check linux system version
run `ls -l /etc/*-release` 

## airflow setting
### airflow config path
run `cd /opt/bitnami/airflow`
### setting AWS env variables in .env file for airflow
`AIRFLOW_CONN_S3_CONN='aws://<access_key_id>:<secret_key_id>@'`

⚠️ Note: connection id using environment variables will not show in airflow UI


### reference
https://towardsdatascience.com/how-to-build-a-data-lake-from-scratch-part-2-connecting-the-components-1bc659cb3f4f
https://hub.docker.com/r/bitnami/minio/

### data-reference
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

### airflow reference
https://airflow.apache.org/docs/apache-airflow/2.1.0/howto/connection.html
