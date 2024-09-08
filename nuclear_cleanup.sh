#!/bin/bash

echo "Stopping all running containers..."
docker compose down

echo "Removing all stopped containers..."
docker container prune -f

echo "Removing unused and dangling images..."
docker image prune -f

echo "Removing all volumes..."
docker volume prune -f

echo "Removing all build cache..."
docker builder prune -f

echo "removing unused network..."
docker network prune -f

echo "Docker cleanup completed, retaining all images."