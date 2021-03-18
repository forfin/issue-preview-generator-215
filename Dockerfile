FROM python:3.7-buster as base-image

RUN apt-get update && \
  apt-get install -y zlib1g-dev libjpeg-dev python3-pythonmagick inkscape xvfb poppler-utils \
  libfile-mimeinfo-perl qpdf libimage-exiftool-perl ufraw-batch ffmpeg \
  scribus libreoffice \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /home/app

COPY requirements.txt /home/app
RUN pip install -r requirements.txt

COPY src /home/app
