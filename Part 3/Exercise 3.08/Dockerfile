FROM node:16-alpine as build-stage
ENV REACT_APP_BACKEND_URL=http://localhost:8080
WORKDIR /usr/src/app
COPY . .
RUN npm install && npm run build 

FROM alpine:latest
WORKDIR /usr/src/app
COPY --from=build-stage /usr/src/app/build /usr/src/app/build
RUN REACT_APP_BACKEND_URL=http://localhost:8080 npm run build && \
    apk add --update nodejs npm && npm install -g serve
EXPOSE 5000
CMD ["serve", "-s", "-l", "5000", "build"]