# Generated by Django 4.2.1 on 2023-07-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_description_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=300, verbose_name='Product Description'),
        ),
    ]
