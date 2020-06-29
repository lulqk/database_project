import pymongo
import os
from .models import Manufacturer, Car
from api.serializers import CarSerializer

client = pymongo.MongoClient('mongo', 27017,
                             username=os.environ.get("MONGO_USERNAME"),
                             password=os.environ.get("MONGO_PASSWORD"))
db = client.cars_database
collection = db.cars_collection

def insert_car(car):
    data = CarSerializer(instance=car).data
    manufacturer = Manufacturer.objects.get(id=car.manufacturer_id)
    data['manufacturer'] = manufacturer.name
    collection.update_one(data, {'$set':data}, upsert=True)


def get_cars():
    cars = collection.find()
    return cars
