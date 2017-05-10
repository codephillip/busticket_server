from django.db import models
from django.utils.encoding import smart_str


class BusCompany(models.Model):
    name = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    phone = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    location = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    phone = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    location = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Route(models.Model):
    code = models.IntegerField()
    source = models.CharField(max_length=400)
    destination = models.CharField(max_length=400)
    price = models.IntegerField()
    arrival = models.TimeField()
    departure = models.TimeField()

    def __str__(self):
        return smart_str(self.code)


class Order(models.Model):
    code = models.IntegerField()
    valid = models.IntegerField()
    date = models.DateField(auto_created=True)
    customer = models.ForeignKey(Customer)
    route = models.ForeignKey(Route)

    def __str__(self):
        return smart_str(self.code)

