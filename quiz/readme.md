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

logger = logging.getLogger('<logger_name>')

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
