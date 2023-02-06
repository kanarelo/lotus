# Generated by Django 4.0.5 on 2023-02-01 00:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0172_transfer_flat_fees_to_recurring"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalplanversion",
            name="flat_fee_billing_type",
        ),
        migrations.RemoveField(
            model_name="historicalplanversion",
            name="flat_rate",
        ),
        migrations.RemoveField(
            model_name="planversion",
            name="flat_fee_billing_type",
        ),
        migrations.RemoveField(
            model_name="planversion",
            name="flat_rate",
        ),
    ]