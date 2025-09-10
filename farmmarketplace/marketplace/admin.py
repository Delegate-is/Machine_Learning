from django.contrib import admin
from .models import Vendor, Product, Order, Sale

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Sale)