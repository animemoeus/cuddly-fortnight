from django.test import TestCase
from django.utils import timezone

from warehouses.models import Product, Supplier, Warehouse

from .models import (
    IncomingTransactionDetail,
    IncomingTransactionHeader,
    OutgoingTransactionDetail,
    OutgoingTransactionHeader,
)


class TransactionModelTestCase(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.product = Product.objects.create(name="Test Product")

    def test_incoming_transaction_header_str_method(self):
        incoming_header = IncomingTransactionHeader.objects.create(
            warehouse=self.warehouse, supplier=self.supplier, notes="Test Notes"
        )
        self.assertEqual(str(incoming_header), str(incoming_header.transaction_number))

    def test_incoming_transaction_detail_str_method(self):
        incoming_header = IncomingTransactionHeader.objects.create(
            warehouse=self.warehouse, supplier=self.supplier, notes="Test Notes"
        )
        incoming_detail = IncomingTransactionDetail.objects.create(
            header=incoming_header,
            product=self.product,
            box_quantity=10,
            pcs_quantity=5,
        )
        expected_str = str(incoming_header.transaction_number)
        self.assertEqual(str(incoming_detail), expected_str)

    def test_outgoing_transaction_header_str_method(self):
        outgoing_header = OutgoingTransactionHeader.objects.create(
            warehouse=self.warehouse, supplier=self.supplier, notes="Test Notes"
        )
        self.assertEqual(str(outgoing_header), str(outgoing_header.transaction_number))

    def test_outgoing_transaction_detail_str_method(self):
        outgoing_header = OutgoingTransactionHeader.objects.create(
            warehouse=self.warehouse, supplier=self.supplier, notes="Test Notes"
        )
        outgoing_detail = OutgoingTransactionDetail.objects.create(
            header=outgoing_header,
            product=self.product,
            box_quantity=10,
            pcs_quantity=5,
        )
        expected_str = str(outgoing_header.transaction_number)
        self.assertEqual(str(outgoing_detail), expected_str)

    def test_transaction_header_created_at_auto_now_add(self):
        incoming_header = IncomingTransactionHeader.objects.create(
            warehouse=self.warehouse, supplier=self.supplier, notes="Test Notes"
        )
        outgoing_header = OutgoingTransactionHeader.objects.create(
            warehouse=self.warehouse, supplier=self.supplier, notes="Test Notes"
        )

        self.assertTrue(
            timezone.now() - incoming_header.datetime < timezone.timedelta(seconds=1)
        )
        self.assertTrue(
            timezone.now() - outgoing_header.datetime < timezone.timedelta(seconds=1)
        )
