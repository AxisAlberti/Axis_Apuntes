# Repositorio de apuntes (MkDocs)

Este repositorio contiene los materiales de los modulos de:

- Montaje y Mantenimiento de Equipos Informaticos
- Sistemas Informaticos

## Estructura

- `docs/` → contenido fuente (Markdown + assets)
- `mkdocs.yml` → configuracion del sitio
- `site/` → salida generada (no se sube)

## Uso local

- Construir: `mkdocs build`
- Servir: `mkdocs serve`

## Publicacion en GitHub Pages

El workflow en `.github/workflows/mkdocs.yml` despliega automaticamente el sitio
con cada push a `main` usando `mkdocs gh-deploy`.

Recomendado: mantener `site/` en `.gitignore`.
