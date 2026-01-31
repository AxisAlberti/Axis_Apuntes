# Guía del Repositorio para Agentes

Este repositorio contiene material educativo para módulos de formación profesional. La documentación está dirigida a **alumnado** y debe ser **didáctica, clara y pedagógica**.

## Normas de redacción de apuntes

- Los apuntes deben ser claros, didácticos y orientados al aprendizaje del alumnado.
- Cada vez que se edite un fichero `.md`, se añadirá al final una línea con la fecha de actualización, con el formato: `**Fecha de actualización:** 31/01/2026`.

## Formato recomendado para apuntes

- Título principal con el nombre de la unidad y tema
- Objetivos de aprendizaje (3-5 puntos)
- Desarrollo del contenido con subsecciones claras
- Ejemplos prácticos o casos reales
- Resumen final en 3-5 ideas clave
- Referencias y enlaces (si aplica)

## 1. Estructura del repositorio

### 1.1. Carpeta `docs/`

Contiene la documentación principal en formato MkDocs Material. Está organizada por módulos:

- **section1**: Montaje y Mantenimiento de Equipos Informáticos
- **section2**: Sistemas Informáticos

#### Estructura general por módulo

```
docs/
├── index.md                     # Portada general del sitio
├── section1/                    # Montaje y Mantenimiento
│   ├── index.md                 # Portada del módulo
│   ├── recursos/                # Recursos del módulo
│   ├── u00..u08/                # Unidades didácticas
│   └── A1..A5/                  # Anexos (antiguas u09..u13)
├── section2/                    # Sistemas Informáticos
│   ├── index.md
│   ├── recursos/
│   └── u01..u02/
├── section1/slides/             # Slides del módulo (si aplica)
├── section2/slides/             # Slides del módulo (si aplica)
├── assets/                      # Recursos globales (logo, favicon, imágenes)
├── stylesheets/                 # CSS personalizado
├── includes/                    # Snippets y abreviaturas
├── blog.md
├── tags.md
└── about.md
```

#### Estructura típica de una unidad

```
sectionX/uXX/
├── index.md                     # Resumen y acceso a teoría
├── teoria/                      # Contenidos teóricos
│   ├── MODULO-UX.Y.-Tema.md
│   └── assets/                  # Imágenes y multimedia del tema
├── practica/                    # Prácticas (singular en section1)
└── gift/                        # Cuestionarios (GIFT)
└── slides/                      # Slides de la unidad (Markdown)
```

**Nota:** en `section2` la carpeta de prácticas se llama `practicas/` (plural).

### 1.2. Carpeta `site/`

Salida generada del sitio MkDocs. No editar manualmente.

## 2. Navegación y visibilidad

- La navegación se define en `mkdocs.yml`.
- **Prácticas y GIFT no aparecen en el menú lateral.**
- Los `.gift` están excluidos del build mediante:
  - `exclude_docs: "**/*.gift"`

## 3. Convenciones y formatos

### 3.0. Slides (Markdown y HTML)

- Cada módulo y cada unidad/anexo tiene carpeta `slides/`.
  - Módulo: `docs/sectionX/slides/`
  - Unidad: `docs/sectionX/uXX/slides/` o `docs/section1/A#//slides/`
- Las slides se pueden publicar como:
  - **Markdown** (borradores internos)
  - **HTML Reveal.js** para visualización en navegador
- En Markdown, usar separadores `---` por diapositiva y notas con `Note:`.
- En HTML Reveal.js, incluir `<aside class="notes">...</aside>` para notas.
- En HTML Reveal.js, incluir:
  - Logo arriba a la izquierda (usar `docs/assets/logo.png`)
  - Botón de retorno al módulo o repositorio
- Ejemplo básico (Markdown):

```md
---
marp: true
paginate: true
---

# Título

Note: Mensaje para el docente.
```

- Cuando se añadan slides nuevas, enlazarlas desde:
  - `docs/index.md` (sección Slides)
  - `docs/sectionX/index.md` (sección Slides del módulo)
  - `docs/sectionX/uXX/index.md` o `docs/section1/A#/index.md` si aplica
