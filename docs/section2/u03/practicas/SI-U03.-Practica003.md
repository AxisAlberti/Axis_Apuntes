---
title: "UD 03 - P3: Docker Compose con Apache, PHP y MariaDB"
description: "Practica guiada para desplegar un entorno web multicontenedor con Apache, PHP y MariaDB"
summary: "Uso de Docker Compose para levantar una arquitectura web basica con persistencia y comunicacion entre servicios"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2026-04-07
icon: "material/file-document-edit"
permalink: /si/u03/p3
categories:
    - "SIS"
tags:
    - "practica"
    - "docker"
    - "apache"
    - "php"
    - "mariadb"
    - "docker compose"
---

## Objetivo

Desplegar un entorno multicontenedor con Apache, PHP y MariaDB usando `docker compose`, conectando la aplicacion web con una carpeta local del sistema anfitrion y almacenando los datos de la base de datos en un volumen persistente.

## Que vas a practicar

- Definir varios servicios en `compose.yaml`.
- Compartir archivos web desde el sistema local.
- Crear una base de datos MariaDB con persistencia.
- Comprobar la comunicacion entre contenedores.
- Entender una arquitectura web basica con Docker.

## Requisitos

- Docker funcionando correctamente.
- Soporte para `docker compose`.
- Navegador web.
- Editor de texto.

## 1. Estructura del proyecto

Crea una carpeta para el proyecto.

### En Linux

```bash
mkdir -p ~/docker/apache-php-mariadb/web
cd ~/docker/apache-php-mariadb
```

### En Windows PowerShell

```powershell
mkdir $HOME\docker\apache-php-mariadb\web
cd $HOME\docker\apache-php-mariadb
```

La estructura final sera parecida a esta:

```text
apache-php-mariadb/
├── compose.yaml
└── web/
    └── index.php
```

## 2. Crear el archivo PHP de prueba

Dentro de la carpeta `web`, crea un archivo `index.php`.

### En Linux

```bash
cat > web/index.php <<'EOF'
<?php
echo "<h1>Apache + PHP + MariaDB con Docker Compose</h1>";
echo "<p>La aplicacion PHP se sirve desde una carpeta local compartida.</p>";
echo "<p>Servidor actual: " . gethostname() . "</p>";
?>
EOF
```

### En Windows PowerShell

```powershell
@'
<?php
echo "<h1>Apache + PHP + MariaDB con Docker Compose</h1>";
echo "<p>La aplicacion PHP se sirve desde una carpeta local compartida.</p>";
echo "<p>Servidor actual: " . gethostname() . "</p>";
?>
'@ | Set-Content web/index.php
```

## 3. Crear el archivo `compose.yaml`

Crea este archivo en la carpeta principal del proyecto:

```yaml
services:
  web:
    image: php:8.2-apache
    container_name: practica_web
    ports:
      - "8080:80"
    volumes:
      - ./web:/var/www/html
    depends_on:
      - db

  db:
    image: mariadb:11
    container_name: practica_db
    environment:
      MARIADB_ROOT_PASSWORD: secreto
      MARIADB_DATABASE: ejemplo
      MARIADB_USER: alumno
      MARIADB_PASSWORD: alumno123
    volumes:
      - datos_mariadb:/var/lib/mysql

volumes:
  datos_mariadb:
```

## 4. Explicacion del archivo

### Servicio `web`

- Usa la imagen `php:8.2-apache`.
- Publica Apache en el puerto `8080`.
- Monta la carpeta local `web` dentro de `/var/www/html`.
- Depende del servicio `db`.

### Servicio `db`

- Usa la imagen `mariadb:11`.
- Crea una base de datos inicial.
- Define usuario, contraseña y contraseña de administrador.
- Guarda los datos en un volumen persistente.

### Volumen `datos_mariadb`

El volumen permite que los datos de MariaDB no se pierdan aunque el contenedor se elimine.

## 5. Levantar el entorno

Desde la carpeta donde esta `compose.yaml`, ejecuta:

```bash
docker compose up -d
```

## 6. Comprobar que los servicios estan funcionando

```bash
docker compose ps
```

Debe aparecer al menos:

- Un contenedor web
- Un contenedor de base de datos

## 7. Probar la web en el navegador

Abre:

```text
http://localhost:8080
```

Debe aparecer la pagina PHP de prueba.

## 8. Comprobar la persistencia de MariaDB

Puedes revisar los logs:

```bash
docker compose logs db
```

Tambien puedes entrar al contenedor:

```bash
docker exec -it practica_db mariadb -u alumno -palumno123 ejemplo
```

Una vez dentro, prueba:

```sql
SHOW DATABASES;
EXIT;
```

## 9. Modificar la pagina PHP desde la carpeta local

Edita `web/index.php` y cambia el contenido.

Por ejemplo:

```php
<?php
echo "<h1>Entorno multicontenedor funcionando</h1>";
echo "<p>He modificado este archivo desde la carpeta local.</p>";
?>
```

Recarga el navegador.

### Resultado esperado

Los cambios deben aparecer sin reconstruir la imagen, porque Apache y PHP estan leyendo el archivo desde la carpeta compartida.

## 10. Comprobar la comunicacion entre servicios

Los contenedores definidos en el mismo `compose.yaml` pueden comunicarse usando el nombre del servicio.

En este caso:

- El servicio web puede localizar la base de datos como `db`.

Esto es importante porque en Docker Compose no solemos usar `localhost` para la comunicacion entre contenedores, sino el **nombre del servicio**.

## 11. Diferencias entre Linux y Windows

La practica es la misma en ambos sistemas, pero conviene recordar:

- En **Linux** las rutas suelen ser como `/home/alumno/...`
- En **Windows** las rutas suelen ser como `C:\\Users\\Alumno\\...`
- Si trabajas en **Windows con WSL 2**, conviene mantener claro desde que terminal ejecutas `docker compose`
- Los conceptos de volumen, red y servicios no cambian

## 12. Detener el entorno

Cuando termines:

```bash
docker compose down
```

Si quieres eliminar tambien el volumen de la base de datos:

```bash
docker compose down -v
```

## 13. Cuestiones para reflexionar

1. ¿Que funcion cumple `depends_on` en el archivo `compose.yaml`?
2. ¿Por que MariaDB usa un volumen y la carpeta web usa un montaje local?
3. ¿Por que el servicio web debe dirigirse a la base de datos con el nombre `db` y no con `localhost`?
4. ¿Que diferencia hay entre `docker compose down` y `docker compose down -v`?

## 14. Ampliacion opcional

Como ampliacion, puedes probar:

- Añadir una tabla real en MariaDB.
- Crear una pagina PHP que se conecte a la base de datos.
- Cambiar las credenciales usando variables de entorno en un archivo `.env`.
- Añadir phpMyAdmin como cuarto servicio.

## 15. Idea final

Esta practica muestra un caso muy cercano a un entorno real:

- Un contenedor sirve la aplicacion web.
- Otro contenedor guarda la base de datos.
- Los archivos del proyecto viven en el sistema local.
- Los datos importantes de la base de datos quedan persistidos en un volumen.

Es una buena base para entender por que Docker Compose resulta tan util en desarrollo y pruebas.

**Fecha de actualización:** 07/04/2026
