# Generated by Django 4.2.3 on 2023-07-13 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_delete_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='order',
            new_name='Order',
        ),
    ]
