# Setup new project

1. Update `name` in `package.json`
2. Update `<title>...</title>` in `index.html`

# Start container
1. Get docker
2. Copy `envs/web.default.env` to `envs/web.env`.
3. Copy `envs/cypress.default.env` to `envs/cypress.env`.
4. Start containers `docker compose up --build`.
5. __*(OPTIONAL)*__ Copy node dependencies `docker compose cp web:/app/node_modules ./` *(may require sudo)*.

# Production
1. Copy `envs/web.default.env` to `envs/web.env` and fill environmental variables.
2. Start services `docker compose -f docker-compose.prod.yaml up --build`.

# What's in the box

Template contains dockerized setup of

- Vite React TS with SWC
- vitest, testing-library, MSW, faker, happy-dom
- eslint and prettier
- MaterialUI and TailwindCSS
- Cypress
- Formik and yup
- axios and react-query, with interceptor for token refresh
- react-router with simple guards

# Notes

- You'll probably want to lift `envs` up a single folder up the tree.
- You'll want to merge compose files.
- Cypress is dockerized only in headless version, to use UI for writing tests please install node locally (version
  18.12).

# Useful commands

| command                                            | description                          |
|----------------------------------------------------|--------------------------------------|
| `docker compose run --rm -it web /bin/bash`        | Open terminal within web container   |
| `docker compose run --rm -it web npm run lint`     | Run prettier to fix errors           |
| `docker compose run --rm -it web npm run eslint`   | Run eslint in the project            |
| `docker compose run --rm -it web npm run tsc`      | Open terminal within backend service |
| `docker compose run --rm -it web npm run watch`    | Run start test runner in watch mode  |
| `docker compose run --rm -it web npm run coverage` | Run tests with coverage report       |