# Sesion 4 - Actividad 1: Entrega simulada (Release)

## Datos de la entrega

| Campo | Valor |
|-------|-------|
| Producto | PDLDTLA - Sistema CRUD de Estudiantes |
| Version | v1.0.0 (versionado semantico) |
| Fecha | 2026-05-11 |
| Tag de Git | v1.0.0 |
| Repositorio de artefactos | GitHub Releases |
| Tipo | Release inicial estable |

## Componentes de la entrega

- **Codigo fuente etiquetado:** tag v1.0.0 en https://github.com/RonnyAreUneMi/PDLDTLA/tags
- **Archivo comprimido:** pdldtla-v1.0.0.zip (adjunto al Release)
- **Changelog:** [CHANGELOG.md](https://github.com/RonnyAreUneMi/PDLDTLA/blob/main/CHANGELOG.md) siguiendo Keep a Changelog

## Comandos ejecutados

```powershell
# Crear el tag de la version
git tag -a v1.0.0 -m "Release v1.0.0: primera version estable"

# Subir el tag al remoto
git push origin v1.0.0

# Generar el archivo comprimido
Compress-Archive -Path manage.py, requirements.txt, README.md, CHANGELOG.md, estudiantes, pdldtla, docs, .github, .gitignore -DestinationPath pdldtla-v1.0.0.zip
```
