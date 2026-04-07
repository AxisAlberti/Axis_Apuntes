---
title: "UD 03 - P1: Docker con Apache y carpeta compartida"
description: "Practica guiada para publicar una web con Apache en Docker usando una carpeta local compartida"
summary: "Despliegue de Apache en contenedor con contenido persistente desde el sistema anfitrion"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2026-04-07
icon: "material/file-document-edit"
permalink: /si/u03/p1
categories:
    - "SIS"
tags:
    - "practica"
    - "docker"
    - "apache"
    - "volumenes"
---

## Objetivo

Desplegar un servidor web Apache dentro de un contenedor Docker y conectarlo con una carpeta del sistema local para que los archivos web guardados en esa carpeta aparezcan publicados en el servidor.

## Que vas a practicar

- Crear una carpeta local para contenido web.
- Descargar y ejecutar una imagen con Apache.
- Montar una carpeta del sistema anfitrion dentro del contenedor.
- Verificar que los cambios en los archivos locales se reflejan en el servidor web.

## Requisitos

- Docker funcionando correctamente.
- Terminal disponible.
- Navegador web.

## Concepto clave

En esta practica no vamos a copiar la web dentro de la imagen, sino a **montar una carpeta del equipo anfitrion dentro del contenedor**.

Eso significa que:

- Los archivos HTML se editan en tu ordenador.
- Apache los lee desde esa carpeta compartida.
- Al modificar los archivos locales, el servidor muestra los cambios.

## 1. Crear la carpeta local del proyecto

Elige una carpeta del sistema anfitrion donde guardar la web.

### En Linux

```bash
mkdir -p ~/docker/apache-web
cd ~/docker/apache-web
```

### En Windows PowerShell

```powershell
mkdir $HOME\docker\apache-web
cd $HOME\docker\apache-web
```

## 2. Crear una pagina web de prueba

Crea un archivo `index.html` dentro de esa carpeta.

### En Linux

```bash
cat > index.html <<'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi web en Docker</title>
</head>
<body>
    <h1>Apache en Docker</h1>
    <p>Esta pagina se sirve desde una carpeta local compartida.</p>
</body>
</html>
EOF
```

### En Windows PowerShell

```powershell
@'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi web en Docker</title>
</head>
<body>
    <h1>Apache en Docker</h1>
    <p>Esta pagina se sirve desde una carpeta local compartida.</p>
</body>
</html>
'@ | Set-Content index.html
```

## 3. Descargar la imagen de Apache

Usaremos la imagen oficial `httpd`.

```bash
docker pull httpd:latest
```

## 4. Ejecutar el contenedor con carpeta compartida

Ahora vamos a arrancar Apache conectando la carpeta local con la carpeta web del contenedor.

### En Linux

```bash
docker run -d \
  --name apache_practica \
  -p 8080:80 \
  -v ~/docker/apache-web:/usr/local/apache2/htdocs/ \
  httpd:latest
```

### En Windows PowerShell

```powershell
docker run -d `
  --name apache_practica `
  -p 8080:80 `
  -v ${HOME}\docker\apache-web:/usr/local/apache2/htdocs/ `
  httpd:latest
```

### Explicacion del comando

- `-d`: ejecuta el contenedor en segundo plano.
- `--name apache_practica`: asigna un nombre al contenedor.
- `-p 8080:80`: publica Apache en el puerto `8080` del equipo.
- `-v ruta_local:/usr/local/apache2/htdocs/`: monta la carpeta local dentro del directorio web de Apache.
- `httpd:latest`: indica la imagen utilizada.

## 5. Comprobar que Apache funciona

Verifica que el contenedor esta en ejecucion:

```bash
docker ps
```

Despues abre en el navegador:

```text
http://localhost:8080
```

Debe aparecer la pagina creada en `index.html`.

## 6. Modificar el contenido web desde la carpeta local

Edita `index.html` y cambia el texto.

Ejemplo:

```html
<h1>Apache en Docker funcionando</h1>
<p>He cambiado este contenido desde la carpeta local.</p>
```

Guarda el archivo y recarga el navegador.

### Resultado esperado

Los cambios deben aparecer sin reconstruir la imagen y sin copiar archivos manualmente al contenedor.

Esto demuestra que Apache esta leyendo los archivos directamente desde la carpeta compartida del sistema anfitrion.

## 7. Comprobar el montaje dentro del contenedor

Puedes entrar al contenedor y listar el directorio web:

```bash
docker exec -it apache_practica bash
ls -l /usr/local/apache2/htdocs/
cat /usr/local/apache2/htdocs/index.html
exit
```

## 8. Detener y eliminar el contenedor

Cuando termines:

```bash
docker stop apache_practica
docker rm apache_practica
```

La carpeta local y su contenido seguiran existiendo en tu equipo.

## 9. Cuestiones para reflexionar

1. ¿Que ventaja tiene montar una carpeta local en lugar de copiar los archivos dentro del contenedor?
2. ¿Que diferencia hay entre borrar el contenedor y borrar la carpeta local?
3. ¿Por que este sistema resulta util durante el desarrollo web?
4. ¿Que ocurriria si cambias el puerto publicado a `-p 9090:80`?

## 10. Ampliacion opcional

Como ampliacion, puedes probar estas mejoras:

- Añadir una hoja de estilos CSS a la carpeta local.
- Crear una segunda pagina HTML.
- Montar una carpeta distinta.
- Repetir la practica usando `docker compose`.

## 11. Idea final

Esta practica muestra una de las utilidades mas importantes de Docker en desarrollo:

- El servidor corre dentro del contenedor.
- Los archivos viven en el sistema local.
- Los cambios se reflejan de forma inmediata.

Es una forma muy comoda de trabajar tanto en **Linux** como en **Windows**.

**Fecha de actualización:** 07/04/2026
