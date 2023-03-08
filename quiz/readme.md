# Azeno quiz

## Run Development
1. Copy `backend/.envs/.env-default` to `backend/.envs/.env` and fill environmental variables.
2. Copy `.envs/env_db-default` to `.envs/.env_db` and fill environmental variables.
3. Start services `docker compose up --build`.

## Run Production
1. Copy `backend/.envs/.env-default` to `backend/.envs/.env` and fill environmental variables.
2. Copy `.envs/env_db-default` to `.envs/.env_db` and fill environmental variables.
3. Start services `docker compose -f docker-compose.prod.yaml up --build`.