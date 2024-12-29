pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\shama\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\shama\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
        SCANNER_PATH = 'C:\\Users\\shama\\Downloads\\sonar-scanner-cli-6.2.1.4610-windows-x64\\bin' // Add the path to sonar-scanner
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Set the PATH and install dependencies using pip
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                '''
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonar-token') // Accessing the SonarQube token stored in Jenkins credentials
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%SCANNER_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=test27 ^
                  -Dsonar.sources=. ^
                  -Dsonar.host.url=http://localhost:9000 ^
                  -Dsonar.token=%SONAR_TOKEN%
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}

