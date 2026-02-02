---
title: "A7.1 Intel vs AMD"
description: "Comparativa Intel vs AMD en entorno de taller"
summary: "Intel vs AMD: plataformas, gamas, compatibilidad y criterios de eleccion"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2026-02-02
icon: "material/file-document-outline"
permalink: /mm/a7/intel-vs-amd
categories:
    - "ANE"
tags:
    - "intel"
    - "amd"
    - "cpu"
    - "taller"
---

# Anexo 7. Intel vs AMD

## Objetivos de aprendizaje

- Reconocer las familias y plataformas actuales de Intel y AMD.
- Comprender diferencias practicas en compatibilidad, consumo y rendimiento.
- Identificar gamas de producto y su uso recomendado.
- Justificar una recomendacion al cliente con criterios tecnicos.

---

## 1. Panorama general: que significa "Intel vs AMD" en un taller

En un taller real, la comparativa **Intel vs AMD** no se reduce a "que es mas rapido". Se centra en **compatibilidad**, **precio**, **disponibilidad**, **consumo**, **tipo de uso** y **facilidad de mantenimiento**. La decision final suele depender de la **placa base**, la **memoria**, la **fuente de alimentacion** y el **perfil del cliente**.

---

## 2. Intel hoy: Arrow Lake y Raptor Lake

### 2.1 Arrow Lake (Intel)

Arrow Lake es el **nombre en clave** de una familia de procesadores de Intel. En el entorno de taller, se asocia a plataformas recientes, con foco en rendimiento y eficiencia. Segun la revision de GEEKOM, Arrow Lake aparece ligado a la serie **Core Ultra 200S** y a una plataforma con **DDR5** y **PCIe 5.0**, lo que condiciona la compatibilidad de placa y memoria.

<figure style="text-align: center;">
  <img src="../assets/arrow_lake_die.png" alt="Arrow Lake (die shot, alta resolucion)" />
  <figcaption>Fuente de la imagen: Wikimedia Commons (Arrow Lake die shot).</figcaption>
</figure>

<figure style="text-align: center;">
  <img src="../assets/geekom_arrow_lake.webp" alt="Imagen de Arrow Lake en una revision (GEEKOM)" />
  <figcaption>Fuente de la imagen: GEEKOM (revision Arrow Lake).</figcaption>
</figure>

### 2.2 Raptor Lake (Intel)

Raptor Lake es la **13.ª generacion de Intel Core** y sucesora de Alder Lake. En la practica, se encuentra en muchos equipos de escritorio recientes y convive con DDR5 o DDR4 segun la placa base utilizada, lo que obliga a validar bien la compatibilidad antes de vender o montar un kit de memoria.

<figure style="text-align: center;">
  <img src="../assets/intel_i9_14900kf_cpu.jpg" alt="Procesador Intel de escritorio (ejemplo de CPU reciente)" />
  <figcaption>Fuente de la imagen: Wikimedia Commons (Intel i9-14900KF).</figcaption>
</figure>

---

## 3. AMD hoy: Zen y la familia Ryzen

### 3.1 Zen (microarquitectura)

Zen es una **microarquitectura de CPU** de AMD que da soporte a la familia Ryzen. En un taller, es relevante porque marca generaciones, compatibilidades y el salto en rendimiento frente a arquitecturas anteriores.

<figure style="text-align: center;">
  <img src="../assets/zen_ryzen_chip.jpg" alt="Chip AMD Ryzen asociado a la arquitectura Zen" />
  <figcaption>Fuente de la imagen: Wikipedia (Zen).</figcaption>
</figure>

### 3.2 Gamas Ryzen segun uso

En el mercado, AMD segmenta Ryzen por gamas **Ryzen 3, Ryzen 5, Ryzen 7 y Ryzen 9**, con diferencias de rendimiento y orientacion de uso. Esta segmentacion es clave para recomendar un procesador a un cliente segun presupuesto y necesidades.

<figure style="text-align: center;">
  <img src="../assets/hiraoka_ryzen.jpg" alt="Imagen de catalogo Ryzen (Hiraoka)" />
  <figcaption>Fuente de la imagen: Hiraoka (articulo sobre Ryzen).</figcaption>
</figure>

### 3.3 Zen 5 y mejoras anunciadas

