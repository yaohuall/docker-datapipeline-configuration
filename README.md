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

### reference
https://towardsdatascience.com/how-to-build-a-data-lake-from-scratch-part-2-connecting-the-components-1bc659cb3f4f
https://hub.docker.com/r/bitnami/minio/

### data-reference
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
