# Use a small version of Java to run the app
FROM openjdk:11-jre-slim

# Take the result of the Maven build and put it in the box
COPY target/*.jar app.jar

# Tell the box to run the app when it opens
ENTRYPOINT ["java", "-jar", "app.jar"]
