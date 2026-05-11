# Guia de Comandos Ejecutados y Capturas de Pantalla

Documento maestro de evidencias para las 4 sesiones del taller.
Cada bloque indica los comandos exactos ejecutados, su explicacion y la captura
que debe acompaniarlos.

---

## SESION 2 - Gestion de versiones y control de cambios

### Actividad 1 - Bloque A: Configuracion del repositorio

```powershell
# Crear estructura del proyecto Django
mkdir c:\ronny\talleres\PDLDTLA
cd c:\ronny\talleres\PDLDTLA
python -m venv venv
./venv/Scripts/python -m pip install Django
./venv/Scripts/python -m django startproject pdldtla .
./venv/Scripts/python manage.py startapp estudiantes

# Inicializar repositorio Git con rama principal 'main'
git init -b main

# Conectar repositorio local con remoto en GitHub
git remote add origin https://github.com/RonnyAreUneMi/PDLDTLA.git
git remote -v
```

| Comando | Explicacion |
|---------|-------------|
| `git init -b main` | Inicializa un repo nuevo con la rama por defecto llamada `main`. |
| `git remote add origin <url>` | Asocia el repo local con el remoto en GitHub bajo el alias `origin`. |
| `git remote -v` | Verifica que la URL del remoto se haya configurado correctamente. |

**CAPTURA 1:** Salida de `git remote -v` mostrando origin de fetch y push.

---

### Actividad 1 - Bloque B: Primer commit (linea base)

```powershell
git add .gitignore README.md requirements.txt manage.py pdldtla/ estudiantes/ docs/SESION1-analisis.md
git status --short

git commit -m "feat: proyecto base Django CRUD de estudiantes (Sesion 1)"

git log --oneline
```

| Comando | Explicacion |
|---------|-------------|
| `git add <archivos>` | Mueve los archivos al area de staging. |
| `git status --short` | Lista de forma compacta los archivos en staging y modificados. |
| `git commit -m "..."` | Crea un nuevo commit con el mensaje indicado. Se usa Conventional Commits. |
| `git log --oneline` | Lista los commits, uno por linea, con hash corto y mensaje. |

**CAPTURA 2:** Salida de `git status --short` antes del commit.
**CAPTURA 3:** Salida de `git log --oneline` despues del commit.

---

### Actividad 1 - Bloque C: Rama de funcionalidad (buscador)

```powershell
# Crear y cambiar a rama de feature
git checkout -b feature/buscador-estudiantes

# (edicion de archivos: views.py, list.html, tests.py)

# Verificar cambios pendientes
git status
git diff

# Stage y commit
git add -A
git commit -m "feat(estudiantes): agregar buscador por texto y filtro por carrera"

# Volver a main y fusionar via merge --no-ff (simula merge de PR)
git checkout main
git merge --no-ff feature/buscador-estudiantes -m "Merge PR #1: feat(estudiantes): buscador y filtro por carrera"
```

| Comando | Explicacion |
|---------|-------------|
| `git checkout -b <rama>` | Crea una nueva rama a partir de la actual y se cambia a ella. |
| `git diff` | Muestra los cambios linea por linea sobre el working tree. |
| `git add -A` | Agrega TODOS los cambios (nuevos, modificados, borrados) al staging. |
| `git checkout main` | Cambia a la rama principal. |
| `git merge --no-ff <rama>` | Fusiona la rama generando un commit explicito de merge, util para visualizar la integracion en el grafo. |

**CAPTURA 4:** Salida de `git diff` mostrando lineas verdes/rojas del cambio.
**CAPTURA 5:** Salida de `git log --oneline --graph --all` tras el merge.

---

### Actividad 1 - Bloque D: Rama de funcionalidad (validaciones)

```powershell
git checkout -b feature/validacion-cedula
# (edicion de forms.py y tests.py)
git add -A
git commit -m "feat(estudiantes): validacion estricta de cedula, semestre y correo"

git checkout main
git merge --no-ff feature/validacion-cedula -m "Merge PR #2: feat(estudiantes): validaciones de formulario"
```

