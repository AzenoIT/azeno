# Start Storybook
1. Get docker
2. Copy `envs/web.default.env` to `envs/web.env`.
3. Start containers `docker compose up --build`.
4. __*(OPTIONAL)*__ Copy node dependencies `docker compose cp web:/app/node_modules ./` *(may require sudo)*.

# Useful commands

| command                                            | description                          |
|----------------------------------------------------|--------------------------------------|
| `docker compose run --rm -it web /bin/bash`        | Open terminal within web container   |
| `docker compose run --rm -it web npm run lint`     | Run prettier to fix errors           |
| `docker compose run --rm -it web npm run eslint`   | Run eslint in the project            |
| `docker compose run --rm -it web npm run tsc`      | Open terminal within backend service |
| `docker compose run --rm -it web npm run watch`    | Run start test runner in watch mode  |
| `docker compose run --rm -it web npm run coverage` | Run tests with coverage report       |
