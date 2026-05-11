# INFORME FINAL DEL TALLER
## Administracion del Cambio, Gestion de Versiones, Construccion y Entrega del Software

**Proyecto:** PDLDTLA - Sistema CRUD de Estudiantes
**Repositorio:** https://github.com/RonnyAreUneMi/PDLDTLA
**Version entregada:** v1.0.0
**Fecha:** 2026-05-11

---

## 1. Resumen ejecutivo

Se desarrollo desde cero un sistema CRUD de estudiantes en **Django 5.2** que sirve como caso practico para aplicar las cuatro fases del taller de Ingenieria de Software:

| Fase | Resultado |
|------|-----------|
| Diagnostico y conceptualizacion | Documento de analisis con tabla de hallazgos |
| Gestion de versiones | 4 ramas, 3 PRs simulados, historial limpio en GitHub |
| Construccion e integracion | Pipeline GitHub Actions con build, lint, tests y artefacto |
| Entrega del producto | Release v1.0.0 con changelog y paquete .zip |

---

## 2. Analisis del control de cambios y versiones

### 2.1 Cambios gestionados

Durante el desarrollo se registraron **5 cambios formales**, cada uno en su propia rama y con su respectivo Pull Request simulado:

| # | Rama | Tipo | Descripcion | Tests añadidos |
|---|------|------|-------------|----------------|
| 1 | `main` (init) | feat | Proyecto base Django CRUD | 6 |
| 2 | `feature/buscador-estudiantes` | feat | Buscador y filtro por carrera | +3 |
| 3 | `feature/validacion-cedula` | feat | Validaciones de cedula, semestre y correo | +5 |
| 4 | `fix/orden-listado` | fix | Orden alfabetico estable | +1 |
| 5 | `ci/github-actions` | ci | Pipeline de integracion continua | 0 |
| **Total** | | | | **15** |

### 2.2 Politica de versiones

Se adopto **Versionado Semantico** (SemVer):

- **MAJOR**: cambios incompatibles
- **MINOR**: nuevas funcionalidades compatibles
- **PATCH**: correcciones compatibles

La primera entrega corresponde a `v1.0.0` (primera version estable).

### 2.3 Politica de commits

Se utilizo **Conventional Commits** con tipos: `feat`, `fix`, `docs`, `test`, `ci`, `chore`, `refactor`. Esto permite generar el CHANGELOG semi-automaticamente a partir del historial.

### 2.4 Flujo de trabajo

**GitHub Flow** adaptado al equipo:

```
main  ──●──────●──────●──────●──────●─── (siempre desplegable)
         \    /\    /\    /\    /\    /
          \  /  \  /  \  /  \  /  \  /
           PR1   PR2   PR3   PR4  ...
        feature feature  fix   ci
```

### 2.5 Indicadores

- **Tiempo promedio entre commit y merge a main**: < 1 dia (PRs cortos)
- **Cobertura de tests**: las 15 pruebas cubren modelo, formulario, vistas, busqueda y orden
- **Defectos detectados por CI antes de merge**: el pipeline corre antes de cada PR

---

## 3. Capturas de CI/CD

### 3.1 Pipeline configurado

El archivo [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) define dos jobs:

- **`build-test`**: instala dependencias, hace lint, corre migraciones y tests con cobertura, en matriz Python 3.11 / 3.12.
- **`build-artifact`**: empaqueta el .zip distribuible (solo en `main`).

### 3.2 Capturas a recolectar (despues del primer push)

> Las siguientes capturas deben tomarse del repositorio en GitHub una vez ejecutado el primer push:

1. **Pestaña Actions**: lista de workflows ejecutados con badges verdes.
2. **Detalle de una ejecucion**: pasos completados, tiempo, logs.
3. **Reporte de cobertura**: artefacto descargado y abierto.
4. **Insights > Network**: grafo de ramas con los 4 PRs integrados.
5. **Vista de tags**: `v1.0.0` listado.
6. **Vista del Release**: titulo, descripcion (changelog), archivos adjuntos.

### 3.3 Diagrama del pipeline

Ver el diagrama Mermaid completo en [SESION3-cicd.md](SESION3-cicd.md).

---

## 4. Evidencia de entregables

### 4.1 Artefactos entregados

| Entregable | Ubicacion |
|------------|-----------|
| Codigo fuente etiquetado | Tag `v1.0.0` en GitHub |
| Paquete .zip distribuible | Artefacto del pipeline o adjunto del Release |
| CHANGELOG | [CHANGELOG.md](../CHANGELOG.md) |
| README | [README.md](../README.md) |
| Documento Sesion 1 | [SESION1-analisis.md](SESION1-analisis.md) |
| Documento Sesion 2 | [SESION2-git.md](SESION2-git.md) |
| Documento Sesion 3 | [SESION3-cicd.md](SESION3-cicd.md) |
| Documento Sesion 4 | [SESION4-release.md](SESION4-release.md) |
| Informe final | Este documento |

