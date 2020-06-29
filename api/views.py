from rest_framework import viewsets
from data_input.models import Manufacturer, Car
from .serializers import ManufacturerSerializer, CarSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('name')
    serializer_class = ManufacturerSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('manufacturer__name')
    serializer_class = CarSerializer
