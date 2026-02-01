---
title: "A6.1 BIOS, UEFI y proceso de encendido"
description: "BIOS, UEFI y proceso de encendido del PC"
summary: "BIOS, UEFI y proceso de encendido del PC"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2026-02-01
icon: "material/file-document-outline"
categories:
    - "ANE"
tags:
    - "bios"
    - "uefi"
    - "post"
    - "arranque"
---

# Anexo 6. BIOS, UEFI y proceso de encendido del PC

---

## 1. Panorama general del arranque

El proceso de encendido de un PC es una secuencia ordenada de pasos que comienza cuando el usuario pulsa el boton de encendido y termina cuando el sistema operativo toma el control. Esta secuencia esta dirigida por el firmware de la placa base (BIOS o UEFI), que prepara el hardware, comprueba que todo funciona y decide desde que dispositivo se iniciara el sistema.

Comprender estas fases ayuda a diagnosticar fallos, interpretar mensajes y reducir tiempos de reparacion. En mantenimiento, la clave es distinguir entre problemas de hardware (por ejemplo, RAM defectuosa) y problemas de configuracion (orden de arranque o ajustes incorrectos).

---

## 2. Secuencia de encendido paso a paso

1) **Señal de encendido (Power On)**
- La fuente de alimentacion entrega energia a la placa base.
- El chipset y la CPU reciben energia y se activan.

2) **Ejecucion del firmware (BIOS/UEFI)**
- Se inicializa el microcodigo del procesador.
- Se detecta la memoria RAM, controladoras y dispositivos basicos.

3) **POST (Power-On Self Test)**
- El firmware realiza pruebas basicas de hardware.
- Si detecta errores criticos, detiene el arranque y emite pitidos o mensajes.

4) **Inicializacion de dispositivos**
- Se preparan buses, controladoras SATA/NVMe, USB y GPU.
- Se activa la salida de video para mostrar mensajes o interfaz UEFI.

5) **Seleccion de dispositivo de arranque**
- El firmware consulta el orden de arranque configurado.
- Busca un dispositivo con un cargador valido (bootable).

6) **Carga del sistema operativo**
- BIOS carga el cargador desde el MBR.
- UEFI carga un archivo EFI desde la particion ESP.
- El sistema operativo toma el control del hardware.

<figure>
  <img src="../assets/pccomponentes_uefi_bios.jpg" alt="Interfaz UEFI moderna durante el arranque" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Interfaz UEFI moderna. Fuente: PCComponentes.</figcaption>
</figure>

---

## 3. El POST en detalle

El POST es una serie de comprobaciones automaticas que validan componentes esenciales. Su objetivo es confirmar que el hardware minimo necesario para arrancar esta disponible y funciona correctamente antes de continuar. Aunque el POST completo puede variar segun fabricante, en general sigue un orden logico de inicializacion y prueba.

- CPU y microcodigo inicial.
- Memoria RAM (presencia y conteo).
- GPU o salida de video.
- Teclado y dispositivos basicos.
- Controladoras principales (almacenamiento).

Si el POST falla, el equipo no inicia y suele mostrar **pitidos** o codigos de error. En mantenimiento, el POST es el primer indicador para saber si un fallo es de hardware.

### 3.1 Fases tipicas dentro del POST

1) **Inicializacion del procesador**  
Se comprueba que la CPU responde, se carga el microcodigo y se activan funciones basicas.

2) **Comprobacion de RAM**  
Se detecta la memoria instalada y se realiza un conteo. Si hay un modulo mal colocado o defectuoso, el POST suele detenerse aqui.

3) **Inicializacion de video**  
Se activa la salida grafica para mostrar mensajes. Si falla la GPU, es habitual que aparezcan pitidos y no haya imagen.

4) **Deteccion de periféricos basicos**  
Teclado, dispositivos USB y buses principales (PCIe, SATA/NVMe) se inicializan para permitir el arranque.

