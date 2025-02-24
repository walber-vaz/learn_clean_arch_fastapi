FROM python:3.13.2-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app/

RUN pip install -U pip setuptools wheel
RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config installer.max-workers 10
RUN poetry install --no-root --no-dev --no-interaction --no-ansi

ENV PATH="/app/.venv/bin:$PATH"

COPY ./alembic.ini /app/
COPY ./migrations /app/migrations
COPY ./app /app/app

RUN poetry install --no-dev --no-interaction --no-ansi

RUN addgroup --gid 1001 --system sfuser && \
  adduser --gid 1001 --shell /bin/false --disabled-password --uid 1001 sfuser

RUN chown -R sfuser:sfuser /app/

EXPOSE 8000

CMD runuser -u sfuser -- gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app \
  --bind 0.0.0.0:8000 --forwarded-allow-ips="*" --timeout=120
