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


## Run Tests
1. Run `docker compose exec <docker_service_name> pytest` or `docker compose exec <docker_service_name> poetry run pytest`.


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
3. To build the documentation, type: `sphinx-build -b html . _build`.
   - Find the documentation in the docs/_build/html folder.
   - To view the documentation, open the index.html file in a browser.
4. To update the documentation, type: `make html` inside the docs folder.


Example of using sphinx in code:
```python
def add(a: int, b: int) -> int:
    """
    Add two numbers

    :param a: first number
    :param b: second number
    :return: sum of two numbers
    """
    return a + b
```

## Filling environmental variables

### backend.env
```bash
DJ_SECRET_KEY=
#    This is a secret key for Django. It is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
#    To generate a new secret key, run the following command inside django shell:
#    >>> from django.core.management.utils import get_random_secret_key
#    >>> get_random_secret_key()
    
#    Also, you can use this site: https://djecrety.ir/
    
#    e.g:
    DJ_SECRET_KEY="d_lam4k3w^-mj&tve4u3-nnuzqy9jlw^quw=4!rrw6r#55zq(="
    
DJ_DEBUG=
#    A boolean that turns on/off debug mode.
#    If debug is True, Django will use technical error responses when an exception occurs.
#    If debug is False, Django will display a standard page for the given exception, provided by the handler for that exception.
#    
#    e.g:
    DJ_DEBUG=True

DJ_ALLOWED_HOSTS=
#    A list of strings representing the host/domain names that this Django site can serve.
#    This is a security measure to prevent an attacker from poisoning caches and password reset emails with links to malicious hosts by submitting requests with a fake HTTP Host header, which is possible even under many seemingly-safe web server configurations.

#    e.g:
    DJ_ALLOWED_HOSTS = 'localhost 127.0.0.1'
    
    #Hint: Multiple hosts should be separated by a space.
    
LOGGING_LVL=
#    Logging level. 
#    Available options: DEBUG, INFO, ERROR

#    e.g:
    LOGGING_LVL=DEBUG
```
### web.env
```bash
VITE_PORT=
#    The port number that the dev server will listen on.
#    Default port number for vite is 3000.

#    e.g:
    VITE_PORT=3000
```
### postgres.env
```bash
POSTGRES_USER=
#    The user name for the database.

#   e.g:
    POSTGRES_USER=custom_username
    
POSTGRES_PASSWORD=
#    The password for the database.

#   e.g:
    POSTGRES_PASSWORD=strong_password
    
POSTGRES_DB=
#    The name of the database.

#   e.g:
    POSTGRES_DB=fancy_name
    
POSTGRES_HOST=
#    The host name of the database.
#    If you are using docker-compose, you can use the name of the service.

#   e.g:
    POSTGRES_HOST=postgres_service
    
POSTGRES_PORT=
#    The port number of the database.
#    If you are using docker-compose, you can use the port number of the service.
#    Default port number for postgres is 5432.

#   e.g:
    POSTGRES_PORT=5432
```
