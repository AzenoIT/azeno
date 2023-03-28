FROM node:18.14.2-slim as development

WORKDIR /app

COPY ./package.json ./package-lock.json ./
RUN npm ci

FROM development as builder

COPY . .
RUN npm run build


FROM nginx:1.23.3 as production
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
