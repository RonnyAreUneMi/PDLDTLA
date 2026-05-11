from django.db import models


class Estudiante(models.Model):
    CARRERAS = [
        ("SIS", "Ingenieria en Sistemas"),
        ("SOF", "Ingenieria en Software"),
        ("IND", "Ingenieria Industrial"),
        ("ADM", "Administracion"),
        ("CON", "Contabilidad"),
    ]

    cedula = models.CharField("Cedula", max_length=10, unique=True)
    nombres = models.CharField("Nombres", max_length=80)
    apellidos = models.CharField("Apellidos", max_length=80)
    correo = models.EmailField("Correo electronico", unique=True)
    carrera = models.CharField("Carrera", max_length=3, choices=CARRERAS, default="SIS")
    semestre = models.PositiveSmallIntegerField("Semestre", default=1)
    activo = models.BooleanField("Activo", default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["apellidos", "nombres"]
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.apellidos} {self.nombres} ({self.cedula})"

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"