5) **Resumen y paso al cargador**  
Si no hay errores criticos, se guarda el estado y se pasa a la fase de arranque del sistema operativo.

### 3.2 Que indica un POST correcto

- Se escucha el pitido corto de inicio (si esta habilitado).\n- Aparece logo o texto de la placa base.\n- Se muestra el conteo de memoria o la pantalla UEFI.\n- El sistema continua hacia el cargador del sistema operativo.

### 3.3 Errores tipicos detectados por el POST

- **RAM mal instalada o defectuosa**: pitidos largos repetidos y detencion del arranque.\n- **GPU no detectada**: pitido largo y varios cortos, pantalla en negro.\n- **Teclado no detectado**: mensaje de error y posibilidad de continuar con F1.\n- **Dispositivo de arranque no encontrado**: se completa el POST pero no se encuentra un disco arrancable.

### 3.4 Buenas practicas al diagnosticar con POST

- Verificar primero la RAM: extraer y volver a colocar los modulos.\n- Probar con otra salida de video o con otra tarjeta grafica.\n- Revisar conexiones de alimentacion principales (ATX y CPU).\n- Consultar el manual de la placa para interpretar el codigo de pitidos o LEDs de diagnostico.

<figure>
  <img src="../assets/profesionalreview_bios_setup.jpg" alt="Pantalla BIOS durante comprobaciones" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Pantalla BIOS durante el arranque. Fuente: ProfesionalReview.</figcaption>
</figure>

---

## 4. Pitidos de error y diagnostico

Los pitidos de la BIOS permiten identificar fallos cuando no hay video. El significado exacto depende del fabricante (AMI, Award, Phoenix), pero los patrones mas comunes son:

- **1 pitido corto**: arranque correcto.
- **Pitidos largos repetidos**: fallo de RAM.
- **1 largo + 2 cortos**: error de tarjeta grafica.
- **Pitidos continuos**: fallo de fuente o placa base.

En mantenimiento, siempre se debe consultar la tabla especifica del fabricante para interpretar el patron de pitidos.

### 4.1 Otros metodos de diagnostico de arranque

Ademas de los pitidos, hoy existen varias ayudas para identificar el fallo de forma mas precisa:

- **LEDs de diagnostico en la placa base**: algunas placas tienen indicadores para CPU, RAM, GPU o BOOT. Si queda fijo en uno, apunta al componente afectado.\n- **Display de codigos POST**: muchas placas incluyen un display de dos digitos (hexadecimal) que muestra el codigo del POST. Ese codigo se interpreta con la tabla del fabricante.\n- **Tarjetas POST PCIe**: se insertan en una ranura PCIe y muestran el codigo POST aunque no haya video. Son muy utiles cuando el equipo no da imagen.\n- **Altavoz interno (speaker)**: si la placa no trae altavoz, conectar uno permite escuchar los pitidos.\n
### 4.2 Uso basico de una tarjeta POST PCIe

1) Insertar la tarjeta POST en una ranura PCIe disponible.\n2) Encender el equipo y observar el codigo mostrado.\n3) Consultar la tabla de codigos del fabricante para interpretar el fallo.\n4) Corregir el componente o la configuracion indicada.

Estas tarjetas son especialmente utiles cuando el fallo impide acceder a la pantalla o cuando los pitidos no son claros.

<figure>
  <img src="../assets/corsair_bios.webp" alt="BIOS en placa base" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">BIOS en placa base. Fuente: Corsair.</figcaption>
</figure>

---

## 5. BIOS vs UEFI en el arranque

**BIOS tradicional**
- Utiliza MBR (Master Boot Record).
- Limite tipico de discos de 2 TB.
- Interfaz de texto.

**UEFI moderno**
- Utiliza GPT (GUID Partition Table).
- Soporta discos grandes y arranque seguro (Secure Boot).
- Interfaz grafica y soporte de raton.

En la practica, UEFI es mas flexible y seguro, pero requiere configuracion adecuada (modo UEFI o CSM) para evitar problemas de arranque con sistemas antiguos.

