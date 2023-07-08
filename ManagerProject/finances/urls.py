from django.urls import path
from . import views as finance_views



urlpatterns = [
    path('finances/', finance_views.index, name='finances'),
    path('transactions/', finance_views.transactions , name='transactions'),
    path('transaction/<int:transaction_id>', finance_views.edit_transaction, 
         name='transaction'),

    path('income/', finance_views.income , name='income'),
    path('profit/', finance_views.profit , name='profit'),
    path('costs/', finance_views.costs , name='costs'),
]