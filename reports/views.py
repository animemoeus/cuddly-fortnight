from django.db import models
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.views import View

from warehouses.models import Product, Warehouse


class ReportListView(View):
    def get(self, request):
        products = (
            Product.objects.all()
            .order_by("-id")
            .annotate(
                total_box_quantity_in=Coalesce(
                    Sum("incomingtransactiondetail__box_quantity"), Value(0)
                ),
                total_pcs_quantity_in=Coalesce(
                    Sum("incomingtransactiondetail__pcs_quantity"), Value(0)
                ),
                total_box_quantity_out=Coalesce(
                    Sum("outgoingtransactiondetail__box_quantity"), Value(0)
                ),
                total_pcs_quantity_out=Coalesce(
                    Sum("outgoingtransactiondetail__pcs_quantity"), Value(0)
                ),
                total_box_quantity_available=Coalesce(
                    Sum("incomingtransactiondetail__box_quantity"), Value(0)
                )
                - Coalesce(Sum("outgoingtransactiondetail__box_quantity"), Value(0)),
                total_pcs_quantity_available=Coalesce(
                    Sum("incomingtransactiondetail__pcs_quantity"), Value(0)
                )
                - Coalesce(Sum("outgoingtransactiondetail__pcs_quantity"), Value(0)),
                warehouse=models.Subquery(
                    Warehouse.objects.filter(id=models.OuterRef("pk")).values_list(
                        "name", flat=True
                    )
                ),
            )
        )

        context = {"products": products}

        return render(request, "reports/report-list.html", context)
