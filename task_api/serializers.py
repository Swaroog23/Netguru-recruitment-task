from django.db.models import fields
from task_api.models import Car, CarRating
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField()

    class Meta:
        model = Car
        fields = "__all__"


class CarRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRating
        fields = "__all__"