En medios especializados se menciona que **Zen 5** apunta a mejoras internas como **mas operaciones por ciclo** y cambios en el decode, lo que anticipa avances en rendimiento por nucleo. Esto ayuda a explicar por que una generacion nueva puede rendir mas incluso sin subir demasiado la frecuencia.

<figure style="text-align: center;">
  <img src="../assets/zen_microarchitecture.png" alt="Diagrama de la microarquitectura Zen (esquema)" />
  <figcaption>Fuente de la imagen: Wikimedia Commons (Zen microarchitecture).</figcaption>
</figure>

---

## 4. Comparativa practica en taller

### 4.0 Tabla comparativa tecnica (orientada a taller)

| Criterio | Intel | AMD |
|---|---|---|
| **Familias actuales** | Core i3/i5/i7/i9 y series Core Ultra recientes | Ryzen 3/5/7/9 en gamas de escritorio y portatil |
| **Ejemplos de plataformas** | Raptor Lake (13.ª gen), Arrow Lake (familia reciente) | Ryzen basados en Zen y siguientes generaciones |
| **Socket/placa** | Cambios de socket/chipset mas frecuentes entre generaciones | Mayor continuidad en plataforma, pero depende de BIOS/UEFI |
| **Memoria soportada** | DDR4 o DDR5 segun placa; no se mezclan | DDR4 o DDR5 segun plataforma; revisar compatibilidad |
| **PCIe y expansion** | PCIe 4.0/5.0 en gamas actuales; revisar lineas disponibles | PCIe 4.0/5.0 segun gama; comprobar lineas y chipset |
| **Consumo y refrigeracion** | CPUs tope exigen buena refrigeracion y VRM robusto | Buen rendimiento por vatio en gamas medias/altas |
| **Riesgos tipicos en taller** | Incompatibilidad de socket/chipset o RAM no soportada | BIOS desactualizada o VRM insuficiente |
| **Recomendacion practica** | Verificar compatibilidad total de placa, RAM y fuente | Verificar BIOS, soporte oficial y presupuesto real |

### 4.0.1 Tabla tecnica de ejemplo (sockets, chipsets y consumo)

| Elemento | Intel (ejemplo) | AMD (ejemplo) |
|---|---|---|
| **Socket de escritorio** | LGA 1700 (plataformas recientes) | AM4 y AM5 (segun generacion) |
| **Chipsets habituales** | Series 600/700 | Series 500/600 |
| **Rango de consumo** | 65W a 125W+ (segun modelo) | 65W a 170W (segun modelo) |
| **Requisito de BIOS/UEFI** | Menos frecuente en cambios de CPU dentro de la misma gen | Frecuente al montar CPU nueva en placa antigua |
| **Consejo de taller** | Confirmar socket y chipset exacto | Confirmar version de BIOS y soporte oficial |

### 4.1 Compatibilidad de plataforma

- **Intel**: la plataforma suele cambiar por generaciones, por lo que hay que revisar **socket**, chipset y soporte de memoria en la placa.
- **AMD**: la compatibilidad suele ser mas amplia dentro de la misma plataforma, pero hay que confirmar BIOS/UEFI y soporte de VRM.

**Consejo de taller:** antes de vender un procesador, comprobar **lista de compatibilidad** del fabricante de la placa.

### 4.2 Memoria y ancho de banda

- En plataformas nuevas se impone **DDR5**, que exige modulos compatibles y perfiles correctos.
- Hay placas que admiten **DDR4 o DDR5**, pero nunca ambas a la vez.

### 4.3 Rendimiento real

- Para **ofimatica** y uso general, la diferencia suele ser minima.
- Para **render y creacion**, importan nucleos, frecuencia sostenida y estabilidad.
- Para **gaming**, conviene equilibrar CPU con GPU y no sobredimensionar.

---

## 5. Casos reales de cliente (ejemplos)

1. **Cliente gaming con presupuesto medio**: Ryzen 5 o Intel i5 actuales, priorizando GPU y buen disipador.
2. **Cliente de edicion de video**: Ryzen 7 / i7 con buen numero de nucleos, 32 GB de RAM y SSD rapido.
3. **Cliente oficina**: CPU eficiente, grafica integrada y bajo consumo.

---

