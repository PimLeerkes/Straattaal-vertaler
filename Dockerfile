FROM tiangolo/uvicorn-gunicorn:python3.8-slim

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY ./app /app
COPY ./data /data

WORKDIR /app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
