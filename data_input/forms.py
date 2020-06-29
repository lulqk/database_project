from django.forms import ModelForm
from .models import Manufacturer, Car


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['manufacturer', 'name', 'engine', 'displacement', 'power']
