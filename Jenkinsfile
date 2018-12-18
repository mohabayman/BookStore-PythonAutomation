pipeline {
  agent none
  stages {
    stage('Branch1') {
      parallel {
        stage('Branch1') {
          steps {
            build 'Job1.1'
          }
        }
        stage('Branch2') {
          steps {
            build 'Job2.1'
          }
        }
      }
    }
  }
}