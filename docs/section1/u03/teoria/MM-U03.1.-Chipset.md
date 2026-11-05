---
title: "UD 03 - 3.1 Chipset"
description: "Chipset"
summary: "Chipset"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2026-11-05
icon: "material/file-document-outline"
permalink: /mm/u03/3-1-chipset
categories:
    - "MON"
tags:
    - "chipset"
---

## UD 03. CHIPSET


---

## 0. Vocabulario

<a id="vocabulario"></a>

| Término | Qué es | Para qué sirve / Impacto | Ejemplo / Notas |
|---|---|---|---|
| **Chipset / PCH** | Conjunto de controladores de la placa (en Intel, *Platform Controller Hub*). | Aporta PCIe secundarios, USB, SATA, audio, LAN, sensores, firmware; enlaza con la CPU. | Determina puertos y expansión posibles. |
| **Northbridge (NB)** | Chip “norte” de arquitecturas antiguas. | Gestionaba **memoria** y **gráfica**; conectado a CPU por FSB. | Desapareció al integrarse memoria/PCIe en la CPU. |
| **Southbridge (SB)** | Chip “sur” de arquitecturas antiguas. | E/S “lenta”: SATA/IDE, USB, PCI, audio, LAN, puertos legacy. | Sustituido por PCH único. |
| **FSB** | *Front Side Bus* (bus frontal). | Bus compartido CPU↔NB en PCs antiguos. | Reemplazado por enlaces punto‑a‑punto. |
| **QPI / DMI** | Enlaces Intel (punto‑a‑punto). | Conectan CPU↔CPU (QPI, servidores antiguos) o CPU↔PCH (DMI). | Más ancho = menos cuello de botella al PCH. |
| **HyperTransport (HT)** | Enlace punto‑a‑punto (AMD clásico). | Comunicación de alta velocidad en plataformas anteriores. | Precursor de **Infinity Fabric**. |
| **Infinity Fabric (IF)** | Red interna de AMD. | Une CCDs e I/O Die dentro de la CPU; coordina relojes/memoria. | IF ≈ “autopista” interna de AMD. |
| **IMC (Controlador de memoria integrado)** | Lógica de RAM dentro de la CPU. | Reduce latencia de memoria frente a NB externo. | Presente en CPUs modernas (Intel/AMD). |
| **PCI Express (PCIe)** | Interfaz serie para expansión. | Conecta GPU, NVMe, NICs, capturadoras, etc. | Versiones 3/4/5… con retrocompatibilidad. |
| **Líneas PCIe (x1/x4/x8/x16)** | Número de “hilos” del enlace. | Más líneas = más ancho de banda. | x16 típico para GPU, x4 para NVMe. |
| **Bifurcación PCIe** | División de un enlace en varios. | Permite x8/x8 o x8/x4/x4 desde x16. | Útil para **GPU + 2×M.2**. |
| **M.2** | Factor de forma de módulos. | Soporta NVMe (PCIe) o SATA, y Wi‑Fi (Key E). | Conector clave para SSDs modernos. |
| **NVMe** | Protocolo sobre PCIe para SSD. | Latencia muy baja y alto rendimiento. | Mejor en ranuras conectadas a **CPU**. |
| **SATA / AHCI** | Interfaz y modo de almacenamiento. | Conecta HDD/SSD 2,5"; limitado a 6 Gb/s. | Útil para capacidad, no para máximas velocidades. |
| **RAID / VMD / RAIDXpert** | Tecnologías de agrupación/gestión. | Rendimiento, redundancia o gestión NVMe (Intel VMD / AMD RAIDXpert). | Requieren drivers/UEFI compatibles. |
| **USB 2.0 / 3.x / USB4** | Estándares USB. | Conectividad universal; USB4 permite hasta 40 Gb/s (80 Gb/s en USB4 v2) y DisplayPort Alt Mode. | USB4 depende de controladora/placa. |
| **USB Type‑C / PD / Alt Mode** | Conector y funciones avanzadas. | Carga (Power Delivery) y vídeo por el mismo puerto. | Necesita cableado y controladoras adecuados. |
| **Thunderbolt (TB)** | Protocolo de alta velocidad (Intel). | Datos + vídeo + daisy‑chain; compatible con USB4. | TB4/TB5 en placas de gama alta. |
| **Ethernet 1/2.5/5/10 GbE** | Redes cableadas. | Velocidad de LAN integrada en placa. | 2.5 GbE es común en placas actuales. |
| **CNVi / Wi‑Fi** | Integración Wi‑Fi (Intel) o módulos M.2. | Conectividad inalámbrica integrada. | Depende de módulo y antenas de la placa. |
| **UEFI/BIOS** | Firmware de la placa. | Arranque, opciones de CPU/memoria/PCIe, seguridad. | Actualizaciones añaden soporte de CPU y estabilidad. |
| **Microcódigo** | Parches de CPU cargados por UEFI/OS. | Corrigen/optimizan instrucciones y compatibilidad. | Requieren UEFI actualizado. |
| **TPM / fTPM** | Módulo (físico o firmware) de seguridad. | Cifrado y arranque medido (BitLocker, Secure Boot). | fTPM suele venir en chipsets modernos. |
| **Secure Boot** | Verificación de arranque. | Evita ejecutar firmware/bootloaders no firmados. | Configurable en UEFI. |
| **ASPM / Estados C‑P‑D** | Políticas de ahorro de energía. | Bajada de consumo en enlaces y dispositivos. | Puede aumentar latencia ligeramente. |
| **VRM** | Regulación de voltaje de la placa. | Estabilidad y margen de OC/CPU de alto TDP. | La calidad del VRM importa más que el chipset en OC. |
| **TDP / PL1‑PL2 / PPT** | Límites de potencia (Intel/AMD). | Definen consumo térmico y rendimiento sostenido. | Ajustables en UEFI (según chipset/placa). |
| **Overclock / Undervolt** | Subir frecuencia / bajar voltaje. | Mejora rendimiento/eficiencia si la plataforma lo permite. | Intel “Z”; AMD X‑/B‑series con distintas limitaciones. |
| **XMP / EXPO** | Perfiles de memoria (Intel/AMD). | Carga automática de frecuencias/timings de DDR5. | Requiere módulos y placa compatibles. |
| **IOMMU / VT‑d / SR‑IOV** | Virtualización de E/S. | Asignación directa de dispositivos a VMs, mejor rendimiento. | Útil en servidores/labs. |
| **Retimer / Redriver** | Circuitos para señales de alta velocidad. | Mantienen integridad en USB4/TB/PCIe largos. | Su presencia explica diferencias entre placas. |
| **PHY** | Capa física de una interfaz. | Convierte datos lógicos en señales eléctricas. | Cada estándar (PCIe/USB/Eth) tiene su PHY. |
| **Enlace CPU↔PCH (uplink)** | Conexión principal con el chipset (DMI en Intel; PCIe x4 en AMD). | Límite agregado del tráfico de dispositivos del PCH. | Si saturas USB/NVMe del PCH, este enlace puede ser el cuello. |



