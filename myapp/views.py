from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from myapp.models import Route, Order, Customer, Bus, BusCompany, Location
from myapp.serializers import RouteSerializer, OrderSerializer, CustomerSerializer, BusSerializer, BusCompanySerializer, LocationSerializer


def index(request):
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def routes_route(request):
    return master_route(request, 'routes', Route, RouteSerializer)


@api_view(['GET', 'POST'])
def locations_route(request):
    return master_route(request, 'locations', Location, LocationSerializer)


@api_view(['GET', 'POST'])
def orders_route(request):
    # make random order code
    # if request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
    return master_route(request, 'orders', Order, OrderSerializer)


@api_view(['GET', 'POST', 'PUT'])
def customers_route(request):
    if request.method == 'PUT':
        error_response = Response({"status": "Failed to login customer"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            print('Request data:')
            print(request.data['phone'])
            print(request.data['password'])
            customers = Customer.objects.filter(phone=request.data['phone'])
            print(customers[0].password)
            if customers is not None and customers[0].password == request.data['password']:
                return Response({"customers": CustomerSerializer(customers, many=True).data},
                                status=status.HTTP_202_ACCEPTED)
            else:
                return error_response
        except Exception:
            return error_response
            # handles user sign-up and get all users
    return master_route(request, 'customers', Customer, CustomerSerializer)


@api_view(['GET', 'POST'])
def buses_route(request):
    return master_route(request, 'buses', Bus, BusSerializer)


@api_view(['GET', 'POST'])
def bus_companys_route(request):
    return master_route(request, 'bus_company', BusCompany, BusCompanySerializer)


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
