from django.db import models
from costos.models import CostosCanchaParticular, CostosEscuelaExterna, CostosLiga

class Unidad(models.Model):
	clave = models.CharField(max_length = 5)
	nombre = models.CharField(max_length = 250)
	ubicacion = models.CharField(max_length= 500)
	colonia = models.CharField(max_length=50)
	zona = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre

class Tipo_Cancha(models.Model):
	tipo = models.CharField(max_length= 50)
	imagen = models.ImageField(null=True, blank=True, upload_to='images')

	def __str__(self):
		return self.tipo

class Cancha(models.Model):
	unidad = models.ForeignKey(Unidad, on_delete=models.DO_NOTHING)
	tipo_cancha = models.ForeignKey(Tipo_Cancha, on_delete=models.DO_NOTHING)
	ubicacion_interna = models.CharField(max_length=300)
	clave_cancha = models.CharField(max_length=10)
	activa = models.BooleanField()
	costo_escuela = models.ForeignKey(CostosEscuelaExterna, on_delete=models.DO_NOTHING)
	costo_particular = models.ForeignKey(CostosCanchaParticular, on_delete=models.DO_NOTHING)
	costo_liga_libre = models.ForeignKey(CostosLiga, on_delete=models.DO_NOTHING, related_name = 'libre', default = 0)
	costo_liga_jyf = models.ForeignKey(CostosLiga, on_delete=models.DO_NOTHING, related_name = 'juvenilyfemenil', default = 0)
	costo_liga_infantil = models.ForeignKey(CostosLiga, on_delete=models.DO_NOTHING, related_name = 'infantil', default = 0)


	def __str__(self):
		#return self.clave_cancha
		return '%s ---> %s' % (self.unidad, self.tipo_cancha)
