from django.conf.urls import url
from django.contrib import admin

from myapp import views
from myapp.views import FeedbackView, BusCompanyView, BusView, OrderView, LocationView, RouteView, CustomerOrdersView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/routes$', RouteView.as_view(), name='routes'),
    url(r'^api/v1/locations$', LocationView.as_view(), name='locations'),
    url(r'^api/v1/orders$', OrderView.as_view(), name='orders'),
    url(r'^api/v1/customers$', views.customers_route, name='customers'),
    url(r'^api/v1/customers/(?P<pk>[-\w]+)/orders$', CustomerOrdersView.as_view(), name='customers_orders'),
    url(r'^api/v1/buses$', BusView.as_view(), name='buses'),
    url(r'^api/v1/bus_companys$', BusCompanyView.as_view(), name='bus_companys'),
    url(r'^api/v1/feedbacks$', FeedbackView.as_view(), name='feedback'),
]
