---
title: "UD 06 - 6.1 CMOS y UEFI"
description: "CMOS y UEFI"
summary: "CMOS y UEFI"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2025-10-01
icon: "material/file-document-outline"
permalink: /mm/u06/6-1-cmos-y-uefi
categories:
    - "MON"
tags:
    - "cmos"
---

## TEMA 6. CMOS


## 1. Introducción a la memoria CMOS
#  Vocabulario

| Término          | Definición                                                                                     |
|------------------|------------------------------------------------------------------------------------------------|
| CMOS             | Complementary Metal-Oxide-Semiconductor; tecnología de bajo consumo usada en chips de memoria y circuitos electrónicos en PC.         |
| Memoria CMOS     | Pequeña memoria RAM volátil que almacena la configuración del sistema, como hora, fecha y ajustes de BIOS, alimentada por una pila.    |
| Batería CMOS     | Pila (normalmente CR2032) de la placa base que suministra energía para mantener la memoria CMOS activa cuando el PC está apagado.       |
| BIOS             | Firmware almacenado en memoria ROM que inicializa y prueba el hardware del PC, usando datos guardados en la memoria CMOS.               |
| Reseteo CMOS     | Proceso de borrar la configuración guardada en CMOS para restaurar valores por defecto, mediante botón, puente de pines o extracción de pila. |
| Configuración BIOS| Ajustes almacenados en la memoria CMOS que controlan hardware, secuencia de arranque, contraseñas y otras opciones de sistema.            |


### Definición y conceptos clave

La memoria CMOS (Complementary Metal-Oxide-Semiconductor) es un tipo de memoria RAM de bajo consumo utilizada en las placas base de los PCs para almacenar la configuración del sistema, incluyendo parámetros como la fecha y hora, el orden de arranque, contraseñas y configuraciones de hardware esenciales. Esta memoria es volátil y requiere energía constante suministrada por una batería, comúnmente una pila tipo botón CR2032, que permite conservar los datos cuando el PC está apagado. A diferencia del BIOS, que es el firmware almacenado en memoria ROM, la memoria CMOS almacena los valores modificables por el usuario que son usados por el BIOS durante el arranque del sistema para configurar el hardware y el sistema operativo. Un fallo o pérdida de energía en esta batería provoca que la configuración CMOS se resetee, lo que puede generar errores al arrancar el equipo.

### Breve historia de la tecnología CMOS en PCs

La tecnología CMOS se comenzó a usar ampliamente en PCs desde finales de los años 70 y principios de los 80 como una solución más eficiente energéticamente para mantener la configuración del sistema sin necesidad de fuentes externas o recargas frecuentes, a diferencia de las tecnologías previas como baterías recargables internas. A medida que las placas base y el firmware BIOS evolucionaban, la memoria CMOS se convirtió en un componente estándar para almacenar las configuraciones personalizadas del usuario y facilitar la funcionalidad del sistema. Con el paso del tiempo, el CMOS continuó utilizándose por su bajo consumo y alta fiabilidad, aunque muchas funciones han ido integrándose con tecnologías más modernas como la memoria flash para BIOS/UEFI, que permite actualizar el firmware sin perder la configuración almacenada.

Este equilibrio entre persistencia de configuraciones y eficiencia energética hace que la memoria CMOS siga siendo un elemento clave en el diseño y mantenimiento de PCs modernos.  

---

<div style="text-align: center;">
  <img src="../assets/cmos/cmos.webp" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

## 2. Tecnología CMOS

### Funciones principales y características

La memoria CMOS es un chip de bajo consumo energético presente en la mayoría de placas base de PCs, encargado de almacenar información esencial del sistema, como la configuración del BIOS, fecha, hora, secuencia de arranque, contraseñas y parámetros de hardware. Esta memoria es volátil, por lo que requiere una batería (normalmente una pila CR2032) que le suministre energía aún cuando el PC está apagado. Su función principal es conservar la configuración del sistema para que al encender el equipo, éste pueda arrancar con los ajustes definidos y reconocer el hardware conectado. La tecnología CMOS destaca por su bajo consumo, alta fiabilidad y capacidad para mantener la información crítica sin requerir una fuente de energía principal.

