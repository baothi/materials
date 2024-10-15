from airflow import DAG, Dataset
from datetime import datetime, timedelta

from airflow.decorators import task 

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

with DAG(
    dag_id="producer",
    schedule="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False,
):
    
    @task(outlets=[my_file])
    def update_dataset():
        print("Producing data...")
        with open(my_file.uri, "a+") as f:
            f.write(f"produced at {datetime.now()}\n")
    
    @task(outlets=[my_file_2])
    def update_dataset_2():
        print("Producing data...")
        with open(my_file_2.uri, "a+") as f:
            f.write(f"produced at {datetime.now()}\n")
    update_dataset()  >> update_dataset_2()