FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Instala pdm
RUN pip install pdm

# Copia tudo antes de instalar para garantir que README.md e o projeto estejam no lugar
COPY . /app

# Exporta as dependências do pdm e instala com pip
RUN pdm export -o requirements.txt --without-hashes && pip install -r requirements.txt

# Instala o projeto como pacote editável
RUN pdm install

RUN pdm makemigrations
RUN pdm migrate

EXPOSE 8000

CMD ["pdm", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
