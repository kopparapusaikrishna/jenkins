pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/kopparapusaikrishna/jenkins'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x main.py"
                sh "./main.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
}
