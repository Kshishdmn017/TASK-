FROM python:3.10

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8087

