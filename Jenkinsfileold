pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install boto3
                '''
            }
        }

        stage('Upload to S3') {
            steps {
                sh '''
                . venv/bin/activate
                python3 upload_to_s3.py
                '''
            }
        }
    }
}
