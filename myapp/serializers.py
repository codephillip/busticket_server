from rest_framework import serializers

from myapp.models import Route, Order, BusCompany, Customer, Bus, Location, Feedback
import random


def generate_random_int():
    random_int = random.randint(100000, 999999)
    orders = Order.objects.filter(code=random_int)
    if orders is not None:
        return random.randint(100000, 999999)
    else:
        return random_int


class OrderSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Order
        fields = ('id', 'code', 'valid', 'created_at', 'customer', 'route')

    def validate(self, attrs):
        attrs['code'] = generate_random_int()
        return attrs


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'longitude', 'latitude', 'created_at')


class BusCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusCompany
        fields = ('id', 'name', 'image', 'phone', 'email', 'address', 'longitude', 'latitude', 'created_at')


class BusSerializer(serializers.ModelSerializer):
    bus_company = BusCompanySerializer()
    
    class Meta:
        model = Bus
        fields = ('id', 'number_plate', 'bus_company', 'seats', 'model', 'created_at')


class RouteSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)
    source = LocationSerializer(read_only=True)
    destination = LocationSerializer(read_only=True)

    class Meta:
        model = Route
        fields = ('id', 'code', 'source', 'destination', 'bus', 'price', 'arrival', 'departure', 'created_at')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'password', 'email', 'address', 'longitude', 'latitude', 'created_at')


class OrderGetSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    route = RouteSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'code', 'valid', 'created_at', 'customer', 'route')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'code', 'created_at', 'content', 'title')