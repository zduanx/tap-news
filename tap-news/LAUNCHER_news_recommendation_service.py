#!/bin/bash
service mongod start
service redis_6379 start

cd news_recommendation_service
python3 click_log_processor.py &
python3 recommendation_service.py &

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)
cd ..
