FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY quiz-venv/pyproject.toml quiz-venv/poetry.lock ./

RUN pip install -U poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
