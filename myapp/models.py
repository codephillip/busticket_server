from django.core.validators import RegexValidator
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
    created_at = models.DateTimeField(auto_now_add=True)

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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bus(models.Model):
    number_plate = models.CharField(max_length=8)
    bus_company = models.ForeignKey(BusCompany)
    seats = models.IntegerField()
    model = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return smart_str(self.bus_company.name + ' # ' + self.number_plate)


class Location(models.Model):
    name = models.CharField(max_length=400, unique=True)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    code = models.IntegerField(unique=True)
    source = models.ForeignKey(Location, related_name='source')
    destination = models.ForeignKey(Location, related_name='destination')
    bus = models.ForeignKey(Bus)
    price = models.IntegerField()
    arrival = models.TimeField()
    departure = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return smart_str(self.code)


class Order(models.Model):
    code = models.IntegerField()
    valid = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer)
    route = models.ForeignKey(Route)
    phone = models.CharField(max_length=12, blank=True, null=True, validators=[
        RegexValidator(
            regex='^(256|254|255)[0-9]{9}$',
            message='Wrong phone number format',
        ),
    ])

    def __str__(self):
        return smart_str(self.code)


class Feedback(models.Model):
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length=400)

    def __str__(self):
        return smart_str(self.created_at)