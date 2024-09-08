echo "Initializing Airflow database..."
docker-compose up airflow-init


echo "Starting docker containers in detached mode "
docker-compose up -d