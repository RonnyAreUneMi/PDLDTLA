# Sesion 1 - Diagnostico y Conceptualizacion

## Actividad 1: Seleccion del proyecto

Se selecciona el proyecto **PDLDTLA** (Sistema CRUD de Estudiantes) construido desde cero con **Django 5.2** y **SQLite**. El proyecto implementa las cuatro operaciones CRUD clasicas (Crear, Leer, Actualizar, Eliminar) sobre la entidad `Estudiante` y servira como base para aplicar los conceptos de las cuatro sesiones del taller.

Repositorio: https://github.com/RonnyAreUneMi/PDLDTLA.git

## Actividad 2: Analisis del proyecto

### 2.1 Procesos de cambio evidenciados

| Categoria | Evidencia en el proyecto |
|-----------|--------------------------|
| Cambios correctivos | Correccion del ordenamiento del listado de estudiantes (rama `fix/orden-listado`) |
| Cambios perfectivos | Incorporacion de buscador y filtros (rama `feature/buscador-estudiantes`) |
| Cambios preventivos | Validacion fuerte de cedula y semestre (rama `feature/validacion-cedula`) |
| Cambios adaptativos | Configuracion de pipeline CI en GitHub Actions (Sesion 3) |

### 2.2 Gestion del control de versiones

Se usa **Git + GitHub** bajo el flujo **GitHub Flow**:

- Rama protegida: `main`
- Ramas tematicas: `feature/*` para nuevas funcionalidades, `fix/*` para correcciones
- Politica de commits: mensajes en formato **Conventional Commits** (`feat:`, `fix:`, `docs:`, `test:`, `ci:`, `chore:`)
- Pull Requests obligatorios para integrar a `main`
- Revisores asignados antes del merge
- Etiquetas (`tags`) para marcar versiones (`vX.Y.Z` segun SemVer)

### 2.3 Herramientas utilizadas

| Proposito | Herramienta |
|-----------|-------------|
| Lenguaje y framework | Python 3.14, Django 5.2 |
| Base de datos | SQLite |
| Control de versiones | Git 2.x |
| Hosting de repositorio | GitHub |
| Integracion continua | GitHub Actions |
| Gestion de dependencias | pip + requirements.txt |
| Entorno aislado | venv (modulo estandar de Python) |
| Pruebas | unittest (Django TestCase) |
| Empaquetado de entrega | GitHub Releases + tag SemVer |

## Conceptos teoricos asociados

### Administracion del cambio

Es el conjunto de practicas para registrar, evaluar e integrar las modificaciones que sufre un producto de software durante su ciclo de vida (Pressman, 2010). Sus elementos centrales son:

- **Identificacion** del elemento que cambia (un archivo, modulo, requerimiento)
- **Control** sobre como se aprueba el cambio (revision por pares, pull request)
- **Trazabilidad** del cambio hacia un requerimiento, defecto o solicitud
- **Auditoria** de las versiones afectadas

En el proyecto, cada Pull Request representa una solicitud de cambio formal, con descripcion, autor, revisor, archivos afectados y resultado de la integracion continua.

### Gestion de versiones

Sommerville (2011) define la gestion de configuracion del software (SCM) como la disciplina que controla la evolucion de los productos. La gestion de versiones es su componente mas visible y comprende:

- **Identificacion** unica de cada version (numero, tag, commit hash)
- **Almacenamiento** de cada version (repositorio Git)
- **Ramificacion y fusion** para trabajo paralelo
- **Etiquetado** de versiones liberadas (SemVer: MAJOR.MINOR.PATCH)

Se aplica el **versionado semantico**:
- `MAJOR` (X.0.0): cambios incompatibles
- `MINOR` (0.X.0): nuevas funcionalidades compatibles
- `PATCH` (0.0.X): correcciones compatibles

### Construccion del sistema

Es el proceso automatizado que transforma el codigo fuente en un artefacto ejecutable o desplegable. En proyectos Python/Django no hay un "compilado" tradicional, pero la construccion incluye:

- Instalacion de dependencias (`pip install -r requirements.txt`)
- Aplicacion de migraciones de base de datos
- Recoleccion de archivos estaticos (`collectstatic`)
- Ejecucion de pruebas automatizadas
- Verificacion de estilo (linting)
- Generacion del paquete distribuible (archivo `.zip`/`.tar.gz` o imagen Docker)

La **Integracion Continua (CI)** automatiza esto en cada push o pull request para detectar errores temprano.

### Gestion de entregas

Es el proceso por el cual una version del software pasa al usuario final. Comprende:

- **Versionado** (tag SemVer)
- **Changelog** documentando cambios respecto a la version anterior
- **Repositorio de artefactos** (GitHub Releases en este caso)
- **Notas de liberacion** dirigidas al usuario
- **Estrategia de despliegue** (blue/green, canary, rolling)

En este proyecto la entrega se simula como un **GitHub Release** con tag `v1.0.0`, archivo comprimido del codigo y CHANGELOG.md.

## Tabla resumen de hallazgos

| Concepto | Hallazgo en el proyecto | Herramienta aplicada | Sesion donde se demuestra |
|----------|-------------------------|----------------------|---------------------------|
| Administracion del cambio | Cada cambio se realiza en rama propia y se integra via PR | Git + GitHub PRs | Sesion 2 |
| Gestion de versiones | Historial lineal de commits con mensajes convencionales | Git + Conventional Commits | Sesion 2 |
| Construccion del sistema | Pipeline automatico instala dependencias, aplica migraciones y corre tests | GitHub Actions | Sesion 3 |
| Pruebas automatizadas | Bateria de pruebas unitarias y de integracion sobre el CRUD | Django TestCase | Sesion 3 |
| Gestion de entregas | Release etiquetado v1.0.0 con changelog y artefacto | GitHub Releases + SemVer | Sesion 4 |

## Referencias

1. PRESSMAN, R. S. (2010). *Ingenieria del Software: Un enfoque practico* (7ma ed.). McGraw-Hill.
2. SOMMERVILLE, I. (2011). *Ingenieria de Software* (9na ed.). Pearson Educacion.
