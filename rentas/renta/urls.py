from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('detalles', views.Detalles_rentaView)
router.register('renta', views.RentaView)

urlpatterns = [
    path('', include(router.urls))
]
