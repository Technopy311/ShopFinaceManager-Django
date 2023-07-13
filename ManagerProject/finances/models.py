from django.db import models
from django.db.models import Sum
from core.models import Order



class Transaction(models.Model):
    date = models.DateTimeField("Transaction's date", auto_now=True)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)

    total_profit = models.IntegerField("Transaction's Profit", default=0)
    total_cost = models.IntegerField("Transaction's Income", default=0)
    total_income = models.IntegerField("Transaction's Income", default=0)


    def __str__(self):
        return f"Transaction #{self.pk} -- {self.order.ordered_by}"


    def save(self, *args, **kwargs):
        
        data = self.order.products.aggregate(
            Sum('price_cost',),
            Sum('price_sell')
        )


        self.total_cost = data['price_cost__sum']
        self.total_income = data['price_sell__sum']

        self.total_profit = self.total_income - self.total_cost

        return super().save(*args, **kwargs)
    