from django.shortcuts import render
from django.views.generic import ListView

from .models import Customer


def index(request):
    return render(request, "warehouses/index.html")


class CustomerListView(ListView):
    model = Customer
    template_name = "warehouses/customer-list.html"
    ordering = ["-id"]
