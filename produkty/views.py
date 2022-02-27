from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from . models import Marka, Modelauta, Produkt
from . forms import DodajogloszenieForm

from django.urls import reverse

# def produkt_list(request):
#     return render(request, 'produkty/ogloszenia.html', {'czas': datetime.utcnow()})
#                             #sciezka                       #kontekst
#


def mark(request, id):
    return render(request, 'produkty/model.html', {'model':Modelauta.objects.filter(marka_id=id)})


def base(request):
    return render(request, 'produkty/base.html', {'marka':Marka.objects.all()})


def ogloszenie(request, id):
    return render(request, 'produkty/ogloszenia.html', {'ogloszenie': Produkt.objects.filter(model_samochodu_id=id)})# w nawiasach() podajemy nasz foreingkey

@login_required
def dodajsamochod(request):
    return render(request, 'produkty/dodaj_ogloszenie_samochodu.html', {'dodaj_ogloszenie': DodajogloszenieForm})