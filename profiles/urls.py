from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_hitsory/<order_number>', views.order_hitsory, name='order_history')
]

