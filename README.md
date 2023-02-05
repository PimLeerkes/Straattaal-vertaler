# Straattaal vertaler

Een vertaler gemaakt door Mensen die graag normaal nederlands maar ook straattaal willen spreken.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
	- [Run](#Run)
	- [Use](#Use)
- [Configuration](#Configuration)
- [Built With](#built-with)

## Getting Started

Met deze instructies kun je deze straattaal vertaler beginnen en gebruiken.

### Prerequisites

- Python3
- Docker

### Installation

Get the code:
``` shell
# Clone the repo
git clone https://github.com/PimLeerkes/Straattaal-vertaler.git
# change directory
cd Straattaal-vertaler
```

#### Python:
Set up virtual environment:
``` shell
# Create virtual environment
python3 -m venv env
# Activate the environment
source env/bin/activate
# Install requirements
pip install -r requirements.txt
```

#### Docker
Build docker container:
```shell
docker build -t straatvertaler/web_app .
```

You can also get up and running without cloning this repository directly to your machine.

Create and add this to the  `Dockerfile` :
``` Dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/PimLeerkes/Straattaal-vertaler.git .

RUN pip3 install -r requirements.txt

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/web_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

After that build the container.

## Usage

### Run
With python:
```shell
streamlit run app/web_app.py 
```

With docker:
``` shell
docker run -d --name straatvertaler -p 8080:8080 straatvertaler/web_app
```

### Use
1. Open up your webbrowser at `localhost:8080`.
2. Type what you want translated
3. Copy the text you want to use
4. Done!

## Configuration
If you want to use it for your server you can definitely do that. Here are some examples:
`Dockerfile`:
``` Dockerfile
# Set server port to 80 or 443
ENTRYPOINT ["streamlit", "run", "app/web_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

`.streamlit/config.tom`:
```toml
# Set server port to 80 or 443
[server]
port = 8080
```

Also, streamlit has a community cloud where you can host it [here](https://streamlit.io/cloud)

## Build With
Libraries:
- [Streamlit](https://streamlit.io/) 


