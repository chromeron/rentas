from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('tipo/<tipo_cancha>', views.tipo, name='tipo'),
	path('check_horarios', views.check_horarios, name='check_horarios'),
	path('agendar_horarios', views.agendar_horarios, name='agendar_horarios'),
	path('<unidad>', views.unidad, name='unidad'),
	path('permiso_particulares/', views.permisoParticulares, name='permiso_particulares'),
	path('rentaxdia/<cancha>', views.rentaxdia, name='canchaxdia'),
	path('rentaxperiodo/<cancha>', views.rentaxperiodo, name='canchaxperiodo'),
	path('<cancha>/detalles/<fecha>', views.detalles, name='detalles')
]
