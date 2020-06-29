from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    CHOICES = [
        ('H', 'Hybrid'),
        ('E', 'Electric'),
        ('D', 'Diesel'),
        ('P', 'Petrol'),
    ]
    manufacturer = models.ForeignKey(Manufacturer, related_name='cars', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    engine = models.CharField(max_length=1, choices=CHOICES, default='H')
    displacement = models.PositiveIntegerField(default=0)
    power = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