- Si una unidad no tiene presentación, enlazar a:
  - `docs/section1/slides/no-disponible.md` (section1)
  - `docs/section2/slides/no-disponible.md` (section2)

### 3.1. Rutas de imágenes

- Usar rutas **relativas** en los `.md`.
- Para imágenes locales, el patrón correcto es:
  - `../assets/...` (desde un archivo de teoría dentro de `teoria/`)

### 3.2. Nomenclatura de anexos

Los antiguos `u09..u13` de section1 se renombraron a **A1..A5**:

- `A1` → Arquitecturas de procesadores
- `A2` → Procesos e hilos
- `A3` → Prevención de riesgos laborales
- `A4` → Guía para elegir procesador
- `A5` → Nomenclatura de procesadores

Los ficheros de teoría siguen el formato:

- `A1-1-Arquitecturas-de-procesadores.md`
- `A2-1-Procesos-e-hilos.md`
- `A3-1-Prevencion-de-riesgos-laborales.md`
- `A4-1-Guia-para-elegir-procesador.md`
- `A5-1-Nomenclatura-de-procesadores.md`

### 3.3. Categorías

- Section1 usa categoría `MON`
- Section2 usa categoría `SIS`
- Anexos usan categoría `ANE`

## 4. Recursos y branding

- Favicon: `docs/assets/favicon.ico`
- Logo: `docs/assets/logo.png`
- Logo principal en portada: `docs/index.md` (imagen centrada)

## 5. Comandos útiles

```bash
mkdocs serve
mkdocs build
mkdocs gh-deploy --force
```

Ejemplo básico (Reveal.js HTML):

```html
<section>
  <h2>Título</h2>
  <aside class="notes">Notas para el docente.</aside>
</section>
```

## 6. Publicación

- GitHub Pages publica desde la rama `gh-pages`.
- El despliegue se realiza con `mkdocs gh-deploy --force`.

## 7. Preguntas tipo test con penalización (formato GIFT)

Las preguntas tipo test para cuestionarios se generarán en **formato GIFT** de Moodle, con **una única respuesta correcta y varias incorrectas con penalización**.

### 7.0. Fuentes para generar preguntas

- Las preguntas deben basarse en los apuntes indicados.
- Complementar siempre con información actualizada de Internet.

### 7.1. Estructura básica de la pregunta

Cada pregunta seguirá esta estructura:

```gift
::Texto corto identificador de la pregunta::
Texto de la pregunta, lo más descriptiva posible. Puede plantear una situación práctica
relacionada con el contenido del archivo de teoría al que acompaña. {

=Respuesta correcta #Feedback formativo: explica por qué es correcta.
~%-33.3333%Respuesta incorrecta 1 #Feedback formativo: explica por qué NO es correcta.
~%-33.3333%Respuesta incorrecta 2 #Feedback formativo: explica por qué NO es correcta.
~%-33.3333%Respuesta incorrecta 3 #Feedback formativo: explica por qué NO es correcta.
}
```

### 7.2. Categorías Moodle (GIFT)

- El fichero de categorías está en:
  - `scripts/SMR-categorias.gift`
- Al generar cuestionarios, la **primera línea** del fichero debe ser la categoría correspondiente:

```gift
$CATEGORY: SMR/Section1/Nombre_de_la_unidad/Basico
```

El nombre de la unidad en la categoría debe estar **normalizado**:

- Sin tildes ni caracteres especiales
- Espacios reemplazados por `_`
- Solo letras, números, `_` y `-`

Para actualizar automáticamente el fichero de categorías tras añadir o renombrar unidades/anexos:

```bash
scripts/update_categories.py
```

## 8. Preguntas tipo ensayo con editor HTML (formato GIFT Moodle)

Las preguntas de **tipo ensayo** con editor HTML en Moodle se representan en GIFT siguiendo este patrón:

```gift
$CATEGORY: RUTA/CATEGORIA

// question: ID_INTERNO  name: TÍTULO_VISIBLE_EN_MOODLE
::TITULO_INTERNO::[html]ENUNCIADO_EN_HTML{}
```
