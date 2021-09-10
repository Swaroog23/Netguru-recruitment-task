from task_api.conftest import create_objects
from django.test import Client
from task_api.models import Car, CarRating
from jsonschema import validate
from task_api.response_schemas import car_view_schema, popular_view_schema
import json
import pytest


@pytest.mark.django_db
def test_get_cars_view(client: Client, create_objects: create_objects):
    response = client.get("/cars/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    response_body = response.json()
    validate(instance=response_body, schema=car_view_schema)


@pytest.mark.django_db
def test_get_popular_view(client: Client, create_objects: create_objects):
    response = client.get("/popular/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    response_body = response.json()
    validate(instance=response_body, schema=popular_view_schema)


@pytest.mark.django_db
def test_post_cars_view(client: Client):
    response = client.post(
        "/cars/",
        data=json.dumps({"make": "Honda", "model": "Civic"}),
        content_type="application/json;charset=UTF-8",
    )
    assert response.status_code == 201
    assert Car.objects.count() == 1
    car = Car.objects.get(model="Civic")
    assert car.make == "HONDA"
    assert car.model == "Civic"


@pytest.mark.django_db
def test_post_car_rating_view(client: Client):
    car = Car.objects.create(make="HONDA", model="Civic")
    response = client.post(
        "/rate/",
        data=json.dumps({"car_id": car.id, "rating": 4}),
        content_type="application/json;charset=UTF-8",
    )
    assert response.status_code == 201
    assert CarRating.objects.count() == 1
    rate = CarRating.objects.get(car_id=car.id)
    assert rate.car_id == car.id
    assert rate.rating == 4


@pytest.mark.django_db
def test_delete_car_view(client: Client):
    car = Car.objects.create(make="HONDA", model="Civic")
    assert Car.objects.count() == 1
    response = client.delete(f"/cars/{car.id}")
    assert response.status_code == 200
    assert Car.objects.count() == 0
