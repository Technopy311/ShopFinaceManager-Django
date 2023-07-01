from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def finances(request):
    return render(request, 'core/finances.html')

def inventory(request):
    return render(request, 'core/inventory.html')