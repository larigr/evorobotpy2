FROM python:3.8-slim

RUN apt-get update -q \
  && apt-get install --no-install-recommends -qy \
  gcc \                                    
    inetutils-ping \
  && rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y build-essential

RUN apt-get install -qy libgsl-dev libopenmpi-dev

WORKDIR /usr/app/src

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/local/lib/python3.8/site-packages

RUN rm -r pybullet_envs

COPY config/ /usr/local/lib/python3.8/site-packages/

WORKDIR /usr/app/src
RUN make compile_all



