# Netguru-recruitment-task
##Task for recruitment at Netguru


###Used packages:
Django-rest-framework: For building API, mainly for their serializers </br>

requests: For fetching data from seperate page</br>

pytest: Unit testing</br>

jsonschema: To further check if response was ok during testing</br>

whitenoise, gunicorn: Deployment to heroku</br>

App is dekcerized using docker-compose

###Setup:
docker-compose up should set up two containers: one with django app and second one with postgreSql database
In container with django app, command "python manage.py makemigrations" and "python manage.py migrate" should get the database up and running  

###Used database: PostgreSql
