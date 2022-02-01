from django.contrib import admin
from .models import Produkt
from .models import Obraz
from .models import Marka

admin.site.register(Produkt)
admin.site.register(Obraz)
admin.site.register(Marka)
