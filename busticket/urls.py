from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/routes', views.routes_route, name='routes_route'),
    url(r'^api/v1/orders', views.orders_route, name='orders_route'),
    url(r'^api/v1/customers', views.customers_route, name='customers_route'),
    url(r'^api/v1/buses', views.buses_route, name='buses_route'),
    url(r'^api/v1/bus_companys', views.bus_companys_route, name='bus_companys_route'),
]
