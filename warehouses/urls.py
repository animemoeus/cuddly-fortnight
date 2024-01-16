from django.urls import path

from . import views
from .views import (
    CustomerListView,
    ProductListView,
    SupplierListView,
    WarehouseListView,
)

urlpatterns = [
    path("", views.index),
    path("customers/", CustomerListView.as_view(), name="customers"),
    path("products/", ProductListView.as_view(), name="products"),
    path("suppliers/", SupplierListView.as_view(), name="suppliers"),
    path("warehouse/", WarehouseListView.as_view(), name="warehouse"),
]

app_name = "warehouses"
