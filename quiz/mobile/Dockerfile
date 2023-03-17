# Linux system
FROM ubuntu:22.04

# install Node.js v.18 and Cypress dependencies
RUN apt update && \
  apt-get install -y  curl && \
  curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
  apt-get install -y nodejs libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libxss1 libxtst6 xauth && \
  apt-get install -y xvfb  && \
  apt-get install -y libnss3 && \
  apt-get install -y libasound2

# Setup the directory for the container
WORKDIR /app
COPY . .

# install the npm dependencies + a GLOBAL expo command line interface
RUN npm install && npm install -g expo-cli
CMD [ "npm", "start" ]