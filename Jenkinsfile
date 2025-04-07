pipeline {
    agent any

    environment {
        VENV_PATH = '. venv'
        BUCKET_NAME = 'reportsgraphs'
    }

    stages {
        stage('Checkout Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/superdoo/pipeline_project.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
            sh '''
            python3 -m venv $VENV_PATH
            $VENV_PATH/bin/activate  # Use "." instead of "source"
            pip install -r requirements.txt
            '''
            }
        }

        stage('Query Customer Data') {
            steps {
                sh '''
                $VENV_PATH/bin/activate
                python3 query_customer.py
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

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
