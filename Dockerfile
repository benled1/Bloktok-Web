FROM python:3.10.14-bullseye
ENV PYTHONBUFFERED 1

WORKDIR /app
COPY . /app
ENV DOTENV_PATH="/app/.env"

EXPOSE 8000

RUN apt-get update && \
      apt-get -y install sudo && \
      apt-get install -y libyaml-dev && \
      apt-get install -y vim && \
      sudo apt install imagemagick -y
RUN cat ./policy.xml > /etc/ImageMagick-6/policy.xml
ENV DISPLAY=
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

