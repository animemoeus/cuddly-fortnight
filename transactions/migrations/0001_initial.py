# Generated by Django 4.2.9 on 2024-01-16 10:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("warehouses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OutgoingTransactionHeader",
            fields=[
                (
                    "transaction_number",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.supplier",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.warehouse",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OutgoingTransactionDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("box_quantity", models.PositiveIntegerField()),
                ("pcs_quantity", models.PositiveIntegerField()),
                (
                    "header",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.outgoingtransactionheader",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IncomingTransactionHeader",
            fields=[
                (
                    "transaction_number",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.supplier",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.warehouse",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IncomingTransactionDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("box_quantity", models.PositiveIntegerField()),
                ("pcs_quantity", models.PositiveIntegerField()),
                (
                    "header",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.incomingtransactionheader",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.product",
                    ),
                ),
            ],
        ),
    ]