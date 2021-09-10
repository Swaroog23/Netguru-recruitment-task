import json

from django.db.models.aggregates import Avg
from task_api.serializers import CarSerializer
from task_api.services import get_all_makes, get_models_for_make
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import ParseError
from .models import Car
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.decorators import api_view


class CarViews(APIView):
    def get(self, request):
        cars = Car.objects.annotate(avg_rating=Avg("rating")).all()
        serialized_cars = CarSerializer(cars.values(), many=True).data
        return Response(data=serialized_cars, status=200)

    def post(self, request):
        if "make" in request.data.keys() and "model" in request.data.keys():
            requested_make = request.data["make"].upper()
            requested_model = request.data["model"]
            models_for_make_response = get_models_for_make(requested_make)
            for model in models_for_make_response["Results"]:
                if model["Model_Name"] == requested_model:
                    try:
                        Car.objects.get(model=requested_model)
                        raise ParseError(
                            detail="Object with given name already exists", code=400
                        )
                    except ObjectDoesNotExist:
                        Car.objects.create(
                            make=requested_make, model=model["Model_Name"]
                        )
                        return Response(data="Car created", status=201)
                else:
                    raise NotFound(detail="Model does not exists")
        raise ParseError(detail="Wrong body data provided", code=400)


@api_view(["DELETE"])
def delete_car_view(request, id):
    try:
        car_to_delete = Car.objects.get(id=id)
        car_to_delete.delete()
        return Response(data="Car deleted", status=200)
    except ObjectDoesNotExist:
        raise NotFound(detail="Model does not exists")
