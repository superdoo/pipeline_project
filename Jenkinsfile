pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
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

    stage('Check AWS Credentials') {
        steps {
            script {
                sh 'env | grep AWS'  // This will check if the AWS env vars are set
                }
            }
        }

    stage('Run Python Script with Parameter') {
            steps {
                script {
                    sh "python3 script.py Michael"
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

