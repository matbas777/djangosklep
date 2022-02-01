from django.shortcuts import render
from datetime import datetime

def produkt_list(request):
    return render(request, 'produkty/produkt_list.html', {'czas': datetime.utcnow()})



