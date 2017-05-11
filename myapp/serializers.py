from rest_framework import serializers

from myapp.models import Route, Order, BusCompany, Customer, Bus


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'code', 'source', 'destination', 'bus', 'price', 'arrival', 'departure')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'code', 'valid', 'date', 'customer', 'route')


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'number_plate', 'bus_company', 'seats', 'model')


class BusCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusCompany
        fields = ('id', 'name', 'image', 'phone', 'email', 'address', 'longitude', 'latitude')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'image', 'phone', 'email', 'address', 'longitude', 'latitude')
