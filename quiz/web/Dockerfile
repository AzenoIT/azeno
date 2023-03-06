FROM node:19.7.0-slim as builder

WORKDIR /opt/app

COPY ./package.json ./package-lock.json ./
RUN npm ci

COPY ./public ./public
COPY ./nginx ./nginx
COPY ./src ./src
COPY ./tsconfig.json ./tsconfig.node.json ./vite.config.ts ./index.html ./

RUN npm run build


FROM nginx:1.23.3 as production
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /opt/app/dist /usr/share/nginx/html
