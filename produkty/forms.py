from django import forms
from . models import Produkt
# from accounts.models import # skad mam zaimportowac usera?


class DodajogloszenieForm(forms.ModelForm):
    class Meta:
        model = Produkt
        fields = '__all__'