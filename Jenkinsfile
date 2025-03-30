pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'  // Define AWS Region globally
    }

    stages {

           stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install boto3
                '''
            }
        }
        stage('Checkout Code') {
            steps {
              git branch: 'main', url: 'https://github.com/superdoo/pipeline_project.git'
            }
        }

        stage('AWS CLI Version') {
            steps {
                sh 'aws --version'  // Ensure AWS CLI is available
            }
        }

        stage('AWS Setup Test') { // Echo creds and check caller ID
            steps {
                script {
                    withCredentials([aws(credentialsId: 'my-aws-credentials-id', variable: 'AWS')]) {
                        echo "AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}"  // This will NOT print secrets for security reasons
                        sh 'aws sts get-caller-identity'
                    }
                }
            }
        }

        stage('Upload to S3') {
            steps {
                script {
                    withCredentials([aws(credentialsId: 'my-aws-credentials-id', variable: 'AWS')]) {
                        sh "python3 upload_to_s3.py"
                    }
                }
            }
        }
    }
}
