# docker-datapipeline-configuration
docker configuration for minio, postgres, airflow, nifi, spark

## initialize the pipeline
    docker compose up -d

## airflow setting

### airflow config path
    cd /opt/bitnami/airflow

### setting AWS env variables in .env file for airflow
    AIRFLOW_CONN_S3_CONN='aws://<access_key_id>:<secret_key_id>@'

```diff 
- ⚠️  Note: connection id using environment variables will not show in airflow UI 
```

### using kompose convert docker-compose.yml to k8s yamls
    curl -L https://github.com/kubernetes/kompose/releases/download/v1.26.0/kompose-linux-amd64 -o kompose
    kompose convert

### reference
https://towardsdatascience.com/how-to-build-a-data-lake-from-scratch-part-2-connecting-the-components-1bc659cb3f4f
https://hub.docker.com/r/bitnami/minio/
https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/

### data-reference
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

### airflow reference
https://airflow.apache.org/docs/apache-airflow/2.1.0/howto/connection.html

### code reference
#### check linux system version
    ls -l /etc/*-release

#### convert jupyter notebook to .py file
    jupyter nbconvert --to=script [yourfilename]
