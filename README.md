
# Airflow Setup Using Docker Compose

## Prerequisites

Ensure you have the following installed:
- **Docker**: [Download and install Docker](https://www.docker.com/get-started)
- **Docker Compose**: Comes pre-installed with Docker Desktop.
- **Docker Compose link **: **https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml

## Step 1: Set Up Project Directory

Make sure to set up your project directory where the `docker-compose.yml` and necessary folders (`dags`, `logs`, `plugins`) will reside.

```bash
export AIRFLOW_PROJ_DIR=~/materials
mkdir -p $AIRFLOW_PROJ_DIR/dags $AIRFLOW_PROJ_DIR/logs $AIRFLOW_PROJ_DIR/plugins
```

## Step 2: Define `docker-compose.yml`

Ensure your `docker-compose.yml` file is correctly configured and placed in the root of the project directory (`$AIRFLOW_PROJ_DIR`).

## Step 3: Initialize Airflow and Build Docker Containers

Run the following commands to set up the necessary Airflow components and initialize the environment:

1. **Pull Airflow image and initialize the environment:**

   ```bash
   docker-compose up airflow-init
   ```

   This step ensures the Airflow environment is initialized, creating the necessary database tables and setting up your environment.

2. **Start all Airflow services (scheduler, webserver, workers, triggerer, and Flower):**

   ```bash
   docker-compose up -d
   ```

   This will start the services in detached mode.

3. **Start Flower (optional for monitoring):**

   To start Flower along with the other services, run:

   ```bash
   docker compose --profile flower up -d
   ```

   If you want Flower to always start, remove the `profiles` line from the `flower` service in the `docker-compose.yml`.

## Step 4: Verify Airflow Webserver

Once the services are up, visit the Airflow web UI by navigating to `http://localhost:8080` in your browser.

- Username: `airflow`
- Password: `airflow`

## Step 5: Manually Running a DAG Task

You can manually test a DAG and specific tasks using the following command. For example, to test the `create_table` task of the `user_processing` DAG:

1. Access the Airflow scheduler container:

   ```bash
   docker exec -it materials-airflow-scheduler-1 /bin/bash
   ```

2. Run the task:

   ```bash
   airflow tasks test user_processing create_table 2024-01-01
   ```

## Step 6: Access PostgreSQL for Verification

To verify that the `users` table was created in PostgreSQL:

1. Access the PostgreSQL container:

   ```bash
   docker exec -it materials-postgres-1 /bin/bash
   ```

2. Log into PostgreSQL:

   ```bash
   psql -U airflow -d airflow
   ```

3. Run the following commands to list tables and view data:

   ```bash
   \d users;
   SELECT * FROM users;
   ```

## Step 7: Access Flower for Monitoring

Flower, which is used to monitor Celery workers, can be accessed at:

```bash
http://localhost:5555
```

You can monitor your task queue and the status of workers here.

## Step 8: Copy `airflow.cfg` (Optional)

If you need to modify the `airflow.cfg` file or use it as a template, you can copy it from the running scheduler container as follows:

```bash
docker cp materials-airflow-scheduler-1:/opt/airflow/airflow.cfg .
```

## Step 9: Clean Up

To stop and remove all the services, run:

```bash
docker-compose down
```

If you want to clean up all containers and volumes (including the database):

```bash
docker-compose down -v
```

---

## Troubleshooting

- **Port Already Allocated Error**: If you encounter a port binding error, ensure that the specified ports (e.g., `5432`, `8080`, `5555`) are not being used by other services.
- **Resource Warnings**: Ensure your system meets the recommended resources (at least 4GB of memory and 2 CPUs) for running Airflow smoothly.
  
Feel free to update the configuration based on your needs or infrastructure setup.

---

This should provide you with a step-by-step guide to running Airflow using Docker Compose. Let me know if you encounter any issues!
