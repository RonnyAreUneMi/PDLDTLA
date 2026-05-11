from django.contrib import admin

from .models import Estudiante


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("cedula", "apellidos", "nombres", "correo", "carrera", "semestre", "activo")
    list_filter = ("carrera", "activo", "semestre")
    search_fields = ("cedula", "nombres", "apellidos", "correo")
    ordering = ("apellidos", "nombres")
