from django.shortcuts import render
from . import models as core_models
from finances import models as finances_models

from django.db.models import Sum
from django.db.models.functions import ExtractMonth

# Create your views here.


def index(request):

    """
        Shop's Dashboard
    """
    
    # Get Main Indicators
    finance_data = finances_models.Transaction.objects.aggregate(
        Sum('total_profit'), 
        Sum('total_cost'),
        Sum('total_income')
    )

    stock_data = core_models.Product.objects.aggregate(
        Sum('stock')
    )

    total_income = finance_data['total_income__sum']
    total_profit = finance_data['total_profit__sum']
    total_expenses = finance_data['total_cost__sum']
    total_stock = stock_data['stock__sum']

    # Get latest sales

    latest_sales = finances_models.Transaction.objects.all().order_by('date')[:5]

    
    # order sales by month
    sales_with_month = finances_models.Transaction.objects.order_by('date').annotate(month=ExtractMonth('date'))

    profit_by_month = [0,0,0,0,0,0,0,0,0,0,0,0]

    # Sum the profit in an array
    for item in sales_with_month:
        profit_by_month[item.month-1] += item.total_profit

    context = {
        'income':total_income,
        'profit': total_profit,
        'expenses': total_expenses,
        'total_stock': total_stock,
        'latest_sales': latest_sales,
        'profit_by_month': profit_by_month
    }   

    return render(request, 'core/index.html', context)


def inventory(request):

    """
        View to see all the inventory
    """
    
    products_list = core_models.Product.objects.all()

    context = {
        'products_list': products_list
    }

    return render(request, 'core/inventory.html', context)


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

    order = core_models.Order.objects.get(pk=order_id)
    
    payment_list = order.payment_set.all()


    context = {
        'order': order,
        'payment_list': payment_list
    }

    return render(request, 'core/order.html', context)



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

    payment = core_models.Payment.objects.get(pk=payment_id)

    context = {
        'payment': payment
    }

    return render(request, 'core/payment.html', context)


