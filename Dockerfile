FROM python:3.8
LABEL authors="S.G."

WORKDIR /run
COPY setup.py .
COPY GeoIP/  GeoIP/

RUN pip install .