---


<a id="introduccion"></a>
## 1. Introducción

El **chipset** es el “centro logístico” de la placa base: coordina el flujo de datos entre CPU, memoria, almacenamiento y periféricos. Determina **qué** puedes conectar (puertos disponibles) y **cómo de rápido** funcionará (versiones y anchos de banda). Elegir bien el chipset condiciona **vida útil**, **ampliaciones** y **estabilidad** del equipo. En plataformas modernas, la CPU asume funciones críticas (memoria y PCIe principal), mientras el chipset concentra **E/S** y servicios de **plataforma** (USB, SATA, audio, red, sensores, temporización, seguridad).

<a id="que-es-un-chipset"></a>
## 2. ¿Qué es un chipset?

Conjunto de controladores que integran la **lógica de plataforma**. En placas actuales suele ser un **único chip** (PCH en Intel; “chipset” o **Promontory** en AMD). Proporciona:
- **Líneas PCIe secundarias** (para M.2 y tarjetas), **USB** (hasta USB4 en gamas recientes), **SATA**, **audio**, **Ethernet**, **BT/Wi‑Fi** integrables, **firmware** (UEFI/BIOS), **TPM/fTPM**, **sensores**.
- Enlace de alta velocidad con la CPU (DMI en Intel, PCIe en AMD; históricamente QPI/HT), gestión de **relojes**, **energía** y **arranque**.

