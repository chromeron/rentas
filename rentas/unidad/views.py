from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from django.contrib.auth.models import User

import json


from .models import Unidad, Tipo_Cancha, Cancha
from renta.models import Detalles_renta, Renta, Contrato
from .forms import AgendarHorasForm
from .barcodeGenerator import MyBarcodeDrawing

def index(request):
	unidades_list = Unidad.objects.order_by('id')
	tipo_cancha_list = Tipo_Cancha.objects.order_by('tipo')

	context = {'unidades_list': unidades_list, 'tipo_cancha_list': tipo_cancha_list}

	return render(request, 'unidad/index.html', context)

def tipo(request, tipo_cancha):
	canchas_list = Cancha.objects.filter(tipo_cancha=tipo_cancha)
	cancha_tipo = Tipo_Cancha.objects.get(pk=tipo_cancha)
	context = {'canchas': canchas_list, 'cancha_tipo': cancha_tipo}
	return render(request, 'unidad/tipo.html', context)

def unidad(request, unidad):
	try:
		canchas_list = Cancha.objects.filter(unidad=unidad)
		nombre_unidad = Unidad.objects.get(pk=unidad)
	except ObjectDoesNotExist:
		canchas_list = None
		nombre_unidad = None

	context = {'canchas': canchas_list, 'nombre_unidad': nombre_unidad}
	return render (request, 'unidad/canchas_unidad.html', context)

def rentaxdia (request, cancha):
	try:
		cancha = Cancha.objects.get(pk=cancha)
	except ObjectDoesNotExist:
		cancha = None
	context = {'cancha': cancha }
	return render (request, 'unidad/rentaxdia.html', context)


def desglose (request):
	if request.method == 'POST':
		form = AgendarHorasForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			#horas = data['horas']
			datos_horas = data['horas']
			cancha = data['cancha']
			datos_horas = datos_horas.split(',')
			datos_horas = list(map(int, datos_horas))
			cantidad_horas = len(datos_horas)
			datos_cancha = Cancha.objects.get(pk=cancha)
			total = cantidad_horas * datos_cancha.tipo_cancha.costo_particular.costo
			context = {'horas': datos_horas, 'cancha': cancha, 'fecha': data['fecha'], 'datos_cancha': datos_cancha, 'cantidad_horas': cantidad_horas, 'total': total}
		else:
			context = {'horas': None }

		return render (request, 'unidad/desglose.html', context)

def check_horarios (request):
	if request.method == 'POST':
		received_json_data = json.loads(request.body.decode("utf-8"))
		fechas = received_json_data['dias_formato']
		id = received_json_data['cancha']
		hora_inicio = received_json_data['hora_inicio']
		hora_final = received_json_data['hora_final']
		horas_conflicto = []
		#print(fechas)
		fechas_consulta = Detalles_renta.objects.filter(fecha__in=fechas).filter(renta__espacio_id=id).order_by('fecha','hora')
		if(fechas_consulta):
			for fecha in fechas_consulta:
				if fecha.hora in range(hora_inicio, hora_final+1):
					horas_conflicto.append({'dia': fecha.fecha, 'hora' : fecha.hora})
		return HttpResponse(json.dumps(horas_conflicto, indent=4, sort_keys=True, default=str), content_type='applications/json')

def agendar_horarios (request):
	if request.method == 'POST':
		agendar_json = json.loads(request.body.decode("utf-8"))
		fechas = agendar_json['dias_formato']
		id = agendar_json['cancha']
		hora_inicio = agendar_json['hora_inicio']
		hora_final = agendar_json['hora_final']
		horas_conflicto = []
		bandera = 0
		#print(fechas)
		fechas_consulta = Detalles_renta.objects.filter(fecha__in=fechas).filter(renta__espacio_id=id).order_by('fecha','hora')
		if(fechas_consulta):
			for fecha in fechas_consulta:
				if fecha.hora in range(hora_inicio, hora_final+1):
					horas_conflicto.append({'dia': fecha.fecha, 'hora' : fecha.hora})
					bandera = 1;
			if bandera == 0:
				guardar = agendar(agendar_json)

			print(fechas)
			print(horas_conflicto)
		else:
			print("No hay fechas en conflicto")
			guardar = agendar(agendar_json)


		#return HttpResponse(json.dumps(horas_conflicto), content_type='applications/json')
		return HttpResponse(json.dumps(horas_conflicto, indent=4, sort_keys=True, default=str), content_type='applications/json')

def agendar(json_data):
	print("entra a agendar")
	cancha = int(json_data['cancha'])
	contrato = Contrato.objects.get(pk=1)
	horas_totales = int(json_data['horas_totales'])

	registro = Renta(nombre=json_data['usuario'],
				 	 espacio_id= cancha,
					 tipo_renta=json_data['tipo_renta'],
					 status=json_data['status'],
					 costo=json_data['costo'],
					 detalles=json_data['detalles'],
					 especial=json_data['especial'],
					 contrato = contrato,
					 trimestre=json_data['trimestre'],
					 horas_totales = horas_totales)
	registro.save()
	return "manda los datos"

def rentaxperiodo (request, cancha):
	try:
		usuarios = User.objects.filter(is_staff=False).order_by('username')
		cancha = Cancha.objects.get(pk=cancha)
	except ObjectDoesNotExist:
		cancha = None
	context = {'cancha': cancha, 'usuarios': usuarios }
	return render (request, 'unidad/rentaxperiodo.html', context)

def detalles (request, cancha, fecha):
	horarios = Detalles_renta.objects.order_by('hora').filter(renta__espacio_id=cancha).filter(fecha=fecha)
	horarios = [ horario_serializer(horario) for horario in horarios ]
	return HttpResponse(json.dumps(horarios), content_type='applications/json')
	#return render (request, 'unidad/detalles.html', context)

def horario_serializer(horario):
	return {'hora': horario.hora }

def permisoParticulares(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="somefilename.pdf"'
	p = canvas.Canvas(response)
	b = MyBarcodeDrawing("123456789201299301")
	#barcode = code128.Code128("123456789", barWidth=0.07*cm, barHeight=2*cm)
	b.drawOn(p, 5*cm, 5*cm)
	p.drawString(100, 500, "Hello world.")
	p.drawString(100, 800, "Hello world.")
	p.showPage()
	p.save()
	return response
