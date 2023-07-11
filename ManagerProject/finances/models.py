from django.db import models
from core.models import Order


class Transaction(models.Model):
    date = models.DateTimeField("Transaction's date", auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)        

    total_profit = models.IntegerField("Transaction's Profit", default=0)
    total_cost = models.IntegerField("Transaction's Income", default=0)
    total_income = models.IntegerField("Transaction's Income", default=0)


    def __str__(self):
        return f"Transaction #{self.pk}"


    def calc_cost(self):
    
        for product in self.order.product.objects.all():
            self.total_cost += product.price_cost()


    def calc_income(self):
        for product in self.order.product.objects.all():
            self.total_income += product.price_sell()


    def calc_profit(self):
        self.total_profit = self.total_income - self.total_cost

    
