from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='bejs'),

    # path('base', views.mark, name=''),

    path('marka/<int:id>/', views.mark, name='id-marki'),
    path('ogloszenie/<int:id>/', views.ogloszenie, name='id-modelu'),
    path('dodaj_ogloszenie', views.dodajsamochod, name= 'dodaj_ogloszenieeeee'),

]
