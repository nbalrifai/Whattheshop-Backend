from django.contrib import admin
from .models import CoffeeBean, Order, OrderItem

admin.site.register(CoffeeBean),
admin.site.register(Order),
admin.site.register(OrderItem)
