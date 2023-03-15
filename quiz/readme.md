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

## Testing

| service | type       | command                                       |
|---------|------------|-----------------------------------------------|
| web     | unittests  | `docker exec -it quiz-web-1 npm run test`     |
| web     | coverage   | `docker exec -it quiz-web-1 npm run coverage` |
| backend | unittest   | `docker exec -it quiz-backend-1 pytest`       |
| cypress | end to end | `docker run quiz-cypress-1`                   |

## Cypress

Configuration of Cypress within docker to open browser on the host machine is very tricky and requires each user to
install local dependencies to make sure that the machine is running as `X server`.
For this reason suggested approach would be to install cypress locally and run it there.

### Local cypress setup

1. `cd web`
2. `npx cypress install`
3. `npx cypress open`

## Helpful commands

| command                                       | description                          |
|-----------------------------------------------|--------------------------------------|
| `docker exec -it quiz-web-1 /bin/bash`        | Open terminal within web container   |
| `docker exec -it quiz-web-1 npm run lint`     | Run prettier to fix errors           |
| `docker exec -it quiz-web-1 npm run eslint`   | Run eslint in the project            |
| `docker exec -it quiz-web-1 npm run tsc`      | Open terminal within backend service |
| `docker exec -it quiz-web-1 npm run watch`    | Run start test runner in watch mode  |
| `docker exec -it quiz-web-1 npm run coverage` | Run tests with coverage report       |
