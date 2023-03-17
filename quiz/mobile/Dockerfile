# Linux system
FROM ubuntu:22.04

# install Node.js v.18
RUN apt-get update && \
  apt-get install -y  curl && \
  curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
  apt-get install -y nodejs

# Setup the directory for the container
WORKDIR /app
COPY . .

# install the npm dependencies + a GLOBAL expo command line interface
RUN npm install && npm install -g expo-cli
CMD [ "npm", "start" ]