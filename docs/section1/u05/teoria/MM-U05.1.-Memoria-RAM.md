---
title: "UD 05 - 5.1 Memoria RAM"
description: "Memoria RAM"
summary: "Memoria RAM"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2026-02-10
icon: "material/file-document-outline"
permalink: /mm/u05/5-1-memoria-ram
categories:
    - "MON"
tags:
    - "memoria"
---

## TEMA 5. MEMORIA RAM

---

## 1. Concepto y vocabulario esencial

La **memoria RAM** es la **memoria principal** del sistema. Es **rápida** y **volátil**: guarda datos y programas en uso, pero se pierde al apagar el equipo. Su objetivo es dar a la CPU un espacio de trabajo inmediato para evitar depender del almacenamiento (mucho más lento).

### 1.1 Vocabulario fundamental

| Término | Definición |
|---|---|
| **RAM** | Memoria temporal de trabajo del sistema. |
| **DRAM** | Tipo de RAM basada en condensadores que necesita refresco. |
| **DDR** | Memoria DRAM que transfiere datos en ambos flancos del reloj. |
| **SPD** | Chip con parámetros del módulo para configuración automática. |
| **XMP / EXPO** | Perfiles de memoria preconfigurados para ajustar parámetros en BIOS. |
| **Canal de memoria** | Camino de datos entre la CPU y la RAM. |
| **DIMM / SO-DIMM** | Formatos físicos de módulos de memoria. |

---

## 2. Módulos de memoria y formatos físicos

Los módulos de RAM se fabrican en distintos formatos. En sobremesa se usan **DIMM** y en portátiles **SO-DIMM**. Cada generación tiene muescas y pines específicos para evitar incompatibilidades.

<figure markdown>
  ![](../assets/ram/ram_slots_motherboard.jpg)
  <figcaption>Ranuras DIMM en una placa base. Fuente: Wikimedia Commons.</figcaption>
</figure>

<figure markdown>
 ![](../assets/ram/ddr4_dimm.jpg)
 <figcaption>Módulo DIMM DDR4. Fuente: Wikimedia Commons.</figcaption>
</figure>

<figure markdown>
 ![](../assets/ram/sodimm_modules.jpg)
 <figcaption>Ejemplos de módulos SO-DIMM. Fuente: Wikimedia Commons.</figcaption>
</figure>

---

## 3. Cómo trabaja la RAM: bancos, filas y ráfagas

La DRAM se organiza internamente en **bancos**, **filas** y **columnas**. Para acceder a un dato, primero se activa una fila y luego se lee o escribe en una columna. Para mejorar eficiencia, la RAM usa **prefetch** y envía datos en **ráfagas** (burst). Esto permite mover más información por cada acceso.

---

## 4. Generaciones DDR y compatibilidad

Cada generación de DDR mejora rendimiento y eficiencia, pero **no es compatible físicamente** con la anterior. Por eso es importante elegir el tipo correcto según la placa base.

| Generación | Rasgo clave | Compatibilidad |
|---|---|---|
| DDR3 | Menor consumo que DDR2 | No compatible con DDR4/DDR5 |
| DDR4 | Mejor eficiencia y densidad | No compatible con DDR5 |
| DDR5 | Nuevas mejoras internas y subcanales | No compatible con DDR4 |

---

## 5. Rendimiento práctico: capacidad, canales y perfiles

El rendimiento real no depende solo de la velocidad, sino de tres factores principales:

- **Capacidad:** cuanto mayor es, menos depende el sistema del disco.
- **Canales:** usar dos módulos compatibles en **dual channel** mejora el ancho de banda.
- **Perfiles (XMP/EXPO):** permiten aplicar ajustes validados desde BIOS.

<figure markdown>
  ![](../assets/ram/dual_channel_slots.jpg)
  <figcaption>Ejemplo de ranuras para doble canal. Fuente: Wikimedia Commons.</figcaption>
</figure>

---

## 6. SPD y configuración automática

Cada módulo incluye un chip **SPD** con los parámetros recomendados por el fabricante. La BIOS/UEFI lee estos datos y ajusta la memoria de forma automática.

---

## 7. ECC y fiabilidad

La memoria **ECC** detecta y corrige errores de datos. Se usa sobre todo en servidores y equipos críticos. Para que funcione es necesario que **CPU, placa y módulos** sean compatibles.

---

## 8. Jerarquía de memoria

La RAM se sitúa entre la caché de la CPU y el almacenamiento. Es un punto de equilibrio entre **velocidad** y **capacidad**.

<figure markdown>
 ![](../assets/memoria/piramide_memoria.webp)
 <figcaption>Jerarquía de memorias: caché, RAM y almacenamiento.</figcaption>
</figure>

---

## 9. Compatibilidad e instalación (checklist)

- Verifica el **tipo DDR** compatible con la placa.
- Comprueba el **formato físico** (DIMM o SO-DIMM).
- Instala módulos en ranuras recomendadas para **dual channel**.
- Activa **XMP/EXPO** si el sistema lo soporta.
- Revisa la **QVL** del fabricante para evitar incompatibilidades.

---

## 10. Diagnóstico básico de problemas

Síntomas frecuentes:
- El equipo no arranca.
- Se reconoce menos memoria de la instalada.
- Aparecen reinicios o errores aleatorios.

Pasos típicos:
1. Probar módulos por separado.
2. Cambiar de ranura.
3. Revisar compatibilidad y ajustes en BIOS.

---

## 11. Resumen final

- La RAM es la memoria principal y es **volátil**.
- El formato del módulo y el tipo DDR deben ser compatibles con la placa.
- El **dual channel** mejora el rendimiento.
- **SPD, XMP y EXPO** simplifican la configuración.

---

## 12. Referencias

- Crucial – What is RAM and what does RAM do?: https://www.crucial.com/articles/about-memory/support-what-does-computer-memory-do
- JEDEC – SPD (Serial Presence Detect) announcement: https://www.businesswire.com/news/home/20200302005918/en/JEDEC-Announces-Publication-of-a-New-Serial-Presence-Detect-Device
- Intel – XMP (Extreme Memory Profile): https://www.intel.com/content/www/us/en/gaming/extreme-memory-profile-xmp.html
- AMD – EXPO (Extended Profiles for Overclocking): https://www.amd.com/en/products/processors/technologies/expo.html
- Wikimedia Commons – RAM Module (DDR4): https://commons.wikimedia.org/wiki/File:RAM_Module_(SDRAM-DDR4).jpg
- Wikimedia Commons – Assorted SO-DIMM Modules: https://commons.wikimedia.org/wiki/File:Assorted_SO-DIMM_Modules.jpg
- Wikimedia Commons – Four SDRAM DIMM slots on motherboard: https://commons.wikimedia.org/wiki/File:Four_SDRAM_DIMM_slots_on_a_computer_motherboard.jpg
- Wikimedia Commons – Dual channel slots: https://commons.wikimedia.org/wiki/File:Dual_channel_slots.jpg

**Fecha de actualización:** 10/02/2026
