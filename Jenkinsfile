@Library('jenkings') _

pipeline {
  agent {
    label '!docker-qemu'
  }

  environment {
    CI = 'true'
  }

  stages {
    stage('docker image') {
      /*when {
        branch 'master'
      }*/

      agent {
        label 'docker-qemu'
      }

      stages {
        stage('build') {
          steps {
            script {
              sh "docker image build -t alkesst/biceater-api:${GIT_COMMIT} --pull ."
              sh "docker image tag alkesst/biceater-api:${GIT_COMMIT} alkesst/biceater-api:latest"
            }
          }
        }

        stage('push') {
          steps {
            script {
              docker.withRegistry('', 'alkesst_dockerhub') {
                sh "docker image push alkesst/biceater-api:${GIT_COMMIT}"
                sh "docker image push alkesst/biceater-api:latest"
              }
            }
          }
        }

        // stage('refresh env') {
        //   step {
        //     sh 'curl https://portainer.majorcadevs.com/...'
        //   }
        // }
      }
    }
  }
}