from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('finances/', core_views.finances, name='finances'),
    path('inventory/', core_views.inventory, name='inventory'),
    path('product/<int:product_id>', core_views.edit_product, name='edit_product')
]