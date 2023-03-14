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

### backend.env
```
JWT_SECRET_KEY=7j523!hiq1@=m!(v88x8!py17qzf7r40%9cy*=_-c7hdy3xb9t
Json Web Token secret key is used for encrypting tokens.
```
To make your life easier in development use this [secret key generator](https://djecrety.ir/).
If you are a backend developer, don't be a savage and generate your key with a django built-in function in your terminal.
```python
from django.core.management.utils import get_random_secret_key

get_random_secret_key()
```

```
CORS_ALLOWED_ORIGINS=
Add origins that are alloed to make cross-site HTTP requests. For development you can set this variable to:
It is imortant to set this this strin is that every origin is SPACE SEPARATED
```
<span style="color:green">RIGHT:</span>
"http://localhost:frontend_port http://localhost:backend_port"

<span style="color:red">WRONG:</span>
"http://localhost:frontend_port<span style="color:red">,</span> http://localhost:backend_port"
