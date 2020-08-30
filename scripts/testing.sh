#!/bin/bash
sudo apt-get update
sudo apt update && sudo apt install -y python3 python3-pip python3-venv
pip3 install -r service1/requirements.txt

export DATABASE_URI=${DATABASE_URI}
export SECRET_KEY=${SECRET_KEY}
export TEST_DB_URI=${TEST_DB_URI}
export TEST_SECRET_KEY=${TEST_SECRET_KEY}

cd service1
pytest --cov application
cd ..

cd service2
pytest --cov
cd ..

cd service3
pytest --cov
cd ..

cd service4
pytest --cov
cd ..

