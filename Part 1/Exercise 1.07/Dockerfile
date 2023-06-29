# Start from the ubuntu:20.04 image
FROM ubuntu:20.04

# Use /usr/src/app as our workdir. The following instructions will be executed in this location.
WORKDIR /usr/src/app

# Download updated package information
RUN apt-get update

# Install curl
RUN apt-get -y install curl

# Copy the search_website.sh file from this location to /usr/src/app/ creating /usr/src/app/search_website.sh
COPY search_website.sh .

# Add execution permissions during the build.
RUN chmod +x search_website.sh

# When running docker run the command will be ./search_website.sh
CMD ./search_website.sh