### Comparación con otros tipos de memoria (RAM y ROM)

- **RAM:** La memoria RAM es volátil y se utiliza para almacenar datos y programas en ejecución; al apagar el PC, su contenido se pierde totalmente. La CMOS también es volátil, pero su función es mantener configuraciones específicas mediante alimentación de batería.
- **ROM:** La memoria ROM almacena firmware, como el BIOS o UEFI, de forma permanente y no se borra al apagar el equipo. La CMOS, en cambio, almacena datos modificables por el usuario que afectan el arranque y configuración del sistema.
- La CMOS es más permanente que la RAM para configuraciones, pero menos que la ROM, ya que depende de la pila para mantener su contenido.

### Relación entre CMOS, BIOS y UEFI

**El BIOS (Basic Input Output System) o su sucesor UEFI, son firmware almacenados en memoria no volátil (ROM/Flash) que controlan el proceso de arranque del PC y la inicialización del hardware.** El CMOS almacena los parámetros de configuración que el BIOS/UEFI utiliza durante el arranque para saber cómo debe configurarse el sistema, como el orden de dispositivos de arranque, la hora, y las opciones de seguridad. Aunque CMOS y BIOS trabajan estrechamente, son componentes diferentes: la CMOS solo guarda la configuración, mientras que el BIOS/UEFI ejecuta las instrucciones necesarias para el inicio del sistema.

Esta relación permite modificar configuraciones persistentes sin alterar el firmware y facilita la gestión del hardware y la personalización del arranque del sistema. En sistemas modernos, muchas funciones tradicionales de la CMOS están siendo transferidas al firmware UEFI, pero su principio y función básica se mantienen.


## 3. Ubicación física y alimentación de la CMOS

### Chip y pila en la placa base: tipos y vida útil

La memoria CMOS está contenida en un chip específico dentro de la placa base del PC. Tradicionalmente, esta memoria se encuentra cerca de la batería que la alimenta, y es identificable como un pequeño chip de memoria RAM volátil de bajo consumo. La CMOS depende de una batería interna para mantener los datos almacenados cuando el equipo está apagado.

La batería más común es el modelo de pila de botón tipo CR2032 de 3V, ubicada generalmente en un soporte visible en la placa base, frecuentemente cerca de las ranuras de expansión o en la parte inferior de la placa. La vida útil típica de esta batería oscila entre 3 y 10 años, dependiendo del uso del PC y la calidad de la batería. Cuando esta pila se agota, la memoria CMOS pierde alimentación y con ella la configuración guardada, lo que provoca que el PC pueda perder la fecha, hora y los ajustes del BIOS, además de dificultar o impedir el arranque correcto del sistema.

---

<div style="text-align: center;">
  <img src="../assets/cmos/placa.webp" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

En placas Z790 la “CMOS” no es un chip aparte: el RTC/CMOS está integrado en el PCH (chipset Intel Z790) y los ajustes de UEFI se guardan en la flash SPI. En la foto (Gigabyte Z790 AERO G, con el disipador quitado) la CMOS/RTC reside en el PCH.



### Papel de la batería CR2032

Esta pila CR2032 es fundamental para el funcionamiento continuo de la memoria CMOS, pues suministra la energía necesaria para que la configuración del sistema se mantenga activa y no se borre al apagar el PC. Es una batería de litio con capacidad suficiente para alimentar la memoria durante años en condiciones normales. Cuando la batería comienza a fallar, es habitual notar mensajes de error al encender el PC, como advertencias relacionadas con la fecha y hora, o la imposibilidad de almacenar los parámetros de configuración.

El reemplazo de la batería CR2032 es sencillo, generalmente solo es necesario liberar un pequeño clip o pestillo que la sujeta y colocar una nueva batería del mismo tipo respetando la polaridad indicada. Es recomendable realizar este cambio con el equipo apagado y desconectado para evitar daños.

Mantener esta batería en buen estado es crucial para evitar problemas de configuración y garantizar un arranque estable y confiable del PC.

---

