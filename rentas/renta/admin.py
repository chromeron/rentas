from django.contrib import admin
from .models import Renta, Detalles_renta, Contrato

admin.site.register(Contrato)
admin.site.register(Renta)
admin.site.register(Detalles_renta)
