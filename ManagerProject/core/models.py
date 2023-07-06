from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField("Product Name", default="Product", max_length=200)
    price_sell = models.IntegerField("Product sell Price", default=0)
    price_cost = models.IntegerField("Product cost Price", default=0)
    stock = models.IntegerField("Product Stock", default=0)
    description = models.TextField("Product Description", default="", max_length=300)
    image = models.ImageField("Product Image", default=None)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    ordered_by = models.CharField("Person who ordered", max_length=100, default="---")
    created_datetime = models.DateTimeField("Created datetime", auto_now_add=True)
    updated_datetime = models.DateTimeField("Updated datetime", auto_now=True)
    
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.product}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField("Payment amount", default=0)
    status = models.BooleanField("Payment Confimation", default=False)
    
    payment_method_choices = [
        ("Debit Card", "Debit Card"),
        ("Credit Card", "Credit Card"),
        ("Cash", "Cash"),
        ("Other Method", "Other Method")
    ]

    method = models.CharField(choices=payment_method_choices, default="", max_length=40)


    def __str__(self):
        return f"{self.amount} -- {self.status}"


class Transaction(models.Model):
    date = models.DateTimeField("Transaction's date", auto_now=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction #{self.pk}"
    

    def get_cost(self):
        transaction_products = self.order.product.objects.all()
        cost = 0
        
        for product in transaction_products:
            print(product.price_cost)
            cost += product.price_cost

        return cost
    

    def get_profit(self):
        transaction_products = self.order.product.objects.all()

        total_profit = 0

        for product in transaction_products:
            total_profit += (product.price_sell - product.price_cost)

        return total_profit