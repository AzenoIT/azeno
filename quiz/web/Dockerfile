FROM node:18.14.2-slim as development

WORKDIR /project


COPY ./bank ./bank
COPY ./package.json ./package-lock.json ./
COPY quiz/web/package.json quiz/web/package-lock.json ./quiz/web/
RUN npm install -w quiz/web ./bank
RUN npm ci -W

FROM development as builder

COPY ./.eslintignore ./.eslintrc.json ./.prettierrc.json ./tsconfig.json ./
COPY quiz/web/ ./quiz/web
RUN npm run -w quiz/web build


FROM nginx:1.23.3 as production
EXPOSE 3000
COPY quiz/web/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /project/quiz/web/dist /usr/share/nginx/html
