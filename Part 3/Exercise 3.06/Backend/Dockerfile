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
RUN go build && \ 
    useradd -m appuser

# Add user called "appuser"
USER appuser

# Set frontend URL to pass through cors check in order to access the backend
ENV REQUEST_ORIGIN=http://localhost:5000

# And finally the command to run the application
CMD ["./server"]
