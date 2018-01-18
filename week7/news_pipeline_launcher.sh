#!/bin/bash
service mongod start
service redis_6379 start
redis-cli flushall

pip3 install -r requirements.txt

cd news_pipeline
python3 queue_helper.py
python3 news_monitor.py &
python3 news_fetcher.py &
python3 news_deduper.py &

echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)
cd ..
