# Generated by Django 4.2.3 on 2023-07-08 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_transaction_total_cost_transaction_total_income_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]