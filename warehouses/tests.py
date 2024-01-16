from django.test import TestCase
from django.utils import timezone

from .models import Customer, Product, Supplier, Warehouse


class ModelTestCase(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Supplier 1")
        self.customer = Customer.objects.create(name="Customer 1")
        self.product = Product.objects.create(name="Product 1")
        self.warehouse = Warehouse.objects.create(name="Warehouse 1")

    def test_supplier_str_method(self):
        self.assertEqual(str(self.supplier), "Supplier 1")

    def test_customer_str_method(self):
        self.assertEqual(str(self.customer), "Customer 1")

    def test_product_str_method(self):
        self.assertEqual(str(self.product), "Product 1")

    def test_warehouse_str_method(self):
        self.assertEqual(str(self.warehouse), "Warehouse 1")

    def test_models_created_at_auto_now_add(self):
        self.assertTrue(
            timezone.now() - self.supplier.created_at < timezone.timedelta(seconds=1)
        )
        self.assertTrue(
            timezone.now() - self.customer.created_at < timezone.timedelta(seconds=1)
        )
        self.assertTrue(
            timezone.now() - self.product.created_at < timezone.timedelta(seconds=1)
        )
        self.assertTrue(
            timezone.now() - self.warehouse.created_at < timezone.timedelta(seconds=1)
        )

    def test_models_updated_at_auto_now(self):
        self.supplier.name = "Updated Supplier"
        self.supplier.save()
        self.assertTrue(
            timezone.now() - self.supplier.updated_at < timezone.timedelta(seconds=1)
        )

        self.customer.name = "Updated Customer"
        self.customer.save()
        self.assertTrue(
            timezone.now() - self.customer.updated_at < timezone.timedelta(seconds=1)
        )

        self.product.name = "Updated Product"
        self.product.save()
        self.assertTrue(
            timezone.now() - self.product.updated_at < timezone.timedelta(seconds=1)
        )

        self.warehouse.name = "Updated Warehouse"
        self.warehouse.save()
        self.assertTrue(
            timezone.now() - self.warehouse.updated_at < timezone.timedelta(seconds=1)
        )
