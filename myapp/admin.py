from django.contrib import admin

from myapp.models import BusCompany, Customer, Route, Order, Bus, Location

admin.site.register(BusCompany)
admin.site.register(Bus)
admin.site.register(Location)
admin.site.register(Customer)
admin.site.register(Route)
admin.site.register(Order)
