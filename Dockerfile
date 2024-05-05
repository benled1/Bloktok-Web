FROM python:3.10.14-bullseye
ENV PYTHONBUFFERED 1

WORKDIR /app
COPY . /app

RUN apt-get update && \
      apt-get -y install sudo && \
      apt-get install -y libyaml-dev
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["/bin/bash"]
