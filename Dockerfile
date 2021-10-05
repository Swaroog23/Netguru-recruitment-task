# syntax=docker/dockerfile:1
FROM python:3.9.7
ENV PYTHONUNBUFFERED=1
WORKDIR /Netguru-recruitment-task
COPY . /Netguru-recruitment-task/
RUN ls .
RUN pip install -r requirements.txt
CMD python manage.py makemigrations && python manage.py migrate && python manage.py seed && python manage.py runserver 0.0.0.0:$PORT