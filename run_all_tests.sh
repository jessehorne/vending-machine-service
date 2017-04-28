#!/bin/bash

echo "Starting server..."

python vending_machine_service/vending_machine_service.py &

sleep 10

echo "Running tests..."

cd vending_machine_service/
python -m pytest ../tests

cd ../
