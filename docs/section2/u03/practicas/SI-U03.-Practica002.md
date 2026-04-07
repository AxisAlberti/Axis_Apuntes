---
title: "UD 03 - P2: Docker Compose con Apache y carpeta compartida"
description: "Practica guiada para desplegar Apache con Docker Compose usando una carpeta local compartida"
summary: "Uso de compose.yaml para levantar un servidor Apache con contenido persistente desde el sistema anfitrion"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2026-04-07
icon: "material/file-document-edit"
permalink: /si/u03/p2
categories:
    - "SIS"
tags:
    - "practica"
    - "docker"
    - "apache"
    - "docker compose"
---

## Objetivo

Desplegar un servidor web Apache con `docker compose`, conectando una carpeta del sistema local con el directorio web del contenedor para servir contenido HTML de forma sencilla y persistente.

## Que vas a practicar

- Crear un archivo `compose.yaml`.
- Levantar un servicio Apache con Docker Compose.
- Compartir una carpeta local con el contenedor.
- Verificar que los cambios locales se publican en el servidor.

## Requisitos

- Docker funcionando correctamente.
- Soporte para `docker compose`.
- Navegador web.

## 1. Crear la carpeta del proyecto

### En Linux

```bash
mkdir -p ~/docker/apache-compose/web
cd ~/docker/apache-compose
```

### En Windows PowerShell

```powershell
mkdir $HOME\docker\apache-compose\web
cd $HOME\docker\apache-compose
```

## 2. Crear el archivo HTML inicial

Dentro de la carpeta `web`, crea un archivo `index.html`.

### En Linux

```bash
cat > web/index.html <<'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Apache con Compose</title>
</head>
<body>
    <h1>Servidor Apache con Docker Compose</h1>
    <p>Esta pagina se sirve desde una carpeta local montada como volumen.</p>
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
    <title>Apache con Compose</title>
</head>
<body>
    <h1>Servidor Apache con Docker Compose</h1>
    <p>Esta pagina se sirve desde una carpeta local montada como volumen.</p>
</body>
</html>
'@ | Set-Content web/index.html
```

## 3. Crear el archivo `compose.yaml`

En la carpeta principal del proyecto crea este archivo:

```yaml
services:
  apache:
    image: httpd:latest
    container_name: apache_compose
    ports:
      - "8080:80"
    volumes:
      - ./web:/usr/local/apache2/htdocs/
```

## 4. Explicacion del archivo

- `services`: define los servicios de la aplicacion.
- `apache`: nombre del servicio.
- `image`: imagen usada por el servicio.
- `container_name`: nombre del contenedor.
- `ports`: publica Apache en el puerto `8080`.
- `volumes`: conecta la carpeta `web` del sistema local con la carpeta del servidor dentro del contenedor.

La ventaja de `compose` es que toda la configuracion queda guardada en un archivo y no hace falta escribir un `docker run` largo cada vez.

## 5. Levantar el servicio

Desde la carpeta donde esta `compose.yaml`, ejecuta:

```bash
docker compose up -d
```

## 6. Comprobar que funciona

Verifica el estado:

```bash
docker compose ps
```

Despues abre en el navegador:

```text
http://localhost:8080
```

Debe aparecer la pagina creada en `web/index.html`.

## 7. Modificar el contenido web

Edita el archivo `web/index.html` y cambia el texto:

```html
<h1>Apache con Compose funcionando</h1>
<p>He cambiado esta web desde la carpeta local.</p>
```

Recarga el navegador.

### Resultado esperado

El nuevo contenido debe aparecer sin reconstruir la imagen y sin volver a crear manualmente el contenedor.

## 8. Ver informacion del servicio

Puedes consultar el estado y los logs:

```bash
docker compose ps
docker compose logs
```

## 9. Detener y eliminar el entorno

Cuando termines:

```bash
docker compose down
```

El contenedor se elimina, pero la carpeta `web` y su contenido siguen existiendo en tu sistema local.

## 10. Diferencia entre esta practica y la anterior

En la practica anterior el contenedor se lanzaba con `docker run`. En esta:

- La configuracion queda escrita en `compose.yaml`.
- Es mas facil repetir el entorno.
- Resulta mas comodo ampliar la practica con nuevos servicios.

Por ejemplo, en el futuro podrias añadir:

- Una base de datos.
- Un contenedor PHP.
- Un proxy.

## 11. Cuestiones para reflexionar

1. ¿Que ventaja tiene guardar la configuracion en `compose.yaml`?
2. ¿Que relacion hay entre `volumes` y la carpeta `web` del sistema local?
3. ¿Por que esta forma de trabajo es util en desarrollo web?
4. ¿Que cambiarias si quisieras publicar Apache en el puerto `9090`?

## 12. Ampliacion opcional

Como ampliacion, puedes probar:

- Añadir un archivo CSS.
- Crear una segunda pagina HTML.
- Cambiar el nombre del servicio en `compose.yaml`.
- Añadir otro servicio al mismo archivo.

## 13. Idea final

`docker compose` resulta muy util porque convierte una serie de comandos sueltos en una configuracion reproducible. Esto facilita mucho el trabajo tanto en **Linux** como en **Windows**.

**Fecha de actualización:** 07/04/2026
