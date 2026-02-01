FROM astral/uv:python3.11-alpine

WORKDIR /app

RUN addgroup -S app && adduser -S app -G app
RUN chown -R app:app /app

COPY todo ./todo
COPY pyproject.toml .
COPY uv.lock .
COPY start.py .

RUN uv sync --no-dev

USER app
EXPOSE 5000

ENTRYPOINT ["uv", "run", "--no-sync", "gunicorn", "--bind", "0.0.0.0:5000",  "start:app"]