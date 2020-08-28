#!/bin/bash
sudo apt-get update
sudo apt update && sudo apt install -y python3 python3-pip python3-venv
pip3 install -r service1/requirements.txt

export DATABASE_URI=mysql+pymysql://root:1234@34.105.158.49/project2db
export SECRET_KEY=aujdhfouisnbfdbsedohgosiehdjgoshedpgnsdoia
export TEST_DB_URI=mysql+pymysql://root:1234@34.105.158.49/test_project2db
export TEST_SECRET_KEY=aujdhfouisnbfdbsedohgosiehdjgoshedpgnsdoia

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

