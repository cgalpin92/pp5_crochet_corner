from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history', views.order_history, name='order_history'),
    path('order_history/<order_number>', views.order_history_item, name='order_history_item')
]