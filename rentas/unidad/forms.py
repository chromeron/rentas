from django import forms

class AgendarHorasForm(forms.Form):
	horas = forms.CharField()
	cancha = forms.CharField()
	fecha = forms.CharField()
