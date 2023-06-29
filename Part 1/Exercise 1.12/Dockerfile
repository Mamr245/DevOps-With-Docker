# Specify the node base image with node:<version>
# I found this from Docker Hub
FROM node:16

# Expose port 5000
EXPOSE 5000

# Set conventional WORKDIR
WORKDIR /usr/src/app

# Copy all of the source code
COPY . .

# Install all packages with npm install
RUN npm install

# Build static files
RUN npm run build

# Use package called "serve" to serve the project in port 5000:
RUN npm install -g serve

# And finally the command to run the application
CMD ["serve", "-s", "-l", "5000", "build"]
