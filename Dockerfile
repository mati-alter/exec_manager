FROM python:3.13-slim as base

WORKDIR /app

# Crear usuario no-root
RUN groupadd -r python && useradd -r -g python python

# base
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    chown -R python:python .

# Stage dev
FROM base as dev
EXPOSE 8000
USER python
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Stage prod
FROM base as prod
COPY . .
RUN chown -R python:python .
EXPOSE 8000
USER python
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]