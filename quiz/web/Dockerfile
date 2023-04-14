FROM node:18.14.2-slim as development

WORKDIR /project

COPY ../bank ./bank
COPY ./ ./quiz/web
COPY ../package.json ../package-lock.json ./
RUN npm ci -W

FROM development as builder

COPY ../../bank ../../bank
COPY ../../.eslintignore ../../.eslintrc.json ../../.prettierrc.json ../../tsconfig.json ./ ./
RUN npm run build


FROM nginx:1.23.3 as production
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
