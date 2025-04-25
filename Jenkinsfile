pipeline {
  agent any
  environment {
    IMAGE = "janhvi512/studentproject"
    CREDS = credentials('dockerhub-creds')
  }
  stages {
    stage('Checkout') {
      steps { git 'https://github.com/<your-username>/<your-repo-name>.git' }
    }
    stage('Build') {
      steps { sh "docker build -t ${IMAGE} ." }
    }
    stage('Push') {
      steps {
        sh "echo ${CREDS_PSW} | docker login -u ${CREDS_USR} --password-stdin"
        sh "docker push ${IMAGE}"
      }
    }
  }
}
