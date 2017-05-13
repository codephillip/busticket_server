from rest_framework import serializers

from myapp.models import Route, Order, BusCompany, Customer, Bus, Location


class OrderSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(required=False, allow_null=True)
    date = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Order
        fields = ('id', 'code', 'valid', 'date', 'customer', 'route')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'longitude', 'latitude')


class BusCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusCompany
        fields = ('id', 'name', 'image', 'phone', 'email', 'address', 'longitude', 'latitude')


class BusSerializer(serializers.ModelSerializer):
    bus_company = BusCompanySerializer()
    
    class Meta:
        model = Bus
        fields = ('id', 'number_plate', 'bus_company', 'seats', 'model')


class RouteSerializer(serializers.ModelSerializer):
    bus = BusSerializer()

    class Meta:
        model = Route
        fields = ('id', 'code', 'source', 'destination', 'bus', 'price', 'arrival', 'departure')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'password', 'email', 'address', 'longitude', 'latitude')
