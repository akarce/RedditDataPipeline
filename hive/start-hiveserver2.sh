#!/bin/bash

# Check if HiveServer2 is already running and stop it
PID=$(pgrep -f hiveserver2)
if [ ! -z "$PID" ]; then
  echo "Stopping existing HiveServer2 process with PID $PID..."
  kill -9 $PID
  sleep 5  # Wait for the process to terminate properly
fi

# Check if the process was successfully terminated
if pgrep -f hiveserver2 > /dev/null; then
  echo "Failed to stop existing HiveServer2 process. Exiting..."
  exit 1
fi

# Start HiveServer2
echo "Starting HiveServer2..."
/opt/hive/bin/hive --skiphadoopversion --skiphbasecp --service hiveserver2

# Check if HiveServer2 started successfully
if [ $? -ne 0 ]; then
  echo "Failed to start HiveServer2. Exiting..."
  exit 1
fi

echo "HiveServer2 started successfully."
