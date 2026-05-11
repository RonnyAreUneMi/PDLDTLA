from django.test import TestCase
from django.urls import reverse

from .models import Estudiante


class EstudianteModelTests(TestCase):
    def test_str_returns_apellidos_nombres_cedula(self):
        est = Estudiante.objects.create(
            cedula="0102030405",
            nombres="Ana Maria",
            apellidos="Perez Loor",
            correo="ana@example.com",
        )
        self.assertEqual(str(est), "Perez Loor Ana Maria (0102030405)")

    def test_nombre_completo_property(self):
        est = Estudiante(nombres="Juan", apellidos="Suarez")
        self.assertEqual(est.nombre_completo, "Juan Suarez")


class EstudianteCRUDViewsTests(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            cedula="0999999999",
            nombres="Test",
            apellidos="User",
            correo="test@example.com",
            carrera="SIS",
            semestre=3,
        )

    def test_list_view_status_200(self):
        resp = self.client.get(reverse("estudiantes:list"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Test User")

    def test_create_view_creates_record(self):
        resp = self.client.post(
            reverse("estudiantes:create"),
            {
                "cedula": "1234567890",
                "nombres": "Nuevo",
                "apellidos": "Estudiante",
                "correo": "nuevo@example.com",
                "carrera": "SOF",
                "semestre": 1,
                "activo": "on",
            },
        )
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Estudiante.objects.filter(cedula="1234567890").exists())

    def test_detail_view_shows_estudiante(self):
        resp = self.client.get(reverse("estudiantes:detail", args=[self.estudiante.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.estudiante.correo)

    def test_delete_view_removes_record(self):
        resp = self.client.post(reverse("estudiantes:delete", args=[self.estudiante.pk]))
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Estudiante.objects.filter(pk=self.estudiante.pk).exists())
