from django.core.management.base import BaseCommand
from task_api.models import Car, CarRating
import random
import logging


class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self)
        self.stdout.write("done.")


def create_car_and_car_rating():
    logging.info("Creating cars")
    makes = [
        ["HONDA", "Accord"],
        ["ASTON MARTIN", "DBS"],
        ["TESLA", "Model X"],
        ["JAGUAR", "F-Type"],
    ]

    for make in makes:
        car = Car.objects.create(
            make=make[0],
            model=make[1],
        )
        for _ in range(5):
            CarRating.objects.create(car_id=car.id, rating=random.randint(1, 5))

    logging.info(f"{car} created.")
    return car


def run_seed(self):
    create_car_and_car_rating()