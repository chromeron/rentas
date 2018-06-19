from django.shortcuts import render
from rest_framework import viewsets
from .models import Detalles_renta, Renta
#from unidad.models import Cancha
from .serializers import Detalles_rentaSerializer, RentaSerializer

class RentaView(viewsets.ModelViewSet):
    #queryset = Renta.objects.filter(cancha__id='cancha_id')
    queryset = Renta.objects.all()
    serializer_class = RentaSerializer

class Detalles_rentaView(viewsets.ModelViewSet):
    queryset = Detalles_renta.objects.all()
    serializer_class = Detalles_rentaSerializer
