# Generated by Django 4.2.3 on 2023-07-08 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0012_delete_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name="Transaction's date")),
                ('total_profit', models.IntegerField(default=0, verbose_name="Transaction's Profit")),
                ('total_cost', models.IntegerField(default=0, verbose_name="Transaction's Income")),
                ('total_income', models.IntegerField(default=0, verbose_name="Transaction's Income")),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
    ]