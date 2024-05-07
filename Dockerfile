FROM python:3.10.14-bullseye
ENV PYTHONBUFFERED 1

WORKDIR /app
COPY . /app
ENV DOTENV_PATH="/app/.env"
# attempt to build image magick from source
# RUN cd && \
#       sudo apt update
#       sudo apt install -y build-essential checkinstall \
#       libx11-dev libxext-dev zlib1g-dev libpng-dev \
#       libjpeg-dev libfreetype6-dev libxml2-dev \
#       libtiff-dev liblcms2-dev libwebp-dev libopenexr-dev \
#       libraw-dev libheif-dev libde265-dev && \
#       wget https://download.imagemagick.org/ImageMagick/download/ImageMagick.tar.gz \
#       tar xvzf ImageMagick.tar.gz
#       cd ImageMagick-7.*
#       ./configure
#       make
#       sudo make install
#       sudo ldconfig /usr/local/lib



RUN apt-get update && \
      apt-get -y install sudo && \
      apt-get install -y libyaml-dev && \
      apt-get install -y vim && \
      apt install imagemagick -y
RUN pip install -r /app/requirements.txt

# ENTRYPOINT ["python", "src/main.py"]
ENTRYPOINT ["/bin/bash"]

