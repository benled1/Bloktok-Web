FROM python:3.10.14-bullseye
ENV PYTHONBUFFERED 1

WORKDIR /app
COPY . /app
ENV DOTENV_PATH="/app/.env"
RUN apt-get update && \
      apt-get -y install sudo && \
      apt-get install -y libyaml-dev && \
      apt-get install -y vim
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "src/main.py"]
