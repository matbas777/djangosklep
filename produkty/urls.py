from django.urls import path
from . import views

urlpatterns = [
    path('', views.produkt_list, name='produkt_list'),
    path('base', views.wszystko, name='base'),
    path('marka/<int:id>/', views.mark, name='marka')
]
