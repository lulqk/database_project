from django.shortcuts import render, redirect
from .models import Manufacturer, Car
from .forms import ManufacturerForm, CarForm
from .mongo import insert_car, get_cars


def index(request):
    cars = Car.objects.all()
    car_form = CarForm()
    man_form = ManufacturerForm()
    mongo_cars = get_cars()

    if request.method == 'POST':
        man_form = ManufacturerForm(request.POST)
        if man_form.is_valid():
            man_form.save()
            return redirect('data_input:index')
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            return redirect('data_input:index')

    context = {
        'cars': cars,
        'car_form': car_form,
        'man_form': man_form,
        'mongo_cars': mongo_cars
    }

    return render(request, 'data_input/index.html', context)


def export_to_mongo(request, id):
    car = Car.objects.get(id=id)
    insert_car(car)
    return redirect('data_input:index')
