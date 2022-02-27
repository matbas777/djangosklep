from django.contrib import admin
from .models import Produkt
from .models import Obraz
from .models import Marka
from .models import Modelauta

admin.site.register(Produkt)
admin.site.register(Obraz)
admin.site.register(Marka)
admin.site.register(Modelauta)