<a id="evolucion-historica"></a>
## 3. Evolución histórica: Northbridge/Southbridge → PCH

### 3.1. Arquitectura clásica (años 90–2000): Northbridge + Southbridge
Antes se usaban **dos chips**:
- **Northbridge (NB):** comunicado con la CPU por **FSB**; alojaba el **controlador de memoria** y el **bus gráfico** (AGP y, posteriormente, el primer PCIe x16).  
- **Southbridge (SB):** enlazado al NB; gestionaba **almacenamiento** (IDE→SATA), **USB**, **PCI/PCIe secundarios**, **audio**, **red**, **RTC**, **puertos legacy** (PS/2, serie, paralelo), **BIOS**, sensores.

```
CPU  <== FSB ==>  Northbridge  <== enlace interno ==>  Southbridge
 |                    |   \
 |                    |    \__ AGP / PCIe x16 (gráfica)
 |                    \__ Controlador de memoria (RAM)
```

<div style="text-align: center;">
  <img src="../assets/northsouthbridge_hd.png" alt="Esquema de la arquitectura clásica: CPU, Northbridge con RAM y gráficos (AGP/PCIe), y Southbridge con PCI, audio, SATA, USB y LAN" style="display: block; margin: 0 auto; max-width: 60%; height: auto;">
</div>

**Implicaciones didácticas:**
- El **rendimiento de la RAM** dependía del **NB**; cada salto de CPU/RAM exigía un NB nuevo.
- La **GPU** se conectaba al NB para minimizar latencia con la CPU.
- La **E/S** “lenta y media” recaía en el **SB** (discos, USB, PCI), con más latencia.

### 3.2. Transición: integración en CPU y enlaces punto a punto
Con nuevas arquitecturas:
- El **controlador de memoria** se **integró en la CPU** (primero en AMD de escritorio, luego generalizado).
- El **FSB** se reemplazó por enlaces **punto‑a‑punto** de alta velocidad (QPI/DMI en Intel; HyperTransport y, hoy, enlace PCIe en AMD).
- La CPU asumió el **PCIe principal** (para GPU/M.2 rápidos); el NB perdió protagonismo.

<div style="text-align: center;">
  <img src="../assets/typical_intel_chipset.jpg" alt="Diagrama de un chipset Intel de transición: CPU con Front Side Bus hacia el Northbridge, enlace DMI hacia el Southbridge y periféricos (PCI Express, SATA, USB, audio HD, BIOS)" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

### 3.3. Modelo moderno: PCH (Platform Controller Hub)
- La **CPU** integra: controlador de **memoria** y **líneas PCIe** principales (x16 para GPU, x4/x8 para M.2 rápidos), además de funciones de **seguridad** y aceleradores.
- El **PCH/chipset** aporta: **PCIe secundarios**, **USB**, **SATA**, **audio**, **Ethernet**, **firmware**, **TPM/fTPM**, **sensorística**; se comunica con la CPU por **DMI** (Intel) o **PCIe** (AMD).

```
RAM <——> CPU  <== enlace de plataforma (DMI/PCIe) ==>  PCH (chipset)
         |  \_______________________________  USB, SATA, PCIe secundarios,
         \— PCIe CPU (GPU/M.2 rápidos)       audio, LAN, sensores, firmware…
```

