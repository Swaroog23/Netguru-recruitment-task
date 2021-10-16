# Netguru-recruitment-task
## Task for recruitment at Netguru


### Used packages:
__Django-rest-framework__: For building API, mainly for ability to use serializers </br>

__requests__: For fetching data from seperate api, mainly for checking if POST values for cars are valid</br>

__pytest, pytest-django__: Unit testing</br>

__jsonschema__: To further check if response returned wanted values during testing</br>

__whitenoise__: collecting and serving static files for development server</br>

__python-decouple__: Used for importing data from .env files</br>

App is dockerized using docker-compose



###  Development setup:
.env:

```
DEBUG=1
SECRET_KEY={{django-app secret key}}
ALLOWED_HOSTS={{Allowed hosts}}
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

### JSON request
Endpoints accept these arguments over request:
#### POST:
- __/cars/__ : "model" - model of the car, string; "make" - manufacturer of the car, string; Validity of maker and model of cars is taken from this API: https://vpic.nhtsa.dot.gov/api/

- __/rate/__: "car_id" - id of the car in the database, int; "rating" - value from 1 to 5, int;

#### DELETE:
- __/cars/:id__ : "id" - id of a car in db to delete, int;

The two __GET__ requests are:
 - __/cars/__ - returns all cars with their ratings
 - __/popular/__ - returns all cars based on their popularit, from the highest to lowest rating

Example of the /cars/ GET response:
```
{

  "id" : 1,

  "make" : "Volkswagen",

  "model" : "Golf",

  "avg_rating" : 5.0,

}
```
### Heroku:
This api is avaiable over Heroku under this link: https://api-netguru-task.herokuapp.com/
