from django.test import TestCase
from django.urls import reverse

from .forms import EstudianteForm
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


class BuscadorEstudiantesTests(TestCase):
    def setUp(self):
        Estudiante.objects.create(
            cedula="1111111111", nombres="Ana", apellidos="Castro",
            correo="ana@uni.edu", carrera="SIS", semestre=2,
        )
        Estudiante.objects.create(
            cedula="2222222222", nombres="Bruno", apellidos="Lopez",
            correo="bruno@uni.edu", carrera="SOF", semestre=4,
        )

    def test_busqueda_por_apellido_filtra_resultados(self):
        resp = self.client.get(reverse("estudiantes:list"), {"q": "Castro"})
        self.assertContains(resp, "Ana")
        self.assertNotContains(resp, "Bruno")

    def test_filtro_por_carrera(self):
        resp = self.client.get(reverse("estudiantes:list"), {"carrera": "SOF"})
        self.assertContains(resp, "Bruno")
        self.assertNotContains(resp, "Ana")

    def test_busqueda_sin_resultados_muestra_total_cero(self):
        resp = self.client.get(reverse("estudiantes:list"), {"q": "Zzz_inexistente"})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "(0)")


class EstudianteFormValidationTests(TestCase):
    BASE_VALIDA = {
        "cedula": "1712345678",
        "nombres": "Carla",
        "apellidos": "Mendoza",
        "correo": "Carla@TEST.COM",
        "carrera": "SIS",
        "semestre": 3,
        "activo": "on",
    }

    def test_cedula_no_numerica_rechazada(self):
        data = self.BASE_VALIDA | {"cedula": "ABC1234567"}
        form = EstudianteForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("cedula", form.errors)

    def test_cedula_con_longitud_invalida_rechazada(self):
        data = self.BASE_VALIDA | {"cedula": "12345"}
        form = EstudianteForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("cedula", form.errors)

    def test_cedula_provincia_invalida_rechazada(self):
        data = self.BASE_VALIDA | {"cedula": "9912345678"}
        form = EstudianteForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("cedula", form.errors)

    def test_semestre_fuera_de_rango_rechazado(self):
        data = self.BASE_VALIDA | {"semestre": 15}
        form = EstudianteForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("semestre", form.errors)

    def test_correo_se_normaliza_a_minusculas(self):
        form = EstudianteForm(self.BASE_VALIDA)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data["correo"], "carla@test.com")


class OrdenListadoTests(TestCase):
    def test_listado_ordenado_por_apellido_nombre(self):
        Estudiante.objects.create(cedula="1700000001", nombres="Zoraida", apellidos="Aguilar", correo="z@t.com")
        Estudiante.objects.create(cedula="1700000002", nombres="Andres", apellidos="Zambrano", correo="a@t.com")
        Estudiante.objects.create(cedula="1700000003", nombres="Beatriz", apellidos="Mora", correo="b@t.com")

        resp = self.client.get(reverse("estudiantes:list"))
        contenido = resp.content.decode("utf-8")

        pos_aguilar = contenido.find("Aguilar")
        pos_mora = contenido.find("Mora")
        pos_zambrano = contenido.find("Zambrano")

        self.assertTrue(0 < pos_aguilar < pos_mora < pos_zambrano,
                        "El listado debe estar ordenado alfabeticamente por apellido")
