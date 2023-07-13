# Specify the golang base image with golang:<version>
# I found this from Docker Hub
FROM golang:1.16-apline

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

# Add user called "appuser"
RUN adduser appuser \
    --disabled-password

# Set frontend URL to pass through cors check
ENV REQUEST_ORIGIN=http://localhost:5000

# Change the user with the directive USER 
USER appuser

# And finally the command to run the application
CMD ["./server"]
