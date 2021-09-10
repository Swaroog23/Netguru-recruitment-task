from task_api.models import Car, CarRating
import pytest


@pytest.fixture
def create_objects():
    car1 = Car.objects.create(make="HONDA", model="Civic")
    car2 = Car.objects.create(make="HONDA", model="CR-V")
    car3 = Car.objects.create(make="HONDA", model="Accord")
    CarRating.objects.create(car_id=car1.id, rating=3)
    CarRating.objects.create(car_id=car2.id, rating=3)
    CarRating.objects.create(car_id=car3.id, rating=3)