# Netguru-recruitment-task
Task for recruitment at Netguru


Used packages:
Django-rest-framework: For building API, mainly for their serializers
requests: For fetching data from seperate page
pytest: Unit testing
jsonschema: To further check if response was ok during testing
whitenoise, gunicorn: Deployment to heroku

App is dekcerized using docker-compose

Setup:
docker-compose up should set up two containers: one with django app and second one with postgreSql database
In container with django app, command "python manage.py makemigrations" and "python manage.py migrate" should get the database up and running  

Used database: PostgreSql
