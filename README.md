# Netguru-recruitment-task
## Task for recruitment at Netguru


### Used packages:
__Django-rest-framework__: For building API, mainly for ability to use serializers </br>

__requests__: For fetching data from seperate api, mainly for checking if POST values for cars are valid</br>

__pytest, pytest-django__: Unit testing</br>

__jsonschema__: To further check if response returned wanted values during testing</br>

__whitenoise__: collecting and serving static files for development server</br>

App is dockerized using docker-compose



###  Development setup:
.env:

```
DEBUG=1
DB_ENGINE=django.db.backends.postgresql
DB_TYPE=postgres
DB_DATABASE_NAME={{db name}}
DB_USERNAME={{db user}}
DB_PASSWORD={{db password}}
DB_HOST=db
DB_PORT=5432
PORT=8000
```

.env-db:

``` 
POSTGRES_DB={{same as DB_DATABASE_NAME}}
POSTGRES_USER={{same as DB_USERNAME}}
POSTGRES_PASSWORD={{same as DB_PASSWORD}}
```

``docker-compose -f docker-compose.development.yml up --build`` </br></br>
This command runs development version of docker-compose, building api and a postgres db containers with migrations and seeds.


### Used database: PostgreSql
You should provide username, password and db name to .env files for app to work properly
