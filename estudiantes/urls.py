from django.urls import path

from . import views

app_name = "estudiantes"

urlpatterns = [
    path("", views.estudiante_list, name="list"),
    path("nuevo/", views.estudiante_create, name="create"),
    path("<int:pk>/", views.estudiante_detail, name="detail"),
    path("<int:pk>/editar/", views.estudiante_update, name="update"),
    path("<int:pk>/eliminar/", views.estudiante_delete, name="delete"),
]
