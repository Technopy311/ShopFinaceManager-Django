from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField("Product Name", default="Product", max_length=200)
    price = models.IntegerField("Product Price", default=0)
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
    status = models.BooleanField("Paid", default=False)
    # Payment Methods
    DEBIT = "DEBI"
    CREDIT = "CRED"
    CASH = "CASH"
    OTHER = "OTR"
    
    payment_method_choices = [
        (DEBIT, "Debit Card"),
        (CREDIT, "Credit Card"),
        (CASH, "Cash"),
        (OTHER, "Other Method")
    ]

    method = models.CharField(choices=payment_method_choices, default="", max_length=40)


    def __str__(self):
        return f"{self.amount} -- {self.status}"