### Actividad 1 - Bloque E: Rama de correccion (fix)

```powershell
git checkout -b fix/orden-listado
# (edicion de views.py y tests.py)
git add -A
git commit -m "fix(estudiantes): garantizar orden alfabetico apellido+nombre en listado"

git checkout main
git merge --no-ff fix/orden-listado -m "Merge PR #3: fix(estudiantes): orden alfabetico en listado"
```

### Actividad 1 - Bloque F: Rama CI

```powershell
git checkout -b ci/github-actions
# (creacion de .github/workflows/ci.yml y docs/SESION3-cicd.md)
git add -A
git commit -m "ci: agregar pipeline de GitHub Actions con build, tests y artefacto"

git checkout main
git merge --no-ff ci/github-actions -m "Merge PR #4: ci: integracion continua con GitHub Actions"
```

---

### Actividad 1 - Bloque G: Publicacion en GitHub

```powershell
# Subir rama main al remoto
git push -u origin main

# Subir todas las ramas adicionales como evidencia
git push origin feature/buscador-estudiantes
git push origin feature/validacion-cedula
git push origin fix/orden-listado
git push origin ci/github-actions
```

| Comando | Explicacion |
|---------|-------------|
| `git push -u origin <rama>` | Sube la rama al remoto y establece tracking (la `-u` solo se usa la primera vez). |

**CAPTURA 6:** Salida del `git push` mostrando "new branch" para cada rama.

---

### Actividad 2 - Politica de commits

Se adopto **Conventional Commits**:

```
<tipo>(<alcance opcional>): <descripcion corta>

<cuerpo opcional con detalles>
```

| Tipo | Uso | Ejemplo |
|------|-----|---------|
| `feat` | Nueva funcionalidad | `feat(estudiantes): agregar buscador` |
| `fix` | Correccion de error | `fix(estudiantes): orden alfabetico` |
| `docs` | Solo documentacion | `docs(sesion2): comandos git` |
| `test` | Agregar / corregir pruebas | `test: agregar prueba de buscador` |
| `ci` | Cambios en pipeline | `ci: agregar workflow de actions` |
| `chore` | Mantenimiento, deps | `chore: actualizar Django a 5.2` |
| `refactor` | Cambio interno sin alterar comportamiento | `refactor: extraer helper` |

### Reglas adicionales

1. Nunca commitear directo a `main` (todo entra por PR).
2. Una rama por unidad de trabajo, nunca mezclar features.
3. Commits pequenios y atomicos.
4. Mensaje en imperativo: "agregar X", no "agregado X".
5. Tests deben pasar antes del merge.
6. Merge con `--no-ff` para preservar el commit de merge.

---

### Comandos de evidencia (ejecutarlos ahora para capturar)

```powershell
cd c:\ronny\talleres\PDLDTLA

# 1. Configuracion del remoto
git remote -v

# 2. Lista de ramas locales y remotas
git branch -a

# 3. Historial grafico completo
git log --oneline --graph --all --decorate

# 4. Estado limpio
git status

# 5. Lista de tags
git tag -n5
```

**CAPTURA 7:** Salida completa de los 5 comandos anteriores ejecutados en PowerShell.

---

### Capturas a tomar en GitHub (web)

Abre cada URL con sesion iniciada y captura:

| # | Captura | URL |
|---|---------|-----|
| C1 | Pagina principal del repo con README renderizado | https://github.com/RonnyAreUneMi/PDLDTLA |
| C2 | Lista de ramas activas | https://github.com/RonnyAreUneMi/PDLDTLA/branches |
| C3 | Grafo de red mostrando ramas y merges | https://github.com/RonnyAreUneMi/PDLDTLA/network |
| C4 | Historial de commits en main | https://github.com/RonnyAreUneMi/PDLDTLA/commits/main |
| C5 | Detalle del commit del buscador | https://github.com/RonnyAreUneMi/PDLDTLA/commit/f3761e2 |
| C6 | Comparacion main vs feature/buscador-estudiantes | https://github.com/RonnyAreUneMi/PDLDTLA/compare/main...feature/buscador-estudiantes |
| C7 | Comparacion main vs feature/validacion-cedula | https://github.com/RonnyAreUneMi/PDLDTLA/compare/main...feature/validacion-cedula |
| C8 | Comparacion main vs fix/orden-listado | https://github.com/RonnyAreUneMi/PDLDTLA/compare/main...fix/orden-listado |
| C9 | Repositorio "linea base" sin cambios | https://github.com/RonnyAreUneMi/TallerOriginal |

