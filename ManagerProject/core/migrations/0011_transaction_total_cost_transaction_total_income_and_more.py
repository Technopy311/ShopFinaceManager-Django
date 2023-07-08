# Generated by Django 4.2.3 on 2023-07-08 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_order_completed_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='total_cost',
            field=models.IntegerField(default=0, verbose_name="Transaction's Income"),
        ),
        migrations.AddField(
            model_name='transaction',
            name='total_income',
            field=models.IntegerField(default=0, verbose_name="Transaction's Income"),
        ),
        migrations.AddField(
            model_name='transaction',
            name='total_profit',
            field=models.IntegerField(default=0, verbose_name="Transaction's Profit"),
        ),
    ]
