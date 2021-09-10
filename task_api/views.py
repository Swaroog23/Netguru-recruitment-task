from task_api.validators import (
    validate_list_of_models_exists,
    validate_post_rate_request_data,
    validate_post_car_request_data,
)
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Avg, Count
from task_api.serializers import (
    CarRatingSerializer,
    CarSerializerWithAvgRating,
    CarSerializerWithRatingCount,
)
from task_api.services import get_models_for_make
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import ParseError
from .models import Car
from django.db import IntegrityError
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view


class CarViews(APIView):
    def get(self, request):
        cars = Car.objects.annotate(avg_rating=Avg("rating")).all()
        serialized_cars_with_avg_rating = CarSerializerWithAvgRating(
            cars.values(), many=True
        ).data
        return Response(data=serialized_cars_with_avg_rating, status=200)

    def post(self, request):
        validate_post_car_request_data(request.data)
        models_for_make_response = get_models_for_make(request.data["make"])
        validate_list_of_models_exists(models_for_make_response)
        for model in models_for_make_response["Results"]:
            if request.data["model"].upper() == model["Model_Name"].upper():
                try:
                    Car.objects.create(
                        make=model["Make_Name"], model=model["Model_Name"]
                    )
                    return Response(data="Car created", status=201)
                except IntegrityError:
                    raise ParseError(
                        detail="Object with given name already exists", code=400
                    )
        raise NotFound(detail="Model does not exists")


@api_view(["DELETE"])
def delete_car_view(request, id):
    try:
        car_to_delete = Car.objects.get(id=id)
        car_to_delete.delete()
        return Response(data="Car deleted", status=200)
    except ObjectDoesNotExist:
        raise NotFound(detail="Model does not exists")


@api_view(["POST"])
def post_car_rating_view(request):
    validate_post_rate_request_data(request.data)
    serialized_car_rating = CarRatingSerializer(
        data={
            "rating": request.data["rating"],
            "car": request.data["car_id"],
        }
    )
    if serialized_car_rating.is_valid():
        try:
            serialized_car_rating.save()
            return Response(data="Rating added", status=201)
        except IntegrityError:
            raise NotFound(detail="Car model does not exists")


@api_view(["GET"])
def get_cars_by_popularity(request):
    ordered_cars_by_rating = Car.objects.order_by("rating").annotate(
        rates_number=Count("rating")
    )
    ordered_serialized_cars_by_rating = CarSerializerWithRatingCount(
        ordered_cars_by_rating, many=True
    ).data
    return Response(data=ordered_serialized_cars_by_rating, status=200)
