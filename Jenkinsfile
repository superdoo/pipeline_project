pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }

    stage('Check AWS Credentials') {
        steps {
            script {
                sh 'env | grep AWS'  // This will check if the AWS env vars are set
                }
            }
        }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/superdoo/pipeline_project.git'
            }
        }

        stage('Check AWS Credentials') {
            steps {
                script {
                    echo "AWS_ACCESS_KEY_ID is: ${AWS_ACCESS_KEY_ID}"
                    // Do NOT print AWS_SECRET_ACCESS_KEY to avoid exposing it
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
