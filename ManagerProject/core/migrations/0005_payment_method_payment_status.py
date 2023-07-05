# Generated by Django 4.2.1 on 2023-07-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('DEBI', 'Debit Card'), ('CRED', 'Credit Card'), ('CASH', 'Cash'), ('OTR', 'Other Method')], default='', max_length=40),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Paid'),
        ),
    ]