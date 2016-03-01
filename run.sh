#git pull
mvn -f pom.xml clean compile assembly:single
nohup java -jar target/portfolio-timeline-jar-with-dependencies.jar | tee build.out

