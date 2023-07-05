from django.shortcuts import render
from . import models as core_models
# Create your views here.


def index(request):

    """
        Shop's Dashboard
    """

    context = {
        'income':'test_income',
        'profit': 'test_profit',
        'expenses': 'test_expenses',
        'total_stock': 'test_total_stock'
    }

    return render(request, 'core/index.html', context)


def finances(request):

    """
        Finances Dashboard
    """

    return render(request, 'core/finances.html')


def inventory(request):

    """
        View to see all the inventory
    """
    
    products_list = core_models.Product.objects.all()

    context = {
        'products_list': products_list
    }

    return render(request, 'core/inventory.html', context)


def edit_product(request, product_id):

    """
        View to edit product
    """

    product = core_models.Product.objects.get(pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'core/product.html', context)


def orders(request):
    """
        Orders Dashboard
    """

    orders_list = core_models.Order.objects.all()

    context = {
        'orders_list': orders_list
    }

    return render(request, 'core/order_payments.html', context)

def edit_order(request, order_id):

    """
        View to edit an order
    """

    product = core_models.Product.objects.get(pk=order_id)

    context = {
        'product': product
    }

    return render(request, 'core/product.html', context)



def payments(request):

    """
        Payments Dashboard
    """

    payments_list = core_models.Payment.objects.all()

    context = {
        'payments_list': payments_list
    }

    return render(request, 'core/order_payments.html', context)


def edit_payment(request, payment_id):

    """
        View to edit a payment
    """

    product = core_models.Product.objects.get(pk=payment_id)

    context = {
        'product': product
    }

    return render(request, 'core/product.html', context)
