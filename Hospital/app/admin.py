from django.contrib import admin
from .models import Pacientes, Medico, Consultorio

# Register your models here.
@admin.register(Pacientes)
class Pacientes_admin(admin.ModelAdmin):
	list_display = ('nombre', 'medico','direccion','telefono','descripcion','fecha',)
	list_filter = ('nombre','medico')
	search_fields = ('nombre','medico',)

@admin.register(Medico)
class Medico_admin(admin.ModelAdmin):
	list_display = ('thumbnail','codigo','nombre', 'consultorio','direccion','telefono',)
	list_filter = ('nombre','codigo')
	search_fields = ('nombre','codigo',)

@admin.register(Consultorio)
class Consultorio_admin(admin.ModelAdmin):
	list_display = ('nombre', 'horario','telefono','especialidad','descripcion_es',)
	list_filter = ('nombre','especialidad')
	search_fields = ('nombre','especialidad',)