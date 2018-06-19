from django.db import models

class CostosEscuelaExterna(models.Model):
	concepto = models.CharField(max_length=100)
	costo = models.IntegerField()

	def __str__(self):
		return '%s ---> $ %s.00' % (self.concepto, self.costo)

class CostosCanchaParticular(models.Model):
	concepto = models.CharField(max_length=100)
	costo = models.IntegerField()

	def __str__(self):
		return '%s ---> $ %s.00' % (self.concepto, self.costo)

class CostosLiga(models.Model):
    ZONA = (
        ('A', 'Zona A'),
        ('B', 'Zona B'),
    )
    CATEGORIA = (
        ('Libre', 'Libre'),
        ('J y F', 'Juvenil y Femenil'),
        ('Infantil', 'Infantil')
    )
    TIPO = (
        ('Soccer pasto natural y sintético', 'Soccer pasto natural y sintético'),
        ('Pasto sintético 7', 'Pasto sintético 7'),
        ('Pasto sintético 6 y rápido', 'Pasto sintético 6 y rápido'),
        ('Cemento fútbol rápido y 6', 'Cemento fútbol rápido y 6'),
        ('Soccer tierra', 'Soccer Tierra'),
        ('Multiusos', 'Multiusos')
    )
    zona = models.CharField(max_length=1, choices=ZONA)
    tipo = models.CharField(max_length=35, choices=TIPO)
    categoria = models.CharField(max_length=20, choices=CATEGORIA)
    costo = models.IntegerField()

    def __str__(self):
        return '%s -- %s -- %s --  $ %s.00' % (self.zona, self.tipo, self.categoria, self.costo)
