# Azeno quiz

## Run Development

1. Copy `envs/web.default.env` to `envs/web.env`.
2. Copy `envs/cypress.default.env` to `envs/cypress.env`.
3. Copy `envs/postgres.default.env` to `envs/postgres.env` and fill environmental variables.
4. Copy `envs/backend.default.env` to `envs/backend.env` and fill environmental variables.
5. Start containers `docker compose up --build`.
6. __*(OPTIONAL)*__ Copy node dependencies `docker compose cp web:/project/node_modules ./` *(may require sudo)* *(
   command should be run from repository root)*

## Run Production

1. Copy `envs/web.default.env` to `envs/web.env` and fill environmental variables.
2. Copy `envs/postgres.default.env` to `envs/postgres.env` and fill environmental variables.
3. Copy `envs/backend.default.env` to `envs/backend.env` and fill environmental variables.
4. Start services `docker compose -f docker-compose.prod.yaml up --build`.

## Example of using logging

```python
import logging

logger = logging.getLogger('django')

logger.info("Info message")
logger.debug("Debug message")
logger.warning("Warning message")
```

## Building / Updating Documentation

1. Open a shell inside the container: `docker compose exec <docker_service_name> sh`.
2. Navigate to the docs folder: `cd docs`.
3. For building the documentation, type: `sphinx-build -b html . _build`.

Additional information:

- If you add a new Django app, you should run `sphinx-apidoc -o . ..` inside the `docs` folder.
- To update the documentation, type `make html` in the docs folder.
- Docstrings should be written in reStructuredText
  format. [Check out this site for more information.](https://docutils.sourceforge.io/rst.html)
- To view the documentation, open the `docs/_build/index.html` file in a browser.

Example of using reStructuredText format in code:

```python
def add(a: int, b: int) -> int:
    """Add two numbers

    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :returns: sum of two numbers
    :rtype: int
    """

    return a + b
```

## Filling environmental variables

### backend.env

> **DJ_SECRET_KEY=**

This is a secret key for Django. It is used to provide cryptographic signing, and should be set to a unique,
unpredictable value.
To generate a new secret key, run the following command inside django shell:

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

Also, you can use this site: https://djecrety.ir/

e.g:
`DJ_SECRET_KEY="d_lam4k3w^-mj&tve4u3-nnuzqy9jlw^quw=4!rrw6r#55zq(="`

> **DJ_DEBUG=**

An integer that specifies the debug mode.
If 1, Django will use technical error responses when an exception occurs.
If 0, Django will display a standard page for the given exception, provided by the handler for that exception.

e.g:
`DJ_DEBUG=1`

> **DJ_ALLOWED_HOSTS=**

A list of strings representing the host/domain names that this Django site can serve.
This is a security measure to prevent an attacker from poisoning caches and password reset emails with links to
malicious hosts by submitting requests with a fake HTTP Host header, which is possible even under many seemingly-safe
web server configurations.

e.g:
`DJ_ALLOWED_HOSTS = 'localhost 127.0.0.1'`

Hint: Multiple hosts should be separated by a space.

> **LOGGING_LVL=**

Logging level.
Available options: DEBUG, INFO, ERROR

e.g:
`LOGGING_LVL=DEBUG`

> **Variables used for Django superuser migration**

E.g.

DJ_SU_NAME=lordOfDarkness
DJ_SU_EMAIL=lordofdarkness@gmail.com
DJ_SU_PASSWORD=strongPassword123


> **JWT_SECRET_KEY=**

Json Web Token secret key is used for encrypting tokens.
E.g. `JWT_SECRET_KEY="7j523!hiq1@=m!(v88x8!py17qzf7r40%9cy*=_-c7hdy3xb9t"`
To make your life easier in development use this [secret key generator](https://djecrety.ir/).

If you are a backend developer, don't be a savage and generate your key with a django built-in function in your
terminal.

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

> **CORS_ALLOWED_ORIGINS=**

Add origins that are allowed to make cross-site HTTP requests.
*Make sure that origins are SPACE-SEPARATED, not comma-separated*
For development, you can set this variable to:
`CORS_ALLOWED_ORIGINS="http://localhost:frontend_port http://localhost:backend_port"`

### web.env

> **VITE_PORT=**

The port number that the dev server will listen on.
Default port number for vite is 3000.

e.g:
`VITE_PORT=3000`

### postgres.env

> POSTGRES_USER=

The username for the database.
e.g.
`POSTGRES_USER=custom_username`

> POSTGRES_PASSWORD=

The password for the database.
e.g:
`POSTGRES_PASSWORD=strong_password`

> POSTGRES_DB=

The name of the database.

e.g:`POSTGRES_DB=fancy_name`

> POSTGRES_HOST=

The host name of the database.
If you are using docker-compose, you can use the name of the service.

e.g:
`POSTGRES_HOST=postgres_service`

> POSTGRES_PORT=
>
The port number of the database.
If you are using docker-compose, you can use the port number of the service.
Default port number for postgres is 5432.

e.g: `POSTGRES_PORT=5432`

## Testing

| service | type       | command                                                               |
|---------|------------|-----------------------------------------------------------------------|
| web     | unittests  | `docker compose run --rm -it web npm run --prefix quiz/web/ test`     |
| web     | coverage   | `docker compose run --rm -it web npm run --prefix quiz/web/ coverage` |
| backend | unittest   | `docker compose run --rm -it backend pytest`                          |
| cypress | end to end | `docker compose run --rm -it cypress`                                 |

## Cypress

Configuration of Cypress within docker to open browser on the host machine is very tricky and requires each user to
install local dependencies to make sure that the machine is running as `X server`.
For this reason suggested approach would be to install cypress locally and run it there.

### Local cypress setup

1. `cd web`
2. `npx cypress install`
3. `npx cypress open`

## Helpful commands

| command                                                               | description                          |
|-----------------------------------------------------------------------|--------------------------------------|
| `docker compose run --rm -it web /bin/bash`                           | Open terminal within web container   |
| `docker compose run --rm -it --prefix quiz/web/ web npm run lint`     | Run prettier to fix errors           |
| `docker compose run --rm -it --prefix quiz/web/ web npm run eslint`   | Run eslint in the project            |
| `docker compose run --rm -it --prefix quiz/web/ web npm run tsc`      | Open terminal within backend service |
| `docker compose run --rm -it --prefix quiz/web/ web npm run watch`    | Run start test runner in watch mode  |
| `docker compose run --rm -it --prefix quiz/web/ web npm run coverage` | Run tests with coverage report       |

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
   > int_value = how many objects do you want to create
   >
   >`docker compose exec <backend_service_name> python manage.py create_test_data int_value `

2. To remove test data from database run:
   > `docker compose exec <backend_service_name> python manage.py delete_test_data`
