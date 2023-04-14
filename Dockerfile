FROM node:18.14.2-slim as development

WORKDIR /project

COPY ./bank ./bank
COPY ./package.json ./package-lock.json ./
RUN npm install ./bank
RUN npm ci -W
