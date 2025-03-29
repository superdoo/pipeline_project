pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/superdoo/pipeline_project.git'  // Replace with your GitHub repo
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                script {
                    // Create virtual environment and install dependencies
                    sh 'python -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Run your Python code to query DB and upload to S3
                    sh './venv/bin/python query_customer.py'
                    sh './venv/bin/python upload_to_s3.py'
                }
            }
        }
    }
}
