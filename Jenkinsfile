pipeline {
  agent none
  stages {
    stage('Lower Envs') {
      parallel {
        stage('Dev') {
          steps {
            build 'Job1.1'
            build 'Job1.2'
          }
        }
        stage('US T') {
          steps {
            build 'Job2.1'
          }
        }
        stage('EU T') {
          steps {
            build 'Job1.2'
          }
        }
      }
    }
  }
}