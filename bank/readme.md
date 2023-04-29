# Start Storybook

1. Get docker
2. Copy `envs/web.default.env` to `envs/web.env`.
3. Start containers `docker compose up --build`.
4. **_(OPTIONAL)_** Copy node dependencies `docker compose cp web:/app/node_modules ./` _(may require sudo)_.

# Some guidelines

1. All imports should be absolute, `import Button from "@azeno/bank/components/Button"` instead
   of `import Button from "../../../components/Button"`.
2. Don't use `@ts-ignore` most of ts config is there for a reason.

# Useful commands

| command                                          | description                          |
| ------------------------------------------------ | ------------------------------------ |
| `docker compose run --rm -it web /bin/bash`      | Open terminal within web container   |
| `docker compose run --rm -it web npm run lint`   | Run prettier to fix errors           |
| `docker compose run --rm -it web npm run eslint` | Run eslint in the project            |
| `docker compose run --rm -it web npm run tsc`    | Open terminal within backend service |
