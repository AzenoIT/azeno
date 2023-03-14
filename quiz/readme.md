# Azeno quiz

## Run Development

1. Copy `envs/web.default.env` to `envs/web.env` and fill environmental variables.
2. Copy `envs/postgres.default.env` to `envs/postgres.env` and fill environmental variables.
3. Copy `envs/backend.default.env` to `envs/backend.env` and fill environmental variables.
4. Start services `docker compose up --build`.

## Run Production

1. Copy `envs/web.default.env` to `envs/web.env` and fill environmental variables.
2. Copy `envs/postgres.default.env` to `envs/postgres.env` and fill environmental variables.
3. Copy `envs/backend.default.env` to `envs/backend.env` and fill environmental variables.
4. Start services `docker compose -f docker-compose.prod.yaml up --build`.

## How to run black code formatter

1. Install the Black extension in your IDE.
2. Configure Black to use configuration file form `pyproject.toml`.
3. Use hotkey to format code.

### Alternative way to run black formatter: 
 
- Run the Black formatter by using the following command for all files:
  > docker compose exec <service_name> black ..
- To check only one file, run the following command:
  > docker compose exec <service_name> black <file_name>
  