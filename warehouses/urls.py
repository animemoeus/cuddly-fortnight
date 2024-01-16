from django.urls import path

from . import views
from .views import CustomerListView

urlpatterns = [
    path("", views.index),
    path("customers", CustomerListView.as_view(), name="customers"),
]

app_name = "warehouses"
