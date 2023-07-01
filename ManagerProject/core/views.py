from django.shortcuts import render
from . import models as core_models
# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def finances(request):
    return render(request, 'core/finances.html')


def inventory(request):
    products_list = core_models.Product.objects.all()

    context = {
        'products_list': products_list
    }

    return render(request, 'core/inventory.html', context)



def edit_product(request, product_id):

    product = core_models.Product.objects.get(pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'core/product.html', context)