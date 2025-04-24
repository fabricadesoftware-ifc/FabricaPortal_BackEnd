FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pdm && \
    pdm config python.use_venv false

COPY pyproject.toml pdm.lock* /app/
COPY README.md /app/

RUN pdm install

COPY . /app/

EXPOSE 8000

CMD ["pdm", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