### 3.4. ¿Por qué cambió?
- **Menos latencia, más rendimiento:** memoria y PCIe principal en la **CPU**.
- **Eficiencia energética/térmica:** menos saltos de chips → menos consumo/calor.
- **Escalabilidad:** enlaces punto‑a‑punto y asignación flexible de **PCIe**.
- **Simplificación de plataforma** y mayor **fiabilidad**.


<a id="arquitectura-general"></a>
## 4. Arquitectura general del chipset

El chipset moderno funciona como **hub** de E/S:
- **Switching PCIe** hacia ranuras x1/x4 y M.2 secundarios.
- **Controladoras** USB 2.0/3.x/USB4, **SATA** para HDD/SSD, **audio** HD, **Ethernet** (MAC/PHY según placa), buses **SPI/I²C/UART** para firmware y sensores.
- **Relojería** (clocking) y **gestión de energía** (Estados C/P, ASPM) coordinadas con la CPU.

<a id="enlace-con-la-cpu"></a>
### 4.1. Enlace con la CPU (FSB, DMI, PCIe, QPI/HT)
- **Ayer:** **FSB** compartido (CPU↔NB).  
- **Hoy:** **DMI** (Intel) o un enlace **PCIe x4** (AMD) como enlaces **punto‑a‑punto** dedicados, con varias **líneas** y **generaciones** (ej.: DMI 4.0 x8 en Intel Z790 y Z890; DMI 4.0 x4 en B860/H810; PCIe 4.0 x4 en AMD serie 800). **Infinity Fabric** es la interconexión interna de la CPU, no el enlace con el chipset.

<a id="hub-interno"></a>
### 4.2. Hub interno y distribución de señales
Multiplexa líneas **PCIe** y controla el **ancho de banda agregado** hacia la CPU por el enlace de plataforma. La placa decide cómo repartir las **líneas físicas** entre ranuras y M.2.

<a id="relojes-y-latencias"></a>
### 4.3. Relojes, temporización y latencias
Gestiona **relojes** de alta precisión y políticas de ahorro (ASPM, estados D), que influyen en **latencia** y **consumo**. Un mal ajuste puede provocar **throttling** o inestabilidad.

<a id="compatibilidad-de-sockets"></a>
## 5. Compatibilidad de sockets y generaciones de CPU

El chipset y el **socket** determinan qué **familias de CPU** puedes usar. Además, la **UEFI/BIOS** debe incluir **microcódigos** compatibles con la CPU para que arranque.

<a id="microcodigos-y-uefi"></a>
### 5.1. Revisión de microcódigos y BIOS/UEFI
Actualizaciones de UEFI aportan **soporte de nuevas CPUs**, arreglos de **estabilidad** y mejoras de **memoria** (XMP/EXPO).

<a id="limites-tdp"></a>
### 5.2. Límites de TDP y soporte de características de la CPU
Aunque la CPU encaje, la **alimentación (VRM)** y el **firmware** de la placa marcan límites (p. ej., curvas de potencia, opciones de overclock/undervolt).

<a id="pcie"></a>
## 6. PCI Express

<a id="pcie-version"></a>
### 6.1. Versión y retrocompatibilidad
PCIe es **retrocompatible** por versión y ancho de enlace. La **versión** (3.0/4.0/5.0/…) afecta al **rendimiento por carril**; el **ancho** (x1/x4/x8/x16) define el caudal total.

<a id="pcie-reparto"></a>
### 6.2. Reparto de líneas: CPU vs chipset
- **CPU:** líneas rápidas (normalmente x16 para GPU + x4/x8 para M.2 de altas prestaciones).  
- **Chipset:** líneas adicionales (x1/x2/x4) para M.2 extra, NICs, capturadoras, etc. Todo ese tráfico **compite** por el enlace CPU↔PCH.

<a id="pcie-topologias"></a>
### 6.3. Topologías típicas (x16, x8/x8, x4 para M.2, bifurcación)
- Bifurcación del x16 de la CPU en **x8/x8** (SLI/CrossFire antiguos) o **x8/x4/x4** para combinar **GPU + 2×M.2**.
- En chipsets con **USB4/Thunderbolt**, parte del ancho proviene de PCIe internos y PHYs dedicados.

