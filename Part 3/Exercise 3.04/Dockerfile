FROM alpine:latest

WORKDIR /usr/src/app

RUN apk update && \
    apk add --no-cache bash && \
    apk add git && \
    apk add docker

COPY . .

ENTRYPOINT ["/usr/src/app/builder.sh"]

# docker run -e DOCKER_USER=<username> -e DOCKER_PWD=<password> -v /var/run/docker.sock:/var/run/docker.sock builder <github repository> <docker hub repository>
# Example: <github repository> -------->  Mamr245/DevOps-Docker-Express-app 
# Example: <docker hub repository> ---->  mamr24/expressapp
