# Specify the Java base image with openjdk:<version>
FROM openjdk:8

# Expose port 8080
EXPOSE 8080

# Set conventional WORKDIR
WORKDIR /usr/src/app

# Copy all of the source code
COPY . .

# Build project
RUN ./mvnw package

# And finally the command to run the application
CMD ["java", "-jar", "./target/docker-example-1.1.3.jar"]