FROM node:18.14.2-slim as development

WORKDIR /app

COPY ./package.json ./package-lock.json ./
COPY ./bank/package.json ./bank/package-lock.json ./bank/
RUN npm ci -W

FROM development as builder

COPY ./.eslintignore ./.eslintrc.json ./.prettierrc.json ./tsconfig.json ./
COPY ./bank/ ./bank/
RUN npm run build-storybook


FROM nginx:1.23.3 as production
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
