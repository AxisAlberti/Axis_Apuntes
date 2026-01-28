# Guía del Repositorio para Agentes

Este repositorio contiene material educativo para módulos de formación profesional. La documentación está dirigida a **alumnado** y debe ser **didáctica, clara y pedagógica**.

## Normas de redacción de apuntes

- Los apuntes deben ser claros, didácticos y orientados al aprendizaje del alumnado.

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
- Logo: `docs/assets/axis.png`
- Logo principal en portada: `docs/index.md` (imagen centrada)

## 5. Comandos útiles

```bash
mkdocs serve
mkdocs build
mkdocs gh-deploy --force
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
  - `docs/section1/gift/SMR-categorias.gift`
- Al generar cuestionarios, la **primera línea** del fichero debe ser la categoría correspondiente:

```gift
$CATEGORY: SMR/Section1/Nombre de la unidad/Basico
```

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