<a id="almacenamiento"></a>
## 7. Almacenamiento

<a id="sata"></a>
### 7.1. SATA (puertos, modos AHCI/RAID)
Aún útil para HDD/SSD 2,5", pero limitado por **6 Gb/s** en SATA 3.0. Muchos chipsets ofrecen **RAID** por firmware.

<a id="nvme-m2"></a>
### 7.2. NVMe/M.2 (PCIe x4, bifurcación, disipación)
Los **NVMe** M.2 enlazados a la **CPU** rinden más (menos latencia) que los colgados del **chipset**. Requieren **disipación** por su densidad térmica.

<a id="raid-y-vmd"></a>
### 7.3. RAID/RST, VMD y RAIDXpert (visión general)
- **Intel RST/VMD**: gestión avanzada de NVMe/RAID vía firmware/driver.  
- **AMD RAIDXpert**: solución análoga en plataformas AMD.

<a id="usb"></a>
## 8. Conectividad USB

<a id="usb-estandares"></a>
### 8.1. Estándares (2.0/3.x/USB4) y velocidades
- **USB 3.x** (5/10/20 Gb/s).  
- **USB4** reutiliza tecnología Thunderbolt para alcanzar **40 Gb/s** (**80 Gb/s** en USB4 v2), con compatibilidad DP Alt Mode.

<a id="usb-tipo-c"></a>
### 8.2. Tipo‑C, Alternate Mode y Power Delivery (PD)
Type‑C permite **PD** (carga rápida) y **video** por **Alt Mode**; el soporte real depende del **controlador** y el **cableado** de la placa.

<a id="redes"></a>
## 9. Redes integradas

<a id="ethernet"></a>
### 9.1. Ethernet (1/2.5/5/10 Gb)
Cada vez más común **2.5GBASE‑T** nativo. En gamas altas aparecen **5/10 GbE** vía controladoras PCIe adicionales.

<a id="wifi-bt"></a>
### 9.2. Wi‑Fi/Bluetooth (CNVi/PCIe)
Módulos **M.2 Key E** (Intel/Realtek/Qualcomm) o soluciones **CNVi**/RFFE integradas según plataforma y placa.

<a id="audio"></a>
## 10. Audio y códecs integrados (ALC, S/PDIF, front panel)
Códecs **Realtek ALC** y similares, con soporte para **S/PDIF**, **jack frontales** y mejoras por **opamps**/aislamiento PCB en placas gaming/creator.

<a id="controladoras"></a>
## 11. Controladoras y E/S adicionales

<a id="thunderbolt-usb4"></a>
### 11.1. Thunderbolt/USB4 (cuando procede)
Algunas placas integran **USB4**/Thunderbolt (controladoras dedicadas + redriver/retimer).

<a id="puertos-legacy"></a>
### 11.2. Puertos legacy (SPI, UART, PS/2)
Aún presentes en placas orientadas a **empresa/industria** y para compatibilidad.

<a id="energia-termicas"></a>
## 12. Gestión de energía y térmicas

<a id="aspm"></a>
### 12.1. Estados C/P, ASPM y ahorro de energía
El chipset negocia **ASPM** y estados **D** de dispositivos. Afecta a consumo y latencia.

<a id="vrm-pch"></a>
### 12.2. VRM de placa y consideraciones térmicas del PCH
El **PCH** suele estar bajo un **disipador**; en placas con **USB4/PCIe 5** puede calentarse más. La calidad del **VRM** condiciona estabilidad.

<a id="overclock-undervolt"></a>
## 13. Overclock/Undervolt y límites de plataforma
Las opciones dependen de **CPU + chipset + UEFI**. En Intel serie Z es donde hay más control; en AMD, gamas **X8xx/B8xx** ofrecen OC de memoria/IF.

