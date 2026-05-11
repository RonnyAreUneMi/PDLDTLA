# Changelog

Todas las modificaciones importantes de este proyecto se documentan aqui.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y este proyecto adopta [Versionado Semantico](https://semver.org/lang/es/).

## [1.0.0] - 2026-05-11

### Liberada
Primera version estable del sistema CRUD de estudiantes PDLDTLA.

### Agregado
- Modelo `Estudiante` con campos: cedula, nombres, apellidos, correo, carrera, semestre, activo.
- Vistas CRUD completas: listado, detalle, creacion, edicion y eliminacion.
- Interfaz web con Bootstrap 5.
- Buscador por texto sobre cedula, nombres, apellidos y correo.
- Filtro por carrera en el listado.
- Validacion estricta de cedula ecuatoriana (10 digitos, codigo de provincia 01-24).
- Validacion de rango de semestre (1-10).
- Normalizacion automatica de correos a minusculas.
- Panel de administracion de Django registrado.
- Suite de **15 pruebas automatizadas** (modelo, vistas, formularios, busqueda, orden).
- Pipeline de integracion continua en GitHub Actions con matriz Python 3.11 / 3.12.
- Generacion automatica de paquete distribuible (.zip) en pushes a `main`.

### Corregido
- Orden alfabetico estable del listado por apellido y nombre, incluso al aplicar filtros.

### Documentacion
- Documento de Sesion 1: analisis y conceptos teoricos.
- Documento de Sesion 2: comandos Git y politicas de commits.
- Documento de Sesion 3: pipeline CI/CD y diagrama de flujo.
- Documento de Sesion 4: gestion de entrega.
- Informe final integrador.

### Referencias
- Pressman, R. S. (2010). *Ingenieria del Software*. McGraw-Hill.
- Sommerville, I. (2011). *Ingenieria de Software*. Pearson Educacion.

[1.0.0]: https://github.com/RonnyAreUneMi/PDLDTLA/releases/tag/v1.0.0
