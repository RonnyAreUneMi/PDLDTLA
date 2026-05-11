from django import forms

from .models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            "cedula",
            "nombres",
            "apellidos",
            "correo",
            "carrera",
            "semestre",
            "activo",
        ]
        widgets = {
            "cedula": forms.TextInput(attrs={"class": "form-control", "maxlength": 10}),
            "nombres": forms.TextInput(attrs={"class": "form-control"}),
            "apellidos": forms.TextInput(attrs={"class": "form-control"}),
            "correo": forms.EmailInput(attrs={"class": "form-control"}),
            "carrera": forms.Select(attrs={"class": "form-select"}),
            "semestre": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 10}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
