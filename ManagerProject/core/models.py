from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Product(models.Model):
    name = models.CharField("Product Name", default="Product", max_length=200)
    price_sell = models.IntegerField("Product sell Price", default=0)
    price_cost = models.IntegerField("Product cost Price", default=0)
    stock = models.IntegerField("Product Stock", default=0)
    description = models.TextField("Product Description", default="", max_length=300)
    image = models.ImageField("Product Image", default=None)



    def __str__(self):
        return f"{self.name}"


# Signal to update transactions when product's prices change
@receiver(post_save, sender=Product)
def product_changed_callback(sender, instance, **kwargs):
    
    prev_obj = Product.objects.get(pk=instance.pk)  # Before save
    
    # Check if some price has changed

    if (prev_obj.price_cost is not instance.price_cost) or (prev_obj.price_sell is not instance.price_sell):
        
        # Access each produdcts_order and then re-save each transaction so it is updated
        related_orders = instance.order_set.all()
        
        for order in related_orders:
            print(order.transaction)
            order.transaction.save()
    else:
        pass




class Order(models.Model):
    ordered_by = models.CharField("Person who ordered", max_length=100, default="---")
    created_datetime = models.DateTimeField("Created datetime", auto_now_add=True)
    updated_datetime = models.DateTimeField("Updated datetime", auto_now=True)
    completed = models.BooleanField("Order Status", default=False)

    products = models.ManyToManyField(Product, verbose_name="Order's Products", default=None)

    def __str__(self):
        return f"Order #{self.pk}"


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

