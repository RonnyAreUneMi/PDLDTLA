from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import EstudianteForm
from .models import Estudiante


def estudiante_list(request):
    q = (request.GET.get("q") or "").strip()
    carrera = (request.GET.get("carrera") or "").strip()

    estudiantes = Estudiante.objects.all()
    if q:
        estudiantes = estudiantes.filter(
            Q(cedula__icontains=q)
            | Q(nombres__icontains=q)
            | Q(apellidos__icontains=q)
            | Q(correo__icontains=q)
        )
    if carrera:
        estudiantes = estudiantes.filter(carrera=carrera)

    return render(
        request,
        "estudiantes/list.html",
        {
            "estudiantes": estudiantes,
            "total": estudiantes.count(),
            "q": q,
            "carrera_seleccionada": carrera,
            "carreras": Estudiante.CARRERAS,
        },
    )


def estudiante_detail(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, "estudiantes/detail.html", {"estudiante": estudiante})


def estudiante_create(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            est = form.save()
            messages.success(request, f"Estudiante '{est.nombre_completo}' creado correctamente.")
            return redirect(reverse("estudiantes:list"))
    else:
        form = EstudianteForm()
    return render(
        request,
        "estudiantes/form.html",
        {"form": form, "titulo": "Nuevo estudiante", "accion": "Crear"},
    )


def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante actualizado correctamente.")
            return redirect(reverse("estudiantes:detail", args=[estudiante.pk]))
    else:
        form = EstudianteForm(instance=estudiante)
    return render(
        request,
        "estudiantes/form.html",
        {"form": form, "titulo": "Editar estudiante", "accion": "Guardar cambios"},
    )


def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        estudiante.delete()
        messages.success(request, "Estudiante eliminado.")
        return redirect(reverse("estudiantes:list"))
    return render(request, "estudiantes/confirm_delete.html", {"estudiante": estudiante})