---

## SESION 3 - Construccion e integracion del sistema (CI)

### Actividad 1 + 2 - Pipeline en GitHub Actions

**Archivo del pipeline:** [`.github/workflows/ci.yml`](../.github/workflows/ci.yml)

```yaml
name: CI - Build & Test
on:
  push:
    branches: [main, develop, "feature/**", "fix/**"]
  pull_request:
    branches: [main]
  workflow_dispatch:
```

### Estructura del pipeline

| Job | Pasos | Cuando se ejecuta |
|-----|-------|-------------------|
| `build-test` | checkout, setup Python 3.11/3.12, pip install, flake8, migrate, test con coverage, upload coverage.xml | En cada push y PR |
| `build-artifact` | checkout, empaqueta .zip, sube artefacto | Solo en push a `main` |

### Comandos locales para verificacion previa

```powershell
cd c:\ronny\talleres\PDLDTLA

# Aplicar migraciones
./venv/Scripts/python manage.py migrate

# Ejecutar la suite completa
./venv/Scripts/python manage.py test estudiantes -v 2

# Con cobertura
./venv/Scripts/python -m pip install coverage
./venv/Scripts/python -m coverage run --source='estudiantes' manage.py test
./venv/Scripts/python -m coverage report
```

**CAPTURA 8:** Salida de `manage.py test -v 2` mostrando `Ran 15 tests OK`.
**CAPTURA 9:** Salida de `coverage report` con porcentaje por archivo.

---

### Capturas a tomar en GitHub (web)

| # | Captura | URL |
|---|---------|-----|
| C10 | Pestania Actions con lista de workflows | https://github.com/RonnyAreUneMi/PDLDTLA/actions |
| C11 | Detalle de una ejecucion exitosa con pasos | https://github.com/RonnyAreUneMi/PDLDTLA/actions (clic en cualquier run) |
| C12 | Vista del YAML del workflow | https://github.com/RonnyAreUneMi/PDLDTLA/blob/main/.github/workflows/ci.yml |
| C13 | Artefactos descargables de la ejecucion (coverage.xml, .zip) | dentro del detalle del workflow, seccion "Artifacts" |
| C14 | Diagrama Mermaid renderizado | https://github.com/RonnyAreUneMi/PDLDTLA/blob/main/docs/SESION3-cicd.md |

---

## SESION 4 - Entrega simulada del producto

### Actividad 1 - Comandos ejecutados para la release

```powershell
cd c:\ronny\talleres\PDLDTLA

# 1. Verificar que main esta limpio
git status
git log --oneline | head -3

# 2. Crear tag anotado v1.0.0
git tag -a v1.0.0 -m "Release v1.0.0: primera version estable"

# 3. Verificar el tag
git tag -n5

# 4. Publicar el tag en GitHub
git push origin v1.0.0
```

| Comando | Explicacion |
|---------|-------------|
| `git tag -a <nombre> -m "..."` | Crea un tag anotado (con metadata: autor, fecha, mensaje). El tag marca un punto especifico del historial como "version liberada". |
| `git tag -n5` | Lista los tags con las primeras 5 lineas del mensaje. |
| `git push origin <tag>` | Sube el tag al remoto. Sin esto el tag solo existe localmente. |

**CAPTURA 15:** Salida de `git tag -n5` mostrando v1.0.0 con su mensaje.
**CAPTURA 16:** Salida del `git push origin v1.0.0`.

