#! /bin/bash
ssh jenkins@project-2-manager << EOF
git clone https://github.com/BWDaniels97/QA-SFIA-2.git
cd QA-SFIA-2/
git checkout ansible
docker stack deploy --compose-file docker-compose.yaml application
EOF
