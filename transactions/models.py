import uuid

from django.db import models

from warehouses.models import Product, Supplier, Warehouse


class IncomingTransactionHeader(models.Model):
    transaction_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_number}"


class IncomingTransactionDetail(models.Model):
    header = models.OneToOneField(IncomingTransactionHeader, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    box_quantity = models.PositiveIntegerField()
    pcs_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.header.transaction_number}"


class OutgoingTransactionHeader(models.Model):
    transaction_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_number}"


class OutgoingTransactionDetail(models.Model):
    header = models.OneToOneField(OutgoingTransactionHeader, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    box_quantity = models.PositiveIntegerField()
    pcs_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.header.transaction_number}"
