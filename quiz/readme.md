# Azeno quiz

## Run Development

1. Copy `envs/web.default.env` to `envs/web.env`.
2. Copy `envs/cypress.default.env` to `envs/cypress.env`.
3. Copy `envs/postgres.default.env` to `envs/postgres.env` and fill environmental variables.
4. Copy `envs/backend.default.env` to `envs/backend.env` and fill environmental variables.
5. Start services `docker compose up --build`.

## Run Production

1. Copy `envs/web.default.env` to `envs/web.env` and fill environmental variables.
2. Copy `envs/postgres.default.env` to `envs/postgres.env` and fill environmental variables.
3. Copy `envs/backend.default.env` to `envs/backend.env` and fill environmental variables.
4. Start services `docker compose -f docker-compose.prod.yaml up --build`.

## Testing

| service | type       | command                                            |
|---------|------------|----------------------------------------------------|
| web     | unittests  | `docker compose run --rm -it web npm run test`     |
| web     | coverage   | `docker compose run --rm -it web npm run coverage` |
| backend | unittest   | `docker compose run --rm -it backend pytest`       |
| cypress | end to end | `docker compose run --rm -it cypress`              |

## Cypress

Configuration of Cypress within docker to open browser on the host machine is very tricky and requires each user to
install local dependencies to make sure that the machine is running as `X server`.
For this reason suggested approach would be to install cypress locally and run it there.

### Local cypress setup

1. `cd web`
2. `npx cypress install`
3. `npx cypress open`

## Helpful commands

| command                                            | description                          |
|----------------------------------------------------|--------------------------------------|
| `docker compose run --rm -it web /bin/bash`        | Open terminal within web container   |
| `docker compose run --rm -it web npm run lint`     | Run prettier to fix errors           |
| `docker compose run --rm -it web npm run eslint`   | Run eslint in the project            |
| `docker compose run --rm -it web npm run tsc`      | Open terminal within backend service |
| `docker compose run --rm -it web npm run watch`    | Run start test runner in watch mode  |
| `docker compose run --rm -it web npm run coverage` | Run tests with coverage report       |

### backend.env

> #### Variables used for Django superuser migration
> 
> - Here you have some example data:
> - **DJ_SU_NAME=** lordOfDarkness 
> - **DJ_SU_EMAIL=** lordofdarkness@gmail.com
> - **DJ_SU_PASSWORD=** strongPassword123
>
> #### Json Web Token veryfying key
> - **JWT_SECRET_KEY=**
> 
>Json Web Token secret key is used for encrypting tokens.
>``` E.g. JWT_SECRET_KEY=7j523!hiq1@=m!(v88x8!py17qzf7r40%9cy*=_-c7hdy3xb9t```
>To make your life easier in development use this [secret key generator](https://djecrety.ir/).
> 
>If you are a backend developer, don't be a savage and generate your key with a django built-in function in your terminal.
> 
>```python
>from django.core.management.utils import get_random_secret_key
>
>get_random_secret_key()
>```
>
> #### CORS_ALLOWED_ORIGINS=
> 
>Add origins that are allowed to make cross-site HTTP requests. *Make sure that origins are SPACE-SEPARATED, not comma-separated*
> 
> For development, you can set this variable to:
>
><span style="color:green">RIGHT:</span>
>"http://localhost:frontend_port http://localhost:backend_port"
>
><span style="color:red">WRONG:</span>
>"http://localhost:frontend_port<span style="color:red">,</span> http://localhost:backend_port">
 
------

## How to run black code formatter

1. Install the Black extension in your IDE.
2. Configure Black to use configuration file form `pyproject.toml`.
3. Use hotkey to format code.

### Alternative way to run black formatter: 
 
- Run the Black formatter by using the following command for all files:
    > docker compose exec <service_name> black .

- To check only one file, run the following command:
    > docker compose exec <service_name> black <file_name>
  
## How to use mypy type checker
1. Run the mypy type checker by using the following command for all files:
    > docker compose exec <service_name> mypy .
   > 

## Test data generator
1. To add some test data to database run:
    > docker compose exec <backend_service_name> python manage.py create_test_data

2. To remove test data from database run:
    > docker compose exec <backend_service_name> python manage.py delete_test_data
