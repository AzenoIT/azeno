FROM node:18.14.2-slim as development

WORKDIR /project

COPY ./bank ./bank
COPY ./package.json ./package-lock.json ./
COPY flashcards/web/package.json flashcards/web/package-lock.json ./flashcards/web/
RUN npm ci
RUN npm install -w flashcards/web ./bank

FROM development as builder

COPY ./.eslintignore ./.eslintrc.json ./.prettierrc.json ./tsconfig.json ./
COPY flashcards/web/ ./flashcards/web
RUN npm run flashcards/web build


FROM nginx:1.23.3 as production
EXPOSE 3000
COPY .flashcards/web/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /project/flashcards/app/dist /usr/share/nginx/html
