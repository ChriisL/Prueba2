from django.shortcuts import render
from app.models import Pacientes

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect

def wsPacientes(request):
	#if request.user.is_superuser:
	data = serializers.serialize('json', Pacientes.objects.all())
	return HttpResponse(data, content_type='application/json')
	#else:
	#	return HttpResponseRedirect('/')
