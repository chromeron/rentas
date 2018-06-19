from rest_framework import serializers
from .models import Detalles_renta, Renta

class RentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renta
        fields = ('id', 'nombre', 'descuento', 'fecha_renta', 'renta_id', 'tipo_renta')

class Detalles_rentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalles_renta
        fields = ('id', 'fecha', 'hora', 'renta_id')
