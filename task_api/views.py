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


class CarViews(APIView):
    def get(self, request):
        cars = Car.objects.annotate(avg_rating=Avg("rating")).all()
        serialized_cars = CarSerializer(cars.values(), many=True).data
        return Response(serialized_cars)

    def post(self, request):
        if "make" in request.data.keys() and "model" in request.data.keys():
            requested_make = request.data["make"].upper()
            requested_model = request.data["model"]
            models_for_make_response = get_models_for_make(requested_make)
            for model in models_for_make_response["Results"]:
                if model["Model_Name"] == requested_model:
                    saved_object = Car.objects.get_or_create(
                        make=requested_model, model=model["Model_Name"]
                    )
                    return Response(CarSerializer(saved_object).data)
                else:
                    raise NotFound(detail="Model does not exists")
        raise ParseError(detail="Wrong body data provided")
