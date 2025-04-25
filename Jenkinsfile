pipeline {
  agent any
  environment {
    IMAGE = "janhvi512/studentproject"
  }

  stages {
    stage('Build') {
      steps {
        sh "docker build -t ${IMAGE} ."
      }
    }

    stage('Push') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'CREDS_USR',
          passwordVariable: 'CREDS_PSW'
        )]) {
          sh "echo ${CREDS_PSW} | docker login -u ${CREDS_USR} --password-stdin"
          sh "docker push ${IMAGE}"
        }
      }
    }
  }

  post {
    success {
      echo "✅ Successfully built and pushed ${IMAGE}"
    }
    failure {
      echo "❌ Build failed — check logs"
    }
  }
}
