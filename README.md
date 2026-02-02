

Repositorio de material educativo para formacion profesional en sistemas informaticos y montaje y mantenimiento de equipos, publicado con MkDocs Material.

Este repositorio contiene documentacion, practicas, cuestionarios tipo GIFT, recursos y contenidos complementarios organizados por modulos tematicos.

## 📚 Modulos Disponibles

### 🛠️ Montaje y Mantenimiento (section1)
Contenido orientado a hardware, arquitectura de computadores y montaje de equipos.
- **U00**: Sistemas de numeracion
- **U01**: Introduccion a los sistemas informaticos
- **U02**: Componentes internos del PC
- **U03**: Chipset
- **U04**: Conexiones externas
- **U05**: Memoria RAM
- **U06**: CMOS y UEFI
- **U07**: Almacenamiento
- **U08**: Microprocesadores
- **U09**: Tarjetas graficas
- **U10**: Mantenimiento de equipos informaticos
- **A1**: Arquitecturas de procesadores (Anexo)
- **A2**: Procesos e hilos (Anexo)
- **A3**: Prevencion de riesgos laborales (Anexo)
- **A4**: Guia para elegir procesador (Anexo)
- **A5**: Nomenclatura de procesadores (Anexo)
- **A6**: BIOS, UEFI y proceso de encendido (Anexo)
- **A7**: Intel vs AMD (Anexo)

### 💻 Sistemas Informaticos (section2)
Contenido base sobre redes, terminal y fundamentos de sistemas.
- **U01**: Redes
- **U02**: Terminal

## 📁 Estructura del Repositorio

```text
├── docs/                          # Documentacion principal (MkDocs)
│   ├── assets/                    # Recursos globales (imagenes, iconos)
│   ├── includes/                  # Snippets y abreviaturas compartidas
│   ├── stylesheets/               # Estilos personalizados
│   ├── section1/                  # Montaje y mantenimiento
│   │   ├── u00/                   # Unidades didacticas
│   │   │   ├── index.md           # Descripcion de la unidad
│   │   │   ├── teoria/            # Contenidos teoricos
│   │   │   ├── practica/          # Practicas y ejercicios
│   │   │   └── gift/              # Preguntas para cuestionarios
│   │   ├── A1/                    # Anexos (antiguas u09..u13)
│   │   │   ├── index.md
│   │   │   ├── teoria/
│   │   │   ├── practica/
│   │   │   └── gift/
│   │   ├── slides/                # Slides del modulo (si aplica)
│   │   └── ...
│   ├── section2/                  # Sistemas informaticos
│   │   ├── u01/
│   │   │   ├── index.md
│   │   │   ├── teoria/
│   │   │   ├── practicas/
│   │   │   └── gift/
│   │   ├── slides/                # Slides del modulo (si aplica)
│   │   └── ...
│   ├── index.md                   # Pagina principal
│   ├── blog.md                    # Indice del blog
│   ├── tags.md                    # Pagina de etiquetas
│   └── about.md                   # Acerca de
├── .github/
│   └── workflows/                 # CI/CD (deploy de MkDocs)
├── mkdocs.yml                     # Configuracion de MkDocs Material
├── site/                          # Sitio generado (salida de build)
├── AGENTS.md                      # Guia para agentes/contribuidores
└── README.md                      # Este archivo
```

## 🎯 Como Usar el Contenido

### Instalacion rapida
```bash
python -m pip install --upgrade pip
pip install mkdocs-material
pip install mkdocs-blogging-plugin
```

### Documentacion
1. La documentacion principal esta en `/docs/`
2. Se genera automaticamente con MkDocs
3. Cada modulo tiene unidades didacticas con teoria, practica y cuestionarios
4. Los anexos de `section1` estan en carpetas `A1..A5`

### Sitio generado
1. El resultado de `mkdocs build` se genera en `/site/`
2. Normalmente no es necesario editar `/site/` manualmente

### Contenido por modulo
- **Teoria**: Contenidos conceptuales y explicaciones
- **Practica/Practicas**: Ejercicios y actividades evaluables
- **GIFT**: Preguntas para cuestionarios autoevaluables
- **Recursos**: Material complementario por modulo
- **Nota**: Practicas y GIFT no se muestran en el menu lateral
- **Slides**: Material de presentaciones en carpetas `slides/` (Markdown y/o HTML Reveal.js)
- **Slides sin disponibilidad**:
  - `docs/section1/slides/no-disponible.md`
  - `docs/section2/slides/no-disponible.md`

### Categorias Moodle
- Generadas en `scripts/SMR-categorias.gift` con `scripts/update_categories.py`

### Branding y recursos globales
- **Logo**: `docs/assets/logo.png`
- **Favicon**: `docs/assets/favicon.ico`

## 🤝 Como Contribuir

### Requisitos Previos
- Python 3.10+ (recomendado)
- MkDocs y tema Material instalados
- Conocimientos basicos de Git y Markdown

### Proceso de Contribucion

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/TU_USUARIO/Axis_Apuntes.git
   cd Axis_Apuntes
   ```

2. **Crear una rama para tus cambios**
   ```bash
   git checkout -b feature/nuevo-contenido
   # o
   git checkout -b fix/correccion-contenido
   ```

3. **Realizar cambios siguiendo la estructura**
   - Documentacion: `/docs/sectionX/uXX/teoria/` o `/practica(s)/`
   - Cuestionarios: `/docs/sectionX/uXX/gift/`
   - Snippets/abreviaturas: `/docs/includes/`
   - Estilos: `/docs/stylesheets/`

4. **Convenciones de nomenclatura**
   - **Teoria**: `MM-UXX.Y.-Tema.md` o `SI-UXX.Y.-Tema.md`
   - **Teoria anexos**: `A1-1-...`, `A2-1-...`, etc.
   - **Practicas**: `MM-UXX.-PracticaYYY.md` o `SI-UXX.-PracticaYYY.md`
   - **Cuestionarios**: `MM-UXX.Y.-Tema.gift` o `SI-UXX.Y.-Tema.gift`

5. **Validar cambios**
   ```bash
   # Servidor local con recarga
   mkdocs serve

   # Build completo del sitio
   mkdocs build
   ```

6. **Commit y push**
   ```bash
   git add .
   git commit -m "Describe claramente el cambio realizado"
   git push origin feature/nuevo-contenido
   ```

7. **Crear Pull Request**
   - Ve a GitHub y crea un PR desde tu rama
   - Describe que cambiaste y por que
   - Espera revision y feedback

### Tipos de Contribuciones

- ✅ Correcciones: errores tipograficos, enlaces rotos
- ✅ Mejoras: claridad, estructura, ejemplos adicionales
- ✅ Nuevo contenido: teoria, practicas, cuestionarios
- ✅ Actualizaciones: tecnologias, procesos, mejores practicas
- ✅ Recursos: material complementario por unidad/modulo

### Guias de Estilo

- Markdown claro, consistente y bien estructurado
- Titulos y nombres de archivos coherentes con el modulo
- Ejemplos tecnicos verificables cuando aplique
- Recursos y enlaces revisados antes de publicar

### Contacto

Para preguntas o sugerencias:
- Crear un Issue en GitHub
- Revisar `AGENTS.md` para guias detalladas de colaboracion

**Fecha de actualización:** 02/02/2026
