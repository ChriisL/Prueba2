#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse, HttpRequest
from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.views.generic import TemplateView
from .models import Pacientes, Medico, Consultorio
#from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Q

def bienvenido(request):
	return render(request, 'inicio.html')

def acerca(request):
	return render(request, 'app/acerca.html')

def listado_medico(request):
	lis = Medico.objects.all()
	return render(request,'app/reporte_medico.html',{'lis':lis})

def listado_paciente(request):
	lis = Pacientes.objects.all().order_by('nombre')
	return render(request,'app/reporte_paciente.html',{'lis':lis})

def medico_consultorio(request):
	lis = Medico.objects.all()
	return render(request,'app/medico_consultorio.html',{'lis':lis})

def medico_paciente(request):
	lis = Pacientes.objects.all()
	return render(request,'app/medico_paciente.html',{'lis':lis})

def listado_consultorio(request):
	lis = Consultorio.objects.all()
	return render(request,'app/reporte_consultorio.html',{'lis':lis})

def datosmedico(request):
	con = Consultorio.objects.all()
	if request.POST:
			imagen = request.FILES['imagen']
			codigo = request.POST['codigo']
			nombre = request.POST['nombre']
			consultorio = request.POST['consultorio']
			direccion = request.POST['direccion']
			telefono = request.POST['telefono']
			Medico.objects.create(imagen=imagen,codigo=codigo,nombre=nombre,consultorio=consultorio,direccion=direccion,telefono=telefono)
			ctx = {'mensaje':'Se guardo el Medico','con':con}
	else:
		ctx = {'mensaje':'Aun no registra un Medico','con':con}
	return render(request,'app/registro_medico.html',ctx)

def datospaciente(request):
	con = Medico.objects.all().order_by('nombre')
	if request.POST:
			nombre = request.POST['nombre']
			medico = request.POST['medico']
			direccion = request.POST['direccion']
			telefono = request.POST['telefono']
			descripcion = request.POST['descripcion']
			Pacientes.objects.create(nombre=nombre,medico=medico,direccion=direccion,telefono=telefono,descripcion=descripcion)
			ctx = {'mensaje':'Se guardo el Paciente','con':con}
	else:
		ctx = {'mensaje':'Aun no registra el Paciente','con':con}
	return render(request,'app/registro_paciente.html',ctx)

def datosconsultorio(request):
	if request.POST:
			nombre = request.POST['nombre']
			horario = request.POST['horario']
			telefono = request.POST['telefono']
			especialidad = request.POST['especialidad']
			descripcion_es = request.POST['descripcion_es']
			Consultorio.objects.create(nombre=nombre,horario=horario,telefono=telefono,especialidad=especialidad,descripcion_es=descripcion_es)
			ctx = {'mensaje':'Se guardo el Consultorio'}
	else:
		ctx = {'mensaje':'Aun no guarda el Consultorio'}
	return render(request,'app/registro_consultorio.html',ctx)

