# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /Netguru-recruitment-task
COPY requierments.txt /Netguru-recruitment-task/
RUN pip install -r requierments.txt
COPY . /Netguru-recruitment-task/