<div style="text-align: center;">
  <img src="../assets/cmos/pila.avif" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---


## 4. Uso de la memoria CMOS en un PC

### Almacenamiento de la configuración del sistema

La memoria CMOS almacena de forma temporal pero persistente, mediante alimentación por batería, la configuración esencial del sistema que el BIOS utiliza para la puesta en marcha del PC. Estos datos definen cómo el hardware y el firmware interactúan, preservando ajustes específicos establecidos por el usuario o el fabricante. Al apagar el PC, la CMOS mantiene esta información intacta gracias a la batería interna, evitando que se pierdan los parámetros que permiten un arranque correcto y personalizado.

### Parámetros guardados: fecha, hora, configuración de hardware

Entre los parámetros que se almacenan en la memoria CMOS se encuentran la fecha y hora del sistema, que permiten que el reloj del sistema operativo mantenga la sincronía correcta. Además, se guardan configuraciones relevantes de hardware, como la secuencia de arranque (orden en que se reconocen los dispositivos), perfiles de overclocking, opciones de activación o desactivación de componentes, y contraseñas de seguridad para el acceso a la BIOS o al sistema. Esto facilita la personalización y control del funcionamiento del PC.

---

| Parámetro                  | Descripción                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------|
| Fecha y Hora              | Mantiene la fecha y hora del sistema para el reloj interno                                    |
| Secuencia de Arranque    | Define el orden de los dispositivos desde donde se carga el sistema operativo                 |
| Frecuencia y Voltaje CPU | Configuraciones relacionadas con el reloj y voltajes del procesador, esenciales para overclock|
| Configuración de Memoria | Velocidades, timings y perfiles XMP/DOCP para la RAM                                         |
| Control de Energía       | Ajustes de gestión energética, estados C y modos turbo                                       |
| Control de Ventiladores  | Velocidad y perfiles de los ventiladores del sistema                                         |
| Opciones de Seguridad    | Contraseñas BIOS, bloqueo de arranque y control de puertos                                   |
| Periféricos Integrados   | Estado y configuración de audio, red, gráficos y otros dispositivos integrados                |
| Opciones de Virtualización| Habilitación o deshabilitación de tecnologías de virtualización como Intel VT-x              |
| Configuraciones PCIe     | Velocidad y modo de las ranuras PCIe                                                         |
| Control de Dispositivos  | Habilitación o deshabilitación de puertos USB, puertos SATA, redes, etc.                     |
| Estado de la batería CMOS| Almacenamiento del estado o alertas sobre la batería que alimenta la CMOS                     |

---

### Interacción con el BIOS al arranque

Durante el encendido del PC, el BIOS lee los datos almacenados en la memoria CMOS para aplicar los ajustes establecidos antes del arranque del sistema operativo. Esto incluye inicializar dispositivos, configurar buses y velocidades, cargar configuraciones específicas y verificar la integridad del hardware. Si la CMOS está desconfigurada o la batería agotada, el BIOS detecta esta situación y puede mostrar mensajes de error o solicitar al usuario que ingrese a la configuración para corregir los parámetros antes de continuar. Esta interacción es crucial para el correcto funcionamiento y estabilidad del PC desde el primer momento.

## 5. Reseteo y restauración de la CMOS

El reseteo y la restauración de la memoria CMOS son procedimientos habituales para solucionar problemas de configuración, recuperar el acceso si se olvida una contraseña o asegurar el funcionamiento correcto del sistema. Estos procesos devuelven la CMOS a sus valores predeterminados de fábrica.

### Métodos principales para resetear la CMOS

- **Mediante el menú BIOS/UEFI:**  
  1. Accede al menú presionando la tecla correspondiente (F2, SUPR, ESC) durante el arranque.
  2. Busca la opción `Load Setup Defaults`, `Restore Defaults` o similar.
  3. Guarda los cambios y reinicia el PC (generalmente con F10).

---

<div style="text-align: center;">
  <img src="../assets/cmos/reset_cmos_uefi.jpg" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

