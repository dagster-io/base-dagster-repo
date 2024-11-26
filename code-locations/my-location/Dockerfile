FROM python:3.11-slim

WORKDIR /opt/code_location
COPY . /opt/code_location

RUN apt-get update -yqq && \
    apt-get install --no-install-recommends -yqq git

RUN pip install -U uv
RUN pip install uv -e .
