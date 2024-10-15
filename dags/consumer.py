from airflow import DAG, Dataset
from datetime import datetime, timedelta

from airflow.decorators import task 

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

with DAG(
    dag_id="consumer",
    schedule=[my_file, my_file_2],
    start_date=datetime(2022, 1, 1),
    catchup=False,
):
    @task(outlets=[my_file])
    def read_dataset():
        print("read data set...")
        with open(my_file.uri, "a+") as f:
            print(f.read())
    
    read_dataset()