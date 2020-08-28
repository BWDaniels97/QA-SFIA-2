pipeline{
        agent any

	stages{

		stage ('install Docker'){
                        steps{
                                sh "docker.sh"
                        }
                }

		stage ('Test application'){
			steps{
				sh "testing.sh"
			} 
		}
            	
		stage('Install Docker using ansible'){
                	steps{
                        	sh "ansible.sh"
                	}
            	}
                stage('Deploy application'){
                        steps{
                                sh "deploy.sh"

                        }

        	}
	}
}
