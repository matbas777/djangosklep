from django.db import models
from django.contrib.auth.models import User


class Marka(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.marka}, {self.model}'

    class Meta:
        unique_together= ('marka', 'model')

class Produkt(models.Model):
    class Paliwo(models.TextChoices):
        ON = 'Diesel', 'Diesel'
        PB = 'Benzyna', 'Benzyna'
        Hybryda = 'Hybryda', 'Hybryda'
        Electric = 'Elektryczne', 'Elektryczne'
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    opis = models.TextField(null= True)
    rok_prdukcji = models.IntegerField()
    przebieg = models.IntegerField(null=True, blank=True)
    paliwo = models.CharField(max_length=20, choices=Paliwo.choices)
    HP = models.IntegerField(null=True, blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)


class Obraz(models.Model):
    obrazek = models.ImageField()
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE, null=True, blank=True)

