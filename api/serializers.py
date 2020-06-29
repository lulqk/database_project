from data_input.models import Manufacturer, Car
from rest_framework import serializers


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['manufacturer', 'name', 'engine', 'displacement', 'power']
