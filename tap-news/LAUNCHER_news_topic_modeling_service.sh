#!/bin/bash
service mongod start
service redis_6379 start

cd news_topic_modeling_service/server
python3 server.py &

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)
cd ../..
