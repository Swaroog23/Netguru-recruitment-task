# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /Netguru-recruitment-task
COPY requirements.txt /Netguru-recruitment-task/
RUN pip install -r requirements.txt
COPY . /Netguru-recruitment-task/