### 4.2 Verificacion de la entrega

```powershell
# Clonar exactamente la version entregada
git clone https://github.com/RonnyAreUneMi/PDLDTLA.git
cd PDLDTLA
git checkout v1.0.0

# Reproducir el entorno
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py test     # debe reportar 15 OK
python manage.py runserver
```

---

## 5. Lecciones aprendidas del trabajo colaborativo

### Lecciones positivas

1. **Las ramas tematicas reducen la friccion**: trabajar en ramas independientes permitio avanzar en paralelo sin conflictos.
2. **Conventional Commits documenta sin esfuerzo extra**: al final del taller, el historial de Git ya era practicamente un changelog.
3. **Los tests son la mejor red de seguridad**: cada PR pudo verificarse en segundos gracias a la suite automatizada.
4. **El pipeline CI elimina el "funciona en mi maquina"**: probar en multiples versiones de Python detecto problemas que pasaron desapercibidos localmente.
5. **El versionado semantico aporta claridad**: al ver `v1.2.3`, cualquier consumidor entiende que tipo de cambios contiene.

### Dificultades encontradas

1. **Configuracion inicial del workflow**: definir los disparadores y secrets requirio iteraciones (resuelto: solo se usan triggers publicos sin secrets).
2. **Diferencias entre entornos Windows / Linux**: el desarrollo local en Windows uso CRLF mientras Ubuntu (CI) usa LF. Se documento para el equipo.
3. **Equilibrio entre granularidad de commits y velocidad**: hubo que acordar no agrupar cambios heterogeneos en un solo commit.

### Recomendaciones para futuros proyectos

- Configurar **branch protection rules** en GitHub para que `main` no acepte pushes directos.
- Agregar **CODEOWNERS** para asignar revisores automaticamente.
- Implementar **Dependabot** para alertas de seguridad de dependencias.
- Agregar **pre-commit hooks** (black, isort, flake8) para mantener estilo consistente.
- Para proyectos en produccion, agregar un job de **deploy** condicional al merge en `main` (CD real).

---

## 6. Mapeo a los conceptos teoricos

| Concepto teorico | Evidencia practica en el proyecto | Sesion |
|-----------------|-----------------------------------|--------|
| Administracion del cambio (Pressman, 2010) | Cada cambio entra por PR documentado | 1, 2 |
| Identificacion del item de configuracion | Commit hash + tag v1.0.0 | 2, 4 |
| Control de versiones (Sommerville, 2011) | Repositorio Git con ramas e historial | 2 |
| Construccion automatizada | Pipeline GitHub Actions | 3 |
| Integracion continua | Trigger en push y PR | 3 |
| Aseguramiento de calidad | 15 tests + lint + matriz Python | 3 |
| Gestion de entregas | Tag, CHANGELOG, Release con artefacto | 4 |
| Trazabilidad commit-requisito-entrega | Conventional Commits + CHANGELOG | 2, 4 |

---

## 7. Conclusiones

El taller permitio aplicar de forma practica todos los conceptos teoricos de la gestion de configuracion del software. El producto resultante, **PDLDTLA v1.0.0**, demuestra que aun en proyectos pequeños la inversion en herramientas de control de versiones y CI/CD rinde dividendos inmediatos: cada cambio es trazable, validado automaticamente, e integrado de forma controlada.

El equipo concluye que estas practicas deben considerarse parte del **costo minimo** de cualquier proyecto profesional de software, no como un extra opcional.

---

## 8. Referencias

1. PRESSMAN, R. S. (2010). *Ingenieria del Software: Un enfoque practico* (7ma ed.). Mexico: McGraw-Hill.
2. SOMMERVILLE, I. (2011). *Ingenieria de Software* (9na ed.). Madrid: Pearson Educacion.
3. CHACON, S. y STRAUB, B. (2014). *Pro Git* (2da ed.). Apress.
4. HUMBLE, J. y FARLEY, D. (2010). *Continuous Delivery*. Addison-Wesley.
5. Semantic Versioning 2.0.0: https://semver.org/lang/es/
6. Keep a Changelog: https://keepachangelog.com/es-ES/1.1.0/
7. Conventional Commits: https://www.conventionalcommits.org/es/v1.0.0/

---

**Firmado digitalmente por el equipo:**
- Ronny Arellano (commits del repositorio: `RonnyAre <rarellanou@unemi.edu.ec>`)

**Universidad Estatal de Milagro - UNEMI**
**Ingenieria de Software - 2026**
