from django.shortcuts import render
from datetime import datetime
from . models import Marka

def produkt_list(request):
    return render(request, 'produkty/produkt_list.html', {'czas': datetime.utcnow()})
                            #sciezka                       #kontekst

def mark(request, id):
    return render(request, 'produkty/produkt_list.html', {'mark': Marka.objects.get(pk=id)})

def wszystko(request):
    return render(request, 'produkty/mark.html', {'marka': Marka.objects.all()})