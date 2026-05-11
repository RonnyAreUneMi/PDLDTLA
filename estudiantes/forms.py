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

    def clean_cedula(self):
        cedula = (self.cleaned_data.get("cedula") or "").strip()
        if not cedula.isdigit():
            raise forms.ValidationError("La cedula debe contener solo digitos.")
        if len(cedula) != 10:
            raise forms.ValidationError("La cedula debe tener exactamente 10 digitos.")
        provincia = int(cedula[:2])
        if provincia < 1 or provincia > 24:
            raise forms.ValidationError("Los dos primeros digitos deben corresponder a una provincia valida (01-24).")
        return cedula

    def clean_semestre(self):
        semestre = self.cleaned_data.get("semestre")
        if semestre is None or semestre < 1 or semestre > 10:
            raise forms.ValidationError("El semestre debe estar entre 1 y 10.")
        return semestre

    def clean_correo(self):
        correo = (self.cleaned_data.get("correo") or "").strip().lower()
        return correo