<figure>
  <img src="../assets/profesionalreview_bios_vs_uefi.jpg" alt="Comparativa BIOS vs UEFI" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Comparativa BIOS vs UEFI. Fuente: ProfesionalReview.</figcaption>
</figure>

### 5.1 MBR (Master Boot Record)

El MBR es el esquema clasico de particionado. Guarda la tabla de particiones y el cargador de arranque en el primer sector del disco. Sus limites principales son el numero de particiones primarias y el tamano maximo de disco (aprox. 2 TB). En mantenimiento, MBR suele aparecer en equipos antiguos o en instalaciones hechas en modo BIOS.

<figure>
  <img src="../assets/mbr_partition_table_scheme.svg" alt="Esquema de particiones MBR" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Esquema de particionado MBR. Fuente: Wikimedia Commons (GNU GRUB on MBR).</figcaption>
</figure>

### 5.2 GPT (GUID Partition Table)

GPT es el esquema moderno asociado a UEFI. Permite muchos mas registros de particion, soporta discos grandes y guarda copias de seguridad de la tabla. En entornos actuales es el estandar recomendado por seguridad y escalabilidad.

<figure>
  <img src="../assets/gpt_partition_table_scheme.svg" alt="Esquema de particiones GPT" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Esquema de particionado GPT. Fuente: Wikimedia Commons (GUID Partition Table).</figcaption>
</figure>

---

## 6. Busqueda del sistema para arranque

El firmware sigue el **orden de arranque** configurado. El proceso habitual es:

1) Revisar dispositivos internos (SSD/HDD).
2) Revisar unidades externas o USB.
3) Revisar red (PXE), si esta habilitado.

Si no se encuentra un cargador valido, el firmware muestra un error como:

- "No bootable device"
- "Operating system not found"

En estos casos, el tecnico debe comprobar el orden de arranque, el estado del disco y la integridad del cargador.

<figure>
  <img src="../assets/pccomponentes_uefi_bios_2.jpg" alt="Menu de configuracion de arranque UEFI" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Menu de configuracion de arranque. Fuente: PCComponentes.</figcaption>
</figure>

---

## 7. Errores frecuentes en el arranque

- **Pantalla negra sin pitidos**: posible fallo de fuente o placa.
- **Pitidos de RAM**: memoria mal colocada o defectuosa.
- **Reinicio en bucle**: configuracion incorrecta o sobrecalentamiento.
- **Error de disco**: cable SATA flojo o SSD no detectado.

Una buena practica es revisar primero lo basico: alimentacion, memoria y conexiones.

<figure>
  <img src="../assets/corsair_bios_battery.webp" alt="Bateria CMOS en placa base" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Bateria CMOS en placa base. Fuente: Corsair.</figcaption>
</figure>

---

## 8. Recomendaciones de mantenimiento

- Mantener actualizado el BIOS/UEFI cuando el fabricante lo recomiende.
- Verificar la bateria CMOS si se pierden ajustes.
- Revisar el orden de arranque antes de reinstalar sistemas.
- Documentar cambios de firmware y configuraciones.

---

## Resumen (ideas clave)

- El arranque es una secuencia guiada por BIOS/UEFI.
- El POST detecta fallos basicos y emite pitidos.
- BIOS usa MBR; UEFI usa GPT y Secure Boot.
- Los errores de arranque se diagnostican por sintomas y mensajes.

## Referencias y enlaces

- https://www.pccomponentes.com/bios-uefi-que-es
- https://www.corsair.com/es/es/explorer/diy-builder/memory/what-are-cmos-bios-and-uefi/
- https://www.profesionalreview.com/guias/bios/
- https://commons.wikimedia.org/wiki/File:GNU_GRUB_on_MBR_partitioned_hard_disk_drives.svg
- https://commons.wikimedia.org/wiki/File:GUID_Partition_Table_Scheme.svg





**Fecha de actualización:** 01/02/2026
