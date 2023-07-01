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
        products_list: 'products_list'
    }

    return render(request, 'core/inventory.html', context)