#!/bin/bash
service mongod start
service redis_6379 start

cd backend_server
python3 service.py &

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)
cd ..
