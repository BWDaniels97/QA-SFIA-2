pipeline{
        agent any

	stages{

		stage ('Test application'){
			steps{
				sh "scripts/testing.sh"
			} 
		}
            	
		stage('Install Docker using ansible'){
                	steps{
                        	sh "scripts/ansible.sh"
                	}
            	}
		stage ('install Docker'){
                        steps{
                                sh "scripts/docker.sh"
                        }
                }
                stage('Deploy application'){
                        steps{
                                sh "scripts/deploy.sh"

                        }

        	}
	}
}