<a id="familias-chipsets"></a>
## 14. Ejemplos de familias de chipsets (visión comparativa)

<a id="intel-familias"></a>
### 14.1. Intel (series 700/800 y 900 prevista)
- **700 (Z790/B760/H770, etc.)**: enlace **DMI 4.0** (hasta x8), hasta **~28 líneas PCIe** en PCH, combinación **PCIe 4.0/3.0**, SATA y abundante USB.  
- **800 (Z890/B860/H810, etc.)** para **Arrow Lake** y **Arrow Lake Refresh** (Core Ultra 200S desde 2024 y 200S Plus desde marzo de 2026): Z890 con **DMI 4.0 x8** y 24 líneas **PCIe 4.0** en el PCH; B860 y H810 con **DMI 4.0 x4** y menos líneas. Solo Z890 permite overclock de CPU; B860 admite overclock de memoria y H810 no admite ninguno. USB4/Thunderbolt y Wi‑Fi 7 dependen de la placa.
- **900 (Z990/Z970/W980/Q970/B960)** *(prevista, no confirmada)*: chipsets para **Nova Lake** (Core Ultra 400) y el socket **LGA 1954**; según filtraciones, sin gama H, con más líneas **PCIe 5.0** y lanzamiento entre finales de 2026 y el primer trimestre de 2027.  
- Notas comunes: la **CPU** aporta PCIe para **GPU** y NVMe rápidos; el **PCH** añade puertos y líneas secundarias. Consulta siempre el **manual** de la placa para el reparto exacto.

<div style="text-align: center;">
  <img src="../assets/z790_block_diagram.jpg" alt="Diagrama de bloques del chipset Intel Z790: CPU con PCIe 5.0/4.0 y memoria DDR5/DDR4, enlace DMI 4.0 x8 y chipset con 20 líneas PCIe 4.0, 8 PCIe 3.0, SATA, USB y Ethernet" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

<a id="amd-familias"></a>
### 14.2. AMD (AM4 y AM5: X670/B650 → X870/B850/B840)
- **AM4 (X570/B550/B450, etc.)**: PCIe 4.0 generalizado en gamas X570; B550 con mezcla CPU‑PCIe 4 + PCH‑PCIe 3.  
- **AM5 600‑series (X670/X670E, B650/B650E, A620)**: salto a **DDR5** y **PCIe 5** (en “E” para GPU/SSD).  
- **AM5 800‑series (X870E/X870/B850/B840)**: estandarizan **DDR5**, hacen **USB4** obligatorio en X870E/X870 (opcional en B850/B840) y consolidan **PCIe 5** (sobre todo para NVMe, y en **X870E** también para GPU). Cambios de segmentación frente a B650 (algunos B850 desactivan PCIe 5 x16 para GPU).
- **Enlace con la CPU:** en AM5 el chipset se conecta por **PCIe 4.0 x4**, no por Infinity Fabric (≈8 GB/s por sentido, compartidos por todo lo que cuelga del chipset).
- **Promontory 21 y cadena de chips:** *Promontory 21* es el chip de chipset de AM5 (fabricado por ASMedia). Las placas X670, X670E y X870E montan **dos** en **cadena** (*daisy chain*): el primero se conecta a la CPU por PCIe 4.0 x4 y el segundo se conecta al primero por otro PCIe 4.0 x4, no directamente a la CPU. Así la placa dispone de más USB, SATA, M.2 y líneas PCIe, pero todo el tráfico del segundo chip pasa por el primero y comparte el mismo enlace único con la CPU (posible cuello de botella). En gamas más bajas, como B650, basta con un solo chip.

```
CPU ==PCIe 4.0 x4==> Promontory 21 (chip 1) ==PCIe 4.0 x4==> Promontory 21 (chip 2)
                     USB, SATA, M.2, PCIe…                    USB, SATA, M.2, PCIe…
```
- **Transición:** desde 2025 AMD dejó de producir B650 y B850 es la gama media. Se rumorea que los Ryzen **Zen 6** (Olympic Ridge) llegarán en 2027 sobre AM5 (sin confirmar), por lo que las placas serie 800 deberían seguir vigentes.