---

### Pasos para crear el Release en GitHub (web)

1. Abrir https://github.com/RonnyAreUneMi/PDLDTLA/releases/new
2. En **"Choose a tag"** seleccionar `v1.0.0` (ya existe en el remoto).
3. **Release title:** `PDLDTLA v1.0.0 - Primera version estable`
4. **Description:** copiar el contenido de [CHANGELOG.md](../CHANGELOG.md).
5. (Opcional) Adjuntar archivos:
   - Descargar el .zip del pipeline desde la pestania Actions → ultimo workflow → Artifacts.
   - O generar local:
     ```powershell
     Compress-Archive -Path *.py, manage.py, requirements.txt, README.md, CHANGELOG.md, estudiantes, pdldtla, docs, .github -DestinationPath pdldtla-v1.0.0.zip
     ```
6. Marcar como **"Latest release"**.
7. Clic en **"Publish release"**.

**CAPTURA 17:** Pagina del Release publicado con su .zip adjunto.

---

### Generar archivo comprimido localmente

```powershell
cd c:\ronny\talleres\PDLDTLA

Compress-Archive `
  -Path manage.py, requirements.txt, README.md, CHANGELOG.md, estudiantes, pdldtla, docs, .github, .gitignore `
  -DestinationPath pdldtla-v1.0.0.zip

# Verificar
Get-Item pdldtla-v1.0.0.zip | Select-Object Name, Length
```

**CAPTURA 18:** Listado del directorio mostrando el `pdldtla-v1.0.0.zip` generado.

---

### Capturas a tomar en GitHub (web)

| # | Captura | URL |
|---|---------|-----|
| C19 | Pagina de Releases con v1.0.0 publicado | https://github.com/RonnyAreUneMi/PDLDTLA/releases |
| C20 | Detalle del release con changelog y .zip adjunto | https://github.com/RonnyAreUneMi/PDLDTLA/releases/tag/v1.0.0 |
| C21 | Pagina de Tags | https://github.com/RonnyAreUneMi/PDLDTLA/tags |
| C22 | CHANGELOG.md renderizado | https://github.com/RonnyAreUneMi/PDLDTLA/blob/main/CHANGELOG.md |

---

### Actividad 2 - Informe final

El informe esta en [docs/INFORME-FINAL.md](INFORME-FINAL.md) e integra:

| Seccion requerida | Donde se aborda |
|-------------------|-----------------|
| Analisis del control de cambios y versiones | Seccion 2 del informe |
| Capturas de CI/CD | Seccion 3 (insertar capturas C10-C14) |
| Evidencia de entregables | Seccion 4 (insertar capturas C19-C22) |
| Lecciones aprendidas | Seccion 5 |

---

## Resumen de comandos Git por categoria

### Inspeccion (lectura, no modifican nada)

```powershell
git status
git log --oneline --graph --all --decorate
git diff
git diff --cached
git branch -a
git remote -v
git tag -n5
git show <hash>
```

### Modificacion local

```powershell
git add <archivo>
git add -A
git commit -m "tipo(alcance): descripcion"
git checkout <rama>
git checkout -b <rama-nueva>
git merge --no-ff <rama>
git branch -d <rama>
```

### Sincronizacion con remoto

```powershell
git push -u origin <rama>
git push origin <rama>
git push origin <tag>
git pull origin <rama>
git fetch origin
```

### Etiquetado (versiones)

```powershell
git tag -a v1.0.0 -m "Release v1.0.0"
git tag -n5
git push origin v1.0.0
git push origin --tags
```

---

## Checklist final de entrega

- [ ] Capturas C1 a C9 pegadas en el informe (Sesion 2)
- [ ] Capturas C10 a C14 pegadas en el informe (Sesion 3)
- [ ] Capturas C15 a C22 pegadas en el informe (Sesion 4)
- [ ] Release v1.0.0 publicado en GitHub con .zip y changelog
- [ ] Informe final con todas las secciones completas
- [ ] Subir el informe al aula virtual