## 6. Errores comunes y como evitarlos

- Comprar CPU sin comprobar **socket** o **chipset**.
- Instalar RAM no compatible con la placa.
- Olvidar el **consumo** y la potencia real de la fuente.
- Recomendar CPU "tope de gama" sin necesidad real.

---

## 7. Procesadores mas actuales (referencia rapida)

**Nota:** listado orientativo con familias anunciadas oficialmente y vigentes a fecha **02/02/2026**.

### Intel (escritorio)

- **Intel Core Ultra 200S (desktop)**: familia presentada el **10/10/2024** como su gama de escritorio mas reciente con NPU integrada para PCs AI.

### Intel (portatil)

- **Intel Core Ultra 200V (mobile)**: familia anunciada el **03/09/2024** para portatiles, con foco en eficiencia y AI PC.
- **Intel Core Ultra 200HX / 200H (mobile)**: familia presentada en **CES 2025** para creadores y gaming en portatil.

### AMD (escritorio)

- **AMD Ryzen 9000 Series (Zen 5)**: familia anunciada el **02/06/2024** para escritorio, con modelos 9950X/9900X/9700X/9600X.
- **AMD Ryzen 7 9850X3D (Zen 5, 3D V-Cache)**: presentado el **05/01/2026** como tope gaming en la linea Ryzen 9000X3D.

### AMD (portatil)

- **AMD Ryzen AI 300 Series (Zen 5)**: familia anunciada el **02/06/2024** para portatiles con NPU dedicada.

---

## Resumen final (ideas clave)

- Intel y AMD se comparan mejor por **compatibilidad, precio y uso real**.
- Arrow Lake y Raptor Lake son referencias recientes en Intel con distintas plataformas.
- Zen define la base de Ryzen y su evolucion explica saltos de rendimiento.
- En el taller, la **compatibilidad** y la **estabilidad** pesan mas que el rendimiento teorico.

---

## Referencias y enlaces

- Arrow Lake (microprocessor) - Wikipedia: https://en.wikipedia.org/wiki/Arrow_Lake_(microprocessor)
- Revision de Intel Arrow Lake (GEEKOM): https://www.geekom.es/revision-de-intel-arrow-lake/
- Intel Core Ultra 200S (desktop) - Intel Newsroom: https://newsroom.intel.com/client-computing/core-ultra-200s-series-desktop
- Intel Core Ultra 200V (mobile) - Intel Newsroom: https://newsroom.intel.com/client-computing/core-ultra-200v-series-mobile
- Intel CES 2025 (Core Ultra 200HX/H) - Intel Newsroom: https://newsroom.intel.com/client-computing/2025-ces-client-computing-news
- Intel Raptor Lake (IONOS): https://www.ionos.mx/digitalguide/servidores/know-how/intel-raptor-lake/
- Zen (microarquitectura) - Wikipedia: https://es.wikipedia.org/wiki/Zen_(microarquitectura)
- Arrow Lake die shot (imagen) - Wikimedia Commons: https://commons.wikimedia.org/wiki/File:Arrow_Lake_die_shot.png
- Intel i9-14900KF (imagen) - Wikimedia Commons: https://commons.wikimedia.org/wiki/File:Intel_i9-14900KF_CPU.jpg
- Zen microarchitecture (imagen) - Wikimedia Commons: https://commons.wikimedia.org/wiki/File:Zen_microarchitecture.svg
- Procesadores AMD Ryzen (Hiraoka): https://hiraoka.com.pe/blog/post/procesadores-amd-ryzen-caracteristicas-rendimiento-gamas
- AMD Zen 5 (El Chapuzas Informatico): https://elchapuzasinformatico.com/2024/03/amd-zen-5-8-operaciones-por-ciclo-doble-decode/
- AMD Zen 5 Ryzen 9000 y Ryzen AI 300 - AMD Newsroom: https://www.amd.com/en/newsroom/press-releases/2024-6-2-amd-unveils-next-gen-zen-5-ryzen-processors-to-p.html
- AMD CES 2026 (Ryzen 9850X3D) - AMD Newsroom: https://www.amd.com/en/newsroom/press-releases/2026-1-5-amd-expands-ai-leadership-across-client-graphics-.html



**Fecha de actualización:** 02/02/2026