<div style="text-align: center;">
  <img src="../assets/amd_b450_chipset.jpg" alt="Chipset AMD de la serie 400 (AM4) montado en una placa base" style="display: block; margin: 0 auto; max-width: 40%; height: auto;">
</div>

---

## 15. Chipsets actuales (Intel & AMD) — Tabla comparativa


### 15.1. Intel (desktop, serie 800 – LGA 1851)

| Chipset | Socket | CPU objetivo | Memoria | PCIe clave (desde CPU / desde chipset) | USB / Thunderbolt | Almacenamiento | Overclock |
|---|---|---|---|---|---|---|---|
| **Z890** | LGA 1851 | Core Ultra (Series 2, “Arrow Lake‑S”) | **DDR5** | **CPU:** PCIe 5.0 (config. típicas 1×16+1×4 o 2×8+1×4); **PCH:** 24 líneas PCIe 4.0 con DMI 4.0 x8 (según placa) | USB 3.2 abundante; **USB4/TB** según placa (no estándar del PCH) | NVMe **PCIe 5** directo a CPU (≥1×4); **SATA** según placa | **CPU+BCLK+memoria** (chipset Z) |
| **B860** | LGA 1851 | Core Ultra (Series 2) | **DDR5** | **CPU:** PCIe 5.0 (GPU y NVMe; algunas fuentes indican menos líneas de CPU que Z890); **PCH:** ~14 líneas PCIe 4.0 y DMI 4.0 x4 | USB 3.2; **USB4/TB** opcional (según placa) | NVMe PCIe 5 (CPU) + puertos desde chipset; SATA según placa | **Memoria** (sin OC de CPU) |
| **H810** | LGA 1851 | Core Ultra (Series 2) | **DDR5** | **CPU:** PCIe 5.0 1×16 (GPU); **PCH:** ~8 líneas PCIe 4.0 y DMI 4.0 x4 (menos puertos) | USB 3.2 básico + USB 2.0; funciones recortadas | NVMe solo desde el PCH; SATA limitado | **Ninguno** (ni CPU, BCLK ni memoria/XMP) |

---

### 15.2. AMD (desktop, AM5 serie 800)

| Chipset | Socket | CPU objetivo | Memoria | PCIe clave (GPU / SSD) | USB4 | Almacenamiento | Overclock |
|---|---|---|---|---|---|---|---|
| **X870E** | AM5 | Ryzen 9000 / 7000 | **DDR5 (EXPO)** | **PCIe 5.0 GPU** + **PCIe 5.0 NVMe** directos a CPU; más líneas totales que X870 | **Sí** (estándar en X870/X870E) | NVMe PCIe 5 (CPU) + adicionales por chipset; SATA según placa | **CPU+memoria** |
| **X870** | AM5 | Ryzen 9000 / 7000 | **DDR5 (EXPO)** | **PCIe 5.0 GPU** + **PCIe 5.0 NVMe** directos a CPU | **Sí** (estándar) | NVMe PCIe 5 + SATA según placa | **CPU+memoria** |
| **B850** | AM5 | Ryzen 9000 / 7000 | **DDR5 (EXPO)** | **PCIe 5.0 NVMe obligatorio**; **PCIe 5 x16 GPU** **opcional** según placa | **Opcional** (según placa) | NVMe PCIe 5 (mín. 1×4 por norma B850) + SATA | **CPU+memoria** (menos opciones que X870) |
| **B840** | AM5 | Ryzen 9000 / 7000 (recorte) | **DDR5** | Enfoque **PCIe 4.0** para GPU/E/S desde chipset; menos líneas totales | **Opcional** | NVMe PCIe 4 (habitual desde PCH) + SATA | **Limitado** (gama de entrada) |

---

**Fecha de actualización:** 05/11/2026
