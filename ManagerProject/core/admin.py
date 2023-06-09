from django.contrib import admin
from . import models as core_models


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Main details",
         {"fields": ["name", "description", "image"]}
        ),
        ("Finances - Any change here affects ALL transactions",
         {"fields": ["price_sell", "price_cost", "stock"]}
        )
    ]

    list_filter = ["price_sell", "stock", "name"]
    list_display = ["name", "price_sell", "stock"]

admin.site.register(core_models.Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Edit Order",
         {"fields": ["ordered_by", "completed"]}
        ),
        ("Add products",
         {"fields": ["products"]}
        )
    ]
    filter_horizontal = ('products', )
    list_filter = ["updated_datetime", "created_datetime"]
    list_display = ["ordered_by", "updated_datetime", "created_datetime"]

admin.site.register(core_models.Order, OrderAdmin)


class PaymentAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Edit Payment",
         {"fields": ["order", "amount", "status", "method"]}
        )
    ]

    list_filter = ["order", "status", "amount", "method"]
    list_display = ["order", "amount", "status", "method"]

admin.site.register(core_models.Payment, PaymentAdmin)
