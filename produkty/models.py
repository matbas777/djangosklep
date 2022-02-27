from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Modelauta(models.Model):
    marka = models.ForeignKey('Marka', on_delete=models.CASCADE)
    model_samochodu = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.marka} {self.model_samochodu}'       # reprezentacja modelu, zeby mozna bylo sie polapac co to dokladnie jest


class Marka(models.Model):
    marka = models.CharField(max_length=50, unique=True)  # unique = TRUE <<< ten argument zrobi nam ze bedzie wyswietlalo tylko jedna nazwe modelu samochodu nawet jak bedziemy miec 1000 ogloszen z nazwa tej jednej marki np 8ogloszen z modelem samochodu "bmw" a bedzie wyswietlac tylko jeden raz BMW. moze sie polapie z tym wszystkim xd


    def __str__(self):
        return f'{self.marka}'


    # class Meta:
    #     unique_together = ('marka', 'model')  # powoduje ze wystepuje tylko jedena unikalna nazwa zmiennej np jeak jest ogloszenie  bmwx3 razy 5 to wyswietli tylko raz 'bmwx3' a oloszen jest 5

class Produkt(models.Model):
    class Paliwo(models.TextChoices):
        ON = 'Diesel', 'Diesel'
        PB = 'Benzyna', 'Benzyna'
        Hybryda = 'Hybryda', 'Hybryda'
        Electric = 'Elektryczne', 'Elektryczne'
    model_samochodu = models.ForeignKey(Modelauta, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    opis = models.TextField(null=True)
    rok_prdukcji = models.IntegerField()
    przebieg = models.IntegerField(null=True, blank=True)
    paliwo = models.CharField(max_length=20, choices=Paliwo.choices)
    HP = models.IntegerField(null=True, blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)


class Obraz(models.Model):
    obrazek = models.ImageField()
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE, null=True, blank=True)

