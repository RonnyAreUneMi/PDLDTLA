# Sesion 4 - Entrega Simulada del Producto

## Actividad 1: Entrega de la version 1.0.0

### Datos de la entrega

| Campo | Valor |
|-------|-------|
| Nombre del producto | PDLDTLA - Sistema CRUD de Estudiantes |
| Version | 1.0.0 |
| Fecha de liberacion | 2026-05-11 |
| Tag de Git | `v1.0.0` |
| Tipo | Release inicial estable |
| Plataforma | Web (Django 5.2) |
| Licencia | Academica |
| Distribucion | GitHub Releases |

### Versionado semantico aplicado

```
v 1 . 0 . 0
  │   │   │
  │   │   └── PATCH: correcciones compatibles (0 a la fecha)
  │   └────── MINOR: funcionalidades compatibles (0 a la fecha)
  └────────── MAJOR: primera version estable
```

### Artefactos de la entrega

1. **Codigo fuente**: tag `v1.0.0` en el repositorio
2. **Paquete distribuible**: `pdldtla-v1.0.0.zip` (codigo + requirements + docs, sin venv ni db)
3. **CHANGELOG.md**: registro de cambios
4. **README.md**: instrucciones de instalacion y uso
5. **Documentos de las 4 sesiones** en `docs/`

### Comandos ejecutados para la entrega

```bash
# 1. Asegurar que main esta limpio y con todos los cambios
git checkout main
git pull origin main
git status                       # debe estar limpio

# 2. Crear tag anotado v1.0.0
git tag -a v1.0.0 -m "Release v1.0.0: primera version estable"

# 3. Publicar el tag en GitHub
git push origin v1.0.0

# 4. (Opcional, con gh CLI) crear el Release
gh release create v1.0.0 \
  --title "PDLDTLA v1.0.0 - Primera version estable" \
  --notes-file CHANGELOG.md \
  pdldtla-v1.0.0.zip

# 5. Sin gh CLI: ir a https://github.com/RonnyAreUneMi/PDLDTLA/releases/new
#    - Seleccionar tag v1.0.0
#    - Titulo: "PDLDTLA v1.0.0"
#    - Pegar el contenido del CHANGELOG.md
#    - Adjuntar el .zip
#    - Publicar
```

### Generacion del archivo .zip distribuible

El propio pipeline genera el ZIP en cada push a `main`. Tambien se puede crear localmente:

```powershell
Compress-Archive -Path *.py, manage.py, requirements.txt, README.md, CHANGELOG.md, `
                       estudiantes, pdldtla, docs, .github `
                 -DestinationPath pdldtla-v1.0.0.zip
```

## Actividad 2: Informe final

Ver [INFORME-FINAL.md](INFORME-FINAL.md).

## Repositorio de artefactos

Todos los artefactos quedan disponibles en:

- **Releases**: https://github.com/RonnyAreUneMi/PDLDTLA/releases
- **Actions (builds)**: https://github.com/RonnyAreUneMi/PDLDTLA/actions
- **Tags**: https://github.com/RonnyAreUneMi/PDLDTLA/tags

## Reflexion sobre la entrega

La estrategia adoptada permite:

1. **Reproducibilidad**: cualquier desarrollador puede checar el tag `v1.0.0` y obtener exactamente el estado liberado.
2. **Auditoria**: el CHANGELOG documenta cada decision y el historial Git la traza al commit exacto.
3. **Reversibilidad**: si la entrega presenta defectos, basta con liberar `v1.0.1` con el fix; las versiones anteriores siguen disponibles.
4. **Automatizacion**: el pipeline ya genera el artefacto, eliminando errores manuales de empaquetado.
