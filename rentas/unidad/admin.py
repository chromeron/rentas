from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Unidad, Tipo_Cancha, Cancha

@admin.register(Unidad)
class UnidadAdmin(ImportExportModelAdmin):
	pass

admin.site.register(Tipo_Cancha)
admin.site.register(Cancha)
