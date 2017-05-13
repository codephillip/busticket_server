from django.db import models
from django.utils.encoding import smart_str


class BusCompany(models.Model):
    name = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=400)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=400)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=400)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Bus(models.Model):
    number_plate = models.CharField(max_length=8)
    bus_company = models.ForeignKey(BusCompany)
    seats = models.IntegerField()
    model = models.CharField(max_length=400)

    def __str__(self):
        return self.number_plate


class Location(models.Model):
    name = models.CharField(max_length=400)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Route(models.Model):
    code = models.IntegerField(unique=True)
    source = models.CharField(max_length=400)
    destination = models.CharField(max_length=400)
    bus = models.ForeignKey(Bus)
    price = models.IntegerField()
    arrival = models.TimeField()
    departure = models.TimeField()

    def __str__(self):
        return smart_str(self.code)


class Order(models.Model):
    code = models.IntegerField(null=True, unique=True)
    valid = models.BooleanField()
    date = models.CharField(max_length=400, null=True)
    customer = models.ForeignKey(Customer)
    route = models.ForeignKey(Route)

    def __str__(self):
        return smart_str(self.code)
