#! /bin/bash
ssh jenkins@35.189.107.29 << EOF
cd QA-SFIA-2/
export DATABASE_URI=mysql+pymysql://root:1234@34.105.158.49/project2db
export SECRET_KEY=aujdhfouisnbfdbsedohgosiehdjgoshedpgnsdoia
docker stack deploy --compose-file docker-compose.yaml application
EOF