from django.contrib import admin

from .models import Customer, Product, Supplier, Warehouse

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Warehouse)
