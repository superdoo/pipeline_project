pipeline {
    agent any

    environment {
                         // Use Jenkins credentials for AWS access keys
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'my-aws-credentials-id']]) {
                        // Configure AWS CLI with the credentials
                        sh 'aws configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}'
                        sh 'aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}'
                        sh 'aws configure set region ${AWS_REGION}'
    }
    }



    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/superdoo/pipeline_project.git'
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

    stage('AWS CLI Version') {
        steps {
            sh 'aws --version'  // Ensure AWS CLI is available
            }
        }

    stage('AWS Setuptest') { //supposed to echo creds and check caller id
            steps {
                script {
                    echo "AWS_ACCESS_KEY_ID: ${env.AWS_ACCESS_KEY_ID}"
                    echo "AWS_SECRET_ACCESS_KEY: ${env.AWS_SECRET_ACCESS_KEY}"
                    sh 'aws sts get-caller-identity'
                }
            }
        }
        stage('Upload to S3') {
            steps {
                script {
                    sh "python3 upload_to_s3.py"
                }
            }
        }
    }
}

