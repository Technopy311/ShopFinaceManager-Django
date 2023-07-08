from django.shortcuts import render
from . import models as finance_models


def index(request):
    return render(request, 'finances/finances.html')


def profit(request):

    """
        Finances Dashboard
    """

    transaction_list = finance_models.Transaction.objects.all()

    context = {
        'transaction_list': transaction_list
    }

    return render(request, 'finances/profit.html', context)


def costs(request):

    """
        Finances Dashboard
    """

    transaction_list = finance_models.Transaction.objects.all()

    context = {
        'transaction_list': transaction_list
    }

    return render(request, 'finances/costs.html', context)



def income(request):

    """
        Finances Dashboard
    """

    transaction_list = finance_models.Transaction.objects.all()

    context = {
        'transaction_list': transaction_list
    }

    return render(request, 'finances/income.html', context)


def transactions(request):

    """
        Finances Dashboard
    """

    transaction_list = finance_models.Transaction.objects.all()

    context = {
        'transaction_list': transaction_list
    }

    return render(request, 'finances/transactions.html', context)



def edit_transaction(request, transaction_id):

    """
        View to edit a payment
    """

    transaction = finance_models.Transaction.objects.get(pk=transaction_id)
    payment_list = transaction.order.payment_set.all()
    order = transaction.order()
    products = order.product()

    transaction_profit = 0
    transaction_income = 0
    transaction_cost = 0

    # for product in order.:
    #     transaction_cost += 
    

    context = {
        
    }

    return render(request, 'finance/transaction.html', context)
