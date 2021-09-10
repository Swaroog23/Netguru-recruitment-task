from rest_framework.views import APIView
from rest_framework.response import Response
from models import Car


class CarViews(APIView):
    def get(self, request):
        return Response(Car.objects.all())
