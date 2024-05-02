FROM python:3.10.14-bullseye

WORKDIR /app
COPY . /app
RUN apt-get update && \
      apt-get -y install sudo
RUN sudo chmod +x entrypoint.sh
CMD ["/app/entrypoint.sh"]
