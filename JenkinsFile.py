pipeline {
    agent any 
    stages {
        stage('Build & Test') {
            steps {
                // This command tells Maven to check your Even/Odd logic
                sh 'mvn clean package' 
            }
        }
        stage('Docker Build') {
            steps {
                // This command creates the Docker "container"
                sh 'docker build -t even-odd-app .'
            }
        }
    }
}
