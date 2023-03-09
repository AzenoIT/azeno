# Azeno quiz

## Run Development

1. Copy `web.default.env` to `web.env` and fill environmental variables.
2. Copy `envs/db.default.env` to `.envs/db.env` and fill environmental variables.
3. Copy `backend/.envs/.env-default` to `backend/.envs/.env` and fill environmental variables.
4. Start services `docker compose up --build`.

## Run Production

1. Copy `web.default.env` to `web.env` and fill environmental variables.
2. Copy `envs/db.default.env` to `envs/.db.env` and fill environmental variables.
3. Copy `backend/.envs/.env-default` to `backend/.envs/.env` and fill environmental variables.
4. Start services `docker compose -f docker-compose.prod.yaml up --build`.
