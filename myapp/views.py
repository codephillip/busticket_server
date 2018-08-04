import random

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from myapp.models import Route, Order, Customer, Bus, BusCompany, Location, Feedback
from myapp.serializers import RouteSerializer, OrderSerializer, CustomerSerializer, BusSerializer, BusCompanySerializer, \
    LocationSerializer, FeedbackSerializer, OrderGetSerializer


def index(request):
    return render(request, 'index.html')


class RouteView(ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class LocationView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderSerializer
        else:
            return OrderGetSerializer


class CustomerOrdersView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderSerializer
        else:
            return OrderGetSerializer

    def get_queryset(self):
        orders = Order.objects.filter(customer_id=self.kwargs['pk'])
        return orders


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


class BusView(ListCreateAPIView):
    """
    Returns all buses
    Allows User to create bus
    """
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusCompanyView(ListCreateAPIView):
    """
    Returns all bus companies
    Allows User to create bus company
    """
    queryset = BusCompany.objects.all()
    serializer_class = BusCompanySerializer


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


class FeedbackView(ListCreateAPIView):
    """
    Returns all feedbacks in the System
    Allows User to provide feedback
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer