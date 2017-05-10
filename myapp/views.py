from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapp.models import Route
from myapp.serializers import RouteSerializer


def index(request):
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def routes_route(request):
    return master_route(request, 'routes', Route, RouteSerializer)


def master_route(request, tableName, Table, TableSerializer):
    try:
        tables = Table.objects.all()
    except Table.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        print("getting")
        return Response({tableName: TableSerializer(tables, many=True).data})

    if request.method == 'POST':
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
