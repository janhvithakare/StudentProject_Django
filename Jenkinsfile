pipeline {
  agent any
  environment {
    IMAGE = "janhvi512/studentproject"
  }

  stages {
    stage('Build') {
      steps {
        // Use 'bat' instead of 'sh' on Windows
        bat "docker build -t ${IMAGE} ."
      }
    }

    stage('Push') {
      steps {
        // Wrap credentials for Docker login
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'CREDS_USR',
          passwordVariable: 'CREDS_PSW'
        )]) {
          // Note Windows piping syntax
          bat """
            echo %CREDS_PSW% | docker login -u %CREDS_USR% --password-stdin
            docker push ${IMAGE}
          """
        }
      }
    }
  }

  post {
    success {
      echo "✅ Built & pushed ${IMAGE}:latest"
    }
    failure {
      echo "❌ Pipeline failed—check the logs above."
    }
  }
}
