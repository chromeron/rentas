from django.db import models
from unidad.models import Cancha

class Contrato(models.Model):
    fecha_elaboracion = models.DateField(default=None)
    status = models.CharField(max_length=100)

class Renta(models.Model):
    nombre = models.CharField(max_length=100)
    descuento = models.IntegerField(default = 0, blank=True)
    fecha_renta = models.DateField(auto_now=True)
    espacio = models.ForeignKey(Cancha, on_delete=models.CASCADE, blank=True, default=None)
    tipo_renta = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, default=None, blank=True)
    costo = models.FloatField(default= 0, blank=True)
    detalles = models.CharField(max_length = 255, default=None, blank=True)
    especial = models.CharField(max_length= 255, default="NO", blank=True)
    contrato = models.ForeignKey(Contrato, on_delete=models.DO_NOTHING, default=0, blank=True)
    trimestre = models.IntegerField(default=None, blank=True)
    horas_totales = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return '%s ---> %s' % (self.nombre, self.espacio_id)

class Detalles_renta(models.Model):
    fecha = models.DateField()
    hora = models.IntegerField()
    renta = models.ForeignKey(Renta, on_delete=models.CASCADE)

    #class Meta:
    #    unique_together = ('fecha', 'Department')
    def __str__(self):
        return '%s ---> %s ---> %s' % (self.renta, self.fecha, self.hora)