- **Retirando la pila de la placa base:**  
  1. Apaga el PC y desconéctalo de la corriente.
  2. Abre la caja y localiza la pila (tipo CR2032) en la placa base.
  3. Extráela durante al menos 5 minutos (este tiempo es estimado, ya que hay CMOS que pueden necesitar más tiempo).
  4. Vuelve a colocar la pila y enciende el PC.  
  Esto borra cualquier configuración almacenada en la CMOS.

- **Utilizando el jumper de reseteo:**  
  1. Apaga el PC y localiza lo pines “CLR_CMOS”, “CLEAR” o similar en la placa base (consulta el manual).
  2. Usando un jumper, conecta los dos pines. (tambien se realiza con un destornillador, pero es un proceso que entraña ciertos riesgos para el equipo)
  3. Arranca el sistema. 

---

<div style="text-align: center;">
  <img src="../assets/cmos/reset_cmos_jumper.jpg" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

## 6. Problemas y mantenimiento de la CMOS

La memoria CMOS, aunque pequeña y resistente, puede presentar ciertos problemas que afectan el correcto funcionamiento del PC. Diagnosticar y mantener la CMOS ayuda a evitar fallos relacionados con la configuración del sistema.

### Problemas frecuentes relacionados con la CMOS

- **Fallo de la pila:**  
  Si la pila de la placa base está agotada o presenta fallo, el PC puede mostrar mensajes de error como “CMOS Checksum Error” al encender. También pueden perderse la fecha/hora y la configuración BIOS cada vez que se apaga el equipo.

- **Configuraciones corruptas:**  
  Cambios incorrectos en la BIOS/UEFI, cortes eléctricos o incompatibilidades pueden corromper la información almacenada en la CMOS. Esto provoca errores de arranque o inestabilidad.

- **Mensaje de error al iniciar:**  
  Aparecen avisos del tipo “CMOS Battery Failure”, “CMOS Settings Wrong” o similares. Suelen indicar problemas de hardware o configuraciones erróneas.

- **Imposibilidad de guardar cambios:**  
  Si no se guardan los ajustes realizados en la BIOS, puede ser señal de que la pila está descargada o la CMOS dañada.

### Mantenimiento de la CMOS

- **Sustitución periódica de la pila:**  
  Cambiar la pila CR2032 cada 2-4 años —o cuando se perciban síntomas de fallo— garantiza la conservación de la configuración.

- **Revisar y actualizar configuraciones:**  
  Es recomendable comprobar y actualizar los parámetros de BIOS/UEFI después de cambios de hardware o actualizaciones importantes.

- **Limpiar contactos y evitar la acumulación de polvo:**  
  Mantener la zona de la placa base limpia ayuda a prevenir problemas de conexión eléctrica que podrían afectar la memoria CMOS.

- **Actualizar la BIOS/UEFI de forma segura:**  
  Las actualizaciones solventan errores de funcionamiento, pero deben hacerse siguiendo instrucciones del fabricante y comprobando compatibilidad con el modelo de la placa base.

### Recomendaciones adicionales

- Realiza comprobaciones periódicas de la fecha y hora del sistema; desajustes pueden indicar fallo en la pila.
- Guarda una copia de la configuración óptima de la BIOS/UEFI para poder restaurarla en caso de problemas.
- Consulta el manual técnico de la placa base ante cualquier duda o anomalía detectada.

---


### Consideraciones importantes

- Después del reseteo, será necesario reconfigurar parámetros como orden de arranque, fecha/hora, contraseñas y ajustes específicos para el sistema.
- Es recomendable consultar el manual de la placa base para identificar correctamente la ubicación del jumper y de la pila.
- Un reseteo incorrecto puede provocar la pérdida de la configuración necesaria para arrancar el sistema operativo.

### Situaciones en las que es útil el reseteo de la CMOS

- Olvido o bloqueo por contraseña de BIOS.
- Corrupción de configuración tras un fallo de hardware.
- Problemas de incompatibilidad después de actualizar componentes.
- Restablecimiento durante el mantenimiento preventivo.

**RECOMENDABLE DIRÍA CASI OBLIGATORIO RESETEAR CMOS CUANDO SE MANIPULE ALGÚN COMPONENTE**

---
