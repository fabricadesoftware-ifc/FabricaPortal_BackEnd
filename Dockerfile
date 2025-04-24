FROM python:3.13

ENV PYTHONUNBUFFERED=1

COPY . /app/

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pdm

RUN pdm install

RUN pdm migrate

EXPOSE 8000

CMD ["pdm", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
