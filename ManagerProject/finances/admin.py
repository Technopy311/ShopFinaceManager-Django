from django.contrib import admin
from . import models as finances_models

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Edit Transaction",
         {"fields": ["order"]}
        ),
        ("Finance values - only edit if necessary",
         {"fields": ["total_profit", "total_income", "total_cost"]}
        )
    ]

    list_filter = ["date", "order"]
    list_display = ["date", "order"]

admin.site.register(finances_models.Transaction, TransactionAdmin)