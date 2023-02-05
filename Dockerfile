FROM python:3.9-slim

COPY ./app /web/app
COPY requirements.txt /web/app

WORKDIR /web

RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r ./app/requirements.txt

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/web_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
