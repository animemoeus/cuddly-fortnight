from django.contrib import admin

from .models import Customer, Product, Supplier, Warehouse


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


class WarehouseAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
