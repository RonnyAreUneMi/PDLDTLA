# Sesion 2 - Gestion de versiones y control de cambios

## Actividad 1: Repositorio en GitHub y simulacion de control de versiones

### Repositorio configurado

**URL:** https://github.com/RonnyAreUneMi/PDLDTLA.git

### Estrategia de ramificacion (GitHub Flow)

```
main  (rama protegida, siempre desplegable)
  |
  +-- feature/buscador-estudiantes  (nueva funcionalidad)
  +-- feature/validacion-cedula     (nueva funcionalidad)
  +-- fix/orden-listado             (correccion)
```

### Ramas creadas en el proyecto

| Rama | Tipo | Proposito | Pull Request |
|------|------|-----------|--------------|
| `feature/buscador-estudiantes` | Funcionalidad | Buscador por texto y filtro por carrera | PR #1 |
| `feature/validacion-cedula`    | Funcionalidad | Validaciones de cedula, semestre y correo | PR #2 |
| `fix/orden-listado`            | Correccion | Orden alfabetico estable en listado | PR #3 |

### Politica de commits adoptada

Se usa el formato **Conventional Commits**:

```
<tipo>(<alcance opcional>): <descripcion corta>

<cuerpo opcional con detalles>
```

Tipos permitidos:
- `feat`: nueva funcionalidad
- `fix`: correccion de error
- `docs`: cambios solo en documentacion
- `test`: agregar o corregir pruebas
- `ci`: cambios en pipeline o configuracion de CI
- `chore`: tareas de mantenimiento (deps, build tools)
- `refactor`: cambios internos sin alterar comportamiento

### Reglas adicionales

1. **Nunca commitear directo a `main`**: todo cambio entra por Pull Request.
2. **Una rama por unidad de trabajo**: no mezclar features ni fixes.
3. **Commit pequeno y atomico**: cada commit debe poder describirse en una linea.
4. **Mensaje en imperativo**: "agregar X" no "agregado X".
5. **Tests deben pasar antes del merge**: el pipeline CI bloquea el merge si falla.
6. **Merge con `--no-ff`**: preserva el commit de merge para visualizar la integracion de la rama.

## Actividad 2: Comandos Git utilizados y evidencias

### Configuracion inicial

```bash
# Inicializar repositorio local con rama por defecto 'main'
git init -b main

# Conectar con el repositorio remoto en GitHub
git remote add origin https://github.com/RonnyAreUneMi/PDLDTLA.git

# Verificar remoto
git remote -v
```

### Flujo de trabajo por rama

```bash
# 1. Crear rama desde main
git checkout main
git pull origin main           # asegurar que main esta al dia
git checkout -b feature/buscador-estudiantes

# 2. Hacer cambios en codigo, agregar al stage
git status                     # ver archivos modificados
git add .                      # incluir todos los cambios
git diff --cached              # revisar lo que se va a commitear

# 3. Commit con mensaje convencional
git commit -m "feat(estudiantes): agregar buscador por texto y filtro por carrera"

# 4. Publicar la rama en GitHub
git push -u origin feature/buscador-estudiantes

# 5. Crear Pull Request (interfaz web de GitHub)
#    Titulo: feat(estudiantes): buscador y filtro por carrera
#    Reviewers: asignar al menos uno
#    Esperar a que el pipeline CI pase

# 6. Una vez aprobado el PR, mergear a main
git checkout main
git pull origin main
git merge --no-ff feature/buscador-estudiantes -m "Merge PR #1: ..."
git push origin main

# 7. Eliminar la rama local (opcional)
git branch -d feature/buscador-estudiantes
```

### Comandos clave usados en este proyecto

| Comando | Proposito |
|---------|-----------|
| `git init -b main` | Inicializar repo con rama principal `main` |
| `git remote add origin <url>` | Vincular repositorio local con GitHub |
| `git remote -v` | Listar remotos configurados |
| `git status` | Ver estado del working directory |
| `git add <archivos>` | Mover cambios al staging area |
| `git diff` | Ver cambios sin staging |
| `git diff --cached` | Ver cambios en staging |
| `git commit -m "..."` | Confirmar cambios |
| `git checkout -b <rama>` | Crear y cambiar a rama nueva |
| `git checkout <rama>` | Cambiar de rama |
| `git merge --no-ff <rama>` | Fusionar preservando el commit de merge |
| `git log --oneline --graph --all` | Visualizar historial grafico |
| `git push -u origin <rama>` | Subir rama y enlazarla con remoto |
| `git pull` | Traer cambios del remoto |
| `git branch -d <rama>` | Borrar rama local ya fusionada |
| `git tag -a vX.Y.Z -m "..."` | Crear etiqueta anotada |
| `git push origin --tags` | Subir etiquetas al remoto |

### Historial de commits del proyecto

```
*   Merge PR #3: fix(estudiantes): orden alfabetico en listado
|\
| * fix(estudiantes): garantizar orden alfabetico apellido+nombre en listado
|/
*   Merge PR #2: feat(estudiantes): validaciones de formulario
|\
| * feat(estudiantes): validacion estricta de cedula, semestre y correo
|/
*   Merge PR #1: feat(estudiantes): buscador y filtro por carrera
|\
| * feat(estudiantes): agregar buscador por texto y filtro por carrera
|/
* feat: proyecto base Django CRUD de estudiantes (Sesion 1)
```

## Producto: Evidencias

### Pull Requests simulados

> Al ejecutar el push a GitHub, las ramas `feature/buscador-estudiantes`, `feature/validacion-cedula` y `fix/orden-listado` quedan disponibles para abrir los PRs reales desde la interfaz web. El historial local ya refleja los 3 merges con `--no-ff` simulando la integracion por PR.

### Capturas (a tomar tras el push)

1. **Vista del grafo de commits en GitHub** (`Insights > Network`)
2. **Listado de ramas activas** (`branches`)
3. **Detalle de uno de los Pull Requests** (commits, archivos cambiados, comentarios)
4. **Resultado del pipeline CI ejecutandose sobre la rama** (verde)

## Reflexion

La estrategia GitHub Flow demostro ser adecuada para un equipo pequeno: cada cambio se aisla en su rama, el revisor puede inspeccionar diff y resultado de tests sin descargar el codigo, y `main` permanece estable. El uso de Conventional Commits agrego trazabilidad: solo leyendo el historial se entiende que se hizo en cada iteracion (`feat` para nuevas funcionalidades, `fix` para correcciones).
