# Specify the node base image with node:<version>
# I found this from Docker Hub
FROM node:16-alpine

# Expose port 5000
EXPOSE 5000

# Set conventional WORKDIR
WORKDIR /usr/src/app

# Copy all of the source code
COPY . .

# Install all packages with npm install
# RUN npm run build and connect to backend
# Use package called "serve" to serve the project in port 5000:
RUN npm install && \
    REACT_APP_BACKEND_URL=http://localhost:8080 npm run build && \
    npm install -g serve && \
    adduser appuser --disabled-password

# Change the user with the directive USER 
USER appuser

# And finally the command to run the application
CMD ["serve", "-s", "-l", "5000", "build"]