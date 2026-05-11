# PDLDTLA - Sistema CRUD de Estudiantes

Taller de Ingenieria de Software - Practica de Administracion del Cambio, Gestion de Versiones, Construccion y Entrega del Software.

## Stack
- Python 3.14
- Django 5.2
- SQLite (motor por defecto)
- Bootstrap 5 (CDN)
- GitHub Actions (CI/CD)

## Estructura

```
PDLDTLA/
├── pdldtla/             # Configuracion del proyecto Django
├── estudiantes/         # App CRUD de estudiantes
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── tests.py
│   └── templates/estudiantes/
├── docs/                # Informes y evidencias del taller (4 sesiones)
├── .github/workflows/   # Pipeline CI/CD
├── requirements.txt
└── manage.py
```

## Instalacion local

```powershell
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Pruebas

```powershell
python manage.py test
```

## Documentacion del taller

| Sesion | Tema | Documento |
|--------|------|-----------|
| 1 | Diagnostico y conceptualizacion | [docs/SESION1-analisis.md](docs/SESION1-analisis.md) |
| 2 | Gestion de versiones y control de cambios | [docs/SESION2-git.md](docs/SESION2-git.md) |
| 3 | Construccion e integracion | [docs/SESION3-cicd.md](docs/SESION3-cicd.md) |
| 4 | Entrega simulada del producto | [docs/SESION4-release.md](docs/SESION4-release.md) |
| - | Informe final integrador | [docs/INFORME-FINAL.md](docs/INFORME-FINAL.md) |

## Autor
Grupo Taller - UNEMI - 2026
