from django.db import models

# Create your models here.
class Pacientes(models.Model):
	nombre = models.CharField(max_length=200)
	medico = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	telefono = models.IntegerField()
	descripcion = models.TextField(max_length=500)
	fecha = models.DateField(auto_now_add=True)
	# def __unicode__(self):
	#  	return self.lib_imagen; "Titulo: %s; Autor: %s;Categoria: %s;Descripcion: %s;Fecha: %s"%(self.lib_titulo,self.lib_autor,self.lib_categoria,self.lib_descripcion,self.lib_fecha)
	# def thumbnail(self):
	# 	return '<a href="/media/%s"><img src="/media/%s" width="500"/></a>'%(self.lib_imagen,self.lib_imagen)
	# thumbnail.allow_tags=True

class Medico(models.Model):
	imagen = models.ImageField(upload_to='medicos/')
	codigo = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200)
	consultorio = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	telefono = models.IntegerField()
	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width="300"/></a>'%(self.imagen,self.imagen)
	thumbnail.allow_tags=True

class Consultorio(models.Model):
	nombre = models.CharField(max_length=200)
	horario = models.CharField(max_length=200)
	telefono = models.IntegerField()
	especialidad = models.CharField(max_length=200)
	descripcion_es = models.TextField(max_length=500)