export AIRFLOW_PROJ_DIR=~/materials 

docker exec -it materials-airflow-scheduler-1 /bin/bash


airflow tasks test user_processing create_table 2024-01-01



docker exec -it materials-postgres-1 psql -U airflow -d airflow

docker exec -it  materials-postgres-1 /bin/bash

psql -Uairflow
\d users;
select * from users;

# Create airflow.cfg
docker cp materials-airflow-scheduler-1:/opt/airflow/airflow.cfg .