from django.contrib import admin
from . import models as finances_models

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Edit Transaction",
         {"fields": ["order"]}
        )
    ]

    list_filter = ["date", "order"]
    list_display = ["date", "order"]

admin.site.register(finances_models.Transaction, TransactionAdmin)