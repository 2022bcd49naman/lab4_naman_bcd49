pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "2022bcd0049namanomar/wine-quality"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                python train.py
                '''
            }
        }

        stage('Read Accuracy') {
            steps {
                script {
                    def metrics = readJSON file: 'app/artifacts/metrics.json'
                    env.CURRENT_ACCURACY = metrics.accuracy.toString()
                    echo "Current Accuracy: ${env.CURRENT_ACCURACY}"
                }
            }
        }

        stage('Compare Accuracy') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'best-accuracy', variable: 'BEST_ACC')]) {
                        def bestAcc = BEST_ACC.toFloat()
                        def currentAcc = env.CURRENT_ACCURACY.toFloat()

                        if (currentAcc > bestAcc) {
                            env.BUILD_NEW_MODEL = "true"
                        } else {
                            env.BUILD_NEW_MODEL = "false"
                        }
                    }
                }
            }
        }

        stage('Build Docker Image') {
            when {
                expression { env.BUILD_NEW_MODEL == "true" }
            }
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                        def image = docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                        image.tag("latest")
                    }
                }
            }
        }

        stage('Push Docker Image') {
            when {
                expression { env.BUILD_NEW_MODEL == "true" }
            }
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_NUMBER}").push()
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'app/artifacts/**', fingerprint: true
        }
    }
}
