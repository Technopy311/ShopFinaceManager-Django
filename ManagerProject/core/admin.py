from django.contrib import admin
from . import models as core_models


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(core_models.Product, ProductAdmin)