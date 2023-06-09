# Generated by Django 4.2.1 on 2023-07-01 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Product', max_length=200, verbose_name='Product Name')),
                ('price', models.IntegerField(default=0, verbose_name='Product Price')),
                ('stock', models.IntegerField(default=0, verbose_name='Product Stock')),
            ],
        ),
    ]
