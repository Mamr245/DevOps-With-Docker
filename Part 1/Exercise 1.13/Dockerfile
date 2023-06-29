# Specify the golang base image with golang:<version>
# I found this from Docker Hub
FROM golang:1.16

# Expose port 8080
EXPOSE 8080

# Set conventional WORKDIR
WORKDIR /usr/src/app

# Copy all of the source code
COPY . .

# Build project
RUN go build

# Test project
RUN go test ./...

# And finally the command to run the application
CMD ["./server"]
