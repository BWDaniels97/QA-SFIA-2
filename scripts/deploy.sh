#! /bin/bash
ssh jenkins@project-2-manager << EOF
git clone https://github.com/BWDaniels97/QA-SFIA-2.git
cd QA-SFIA-2/
git checkout ansible
export DATABASE_URI=mysql+pymysql://root:1234@34.105.158.49/project2db
export SECRET_KEY=aujdhfouisnbfdbsedohgosiehdjgoshedpgnsdoia
docker stack deploy --compose-file docker-compose.yaml application
EOF
