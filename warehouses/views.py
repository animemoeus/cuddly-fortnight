from django.shortcuts import render
from django.views.generic import ListView

from .models import Customer, Product, Supplier, Warehouse


def index(request):
    return render(request, "warehouses/index.html")


class CustomerListView(ListView):
    model = Customer
    template_name = "warehouses/customer-list.html"
    ordering = ["-id"]


class ProductListView(ListView):
    model = Product
    template_name = "warehouses/product-list.html"
    ordering = ["-id"]


class SupplierListView(ListView):
    model = Supplier
    template_name = "warehouses/supplier-list.html"
    ordering = ["-id"]


class WarehouseListView(ListView):
    model = Warehouse
    template_name = "warehouses/warehouse-list.html"
    ordering = ["-id"]
