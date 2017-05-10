from rest_framework import serializers

from myapp.models import Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'code', 'source', 'destination', 'price', 'arrival', 'departure')

