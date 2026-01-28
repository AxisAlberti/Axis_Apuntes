---
title: "UD 02 - 2.1 Componentes internos del PC"
description: "Componentes internos del PC"
summary: "Componentes internos del PC"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2025-10-01
icon: "material/file-document-outline"
permalink: /mm/u02/2-1-componentes-internos-del-pc
categories:
    - "MON"
tags:
    - "componentes"
---

## TEMA 2. COMPONENTES INTERNOS


---

# 0. Definición y Función General (Placa base)

La **placa base** (también conocida como **tarjeta madre** o **motherboard**) es el **componente principal** de cualquier ordenador.  
Actúa como el **núcleo de interconexión** entre todos los dispositivos del sistema: procesador, memoria RAM, almacenamiento, tarjeta gráfica, periféricos y alimentación eléctrica.

---

La placa base es un **circuito impreso multicapa (PCB)** sobre el que se integran **zocalos, ranuras, puertos y chips** que permiten la comunicación entre los diferentes elementos del sistema informático.

Su diseño y arquitectura determinan:
- Qué **procesadores** y **memorias** son compatibles.  
- Qué tipo y número de **conexiones de expansión** (PCIe, M.2, SATA) soporta.  
- Qué **funciones integradas** (red, audio, gráficos, USB) incorpora.  
- Cómo se distribuye la **alimentación eléctrica** a cada componente.

En términos técnicos, la placa base actúa como una **plataforma de control y comunicación** entre el hardware y el firmware del equipo.

---

El objetivo de la placa base es **coordinar y conectar** todos los componentes para que funcionen de forma conjunta, gestionando:

| Función | Descripción | Componentes implicados |
|----------|-------------|------------------------|
| **Interconexión de datos** | Transmisión de información entre CPU, RAM, almacenamiento y periféricos. | Chipset, buses, controladores. |
| **Distribución eléctrica** | Reparte la energía del suministro (PSU) a cada componente. | VRM, conectores ATX/EPS. |
| **Comunicación y control** | Gestiona señales, interrupciones y prioridades. | Chipset, BIOS/UEFI. |
| **Expansión y conectividad** | Permite agregar dispositivos adicionales. | Ranuras PCIe, M.2, USB. |
| **Sincronización del sistema** | Control de reloj y temporización. | Chipset, generador de reloj. |

---

# 0.1 Principales Fabricantes de Placas Base (2025)

## 0.1.1 Panorama Actual

El mercado de placas base está dominado por **cuatro grandes fabricantes** que concentran la mayoría de modelos disponibles tanto para procesadores **Intel** como **AMD**:

| Fabricante | País de origen | Gamas destacadas | Características |
|-------------|----------------|------------------|-----------------|
| **ASUS** | Taiwán | ROG, TUF, PRIME, PROART | Innovación, calidad y BIOS muy completas |
| **MSI** | Taiwán | MPG, MAG, MEG | Excelente refrigeración y estabilidad eléctrica |
| **Gigabyte** | Taiwán | AORUS, ULTRA DURABLE | Relación calidad/precio, durabilidad |
| **ASRock** | Taiwán | Phantom Gaming, Steel Legend | Buenas opciones en gama media y mini-ITX |

---

## 0.1.2 Fabricantes Secundarios o OEM

Además de los principales, existen marcas **OEM** (Original Equipment Manufacturer) que producen placas para fabricantes de equipos completos:

| Fabricante | Clientes principales | Observaciones |
|-------------|----------------------|----------------|
| **Foxconn** | HP, Dell, Apple | Producción a gran escala |
| **Pegatron** | ASUS, Lenovo | OEM de bajo coste |
| **Biostar** | Mercado doméstico | Alternativa económica |

---

## 0.1.3 Innovaciones Recientes (2024–2025)

- Soporte **PCIe 5.0 y DDR5** en gamas medias.
- Placas **con Wi-Fi 7** integrado.
- **VRM digitales** de 20 fases o más.
- Implementación de **M.2 25110** (formatos extendidos).
- Integración de **conectores 12VHPWR (PCIe 5.0)**.
- Mayor soporte para **BIOS actualizable vía red (Flashback / EZ Flash)**.

---

## 0.1.4 Criterios de Selección para Técnicos

- Compatibilidad con CPU y formato de memoria.
- Calidad de VRM y refrigeración.
- Conectividad: número de M.2, USB, PCIe.
- Facilidad de mantenimiento y actualización de firmware.
- Disponibilidad de soporte técnico y garantía.

---

# 1. Vocabulario Fundamental

| **Término** | **Definición** |
|--------------|----------------|
| **Cuello de botella** | Limitación de rendimiento causada porque un componente (CPU, GPU, RAM, SSD) es más rápido que el resto de la cadena y la transmisión de datos se ve frenada; hoy afecta sobre todo a buses y almacenamiento en gaming de alta gama. |
| **Coma flotante** | Notación para representar números reales con mucha precisión, clave en procesadores y sobre todo en IA moderna y tarjetas gráficas, que ahora realizan trillones de cálculos de coma flotante por segundo. |
| **Factor de forma** | Estándar físico de placas base y chasis: ATX, MicroATX, MiniITX, y el nuevo BTF (Back To Front) en cableado oculto; las RAM CAMM2 empiezan a desplazar a SO-DIMM en portátiles. |
| **Fan (ventilador)** | Elemento crítico de refrigeración. Actualmente la mayoría incluyen control digital (PWM), sensores de temperatura y efecto RGB sincronizable. |
| **FSB (Front Side Bus)** | Bus frontal ya obsoleto, sustituido hoy por buses PCIe, DMI (Intel) o Infinity Fabric (AMD). |
| **Gigahercio (GHz)** | Unidad de frecuencia. Las CPUs actuales alcanzan más de 5.5 GHz y la RAM DDR5 para gaming puede funcionar a más de 8000 MHz. |
| **Memoria flash** | Base tecnológica de los SSDs NVMe y UltraRAM, que superan en velocidad a los discos SATA convencionales. |
| **Nanosegundo (ns)** | Tiempo mínimo de acceso en chips RAM y SSD. En memorias de gama alta se alcanzan valores de 7–12 ns. |
| **Nanómetro (nm)** | Milmillonésima parte de un metro; hace referencia al proceso de fabricación de chips: las tecnologías de 3 nm y 4 nm dominan en CPUs y GPUs modernas. |

---


# 2. Factor de forma

El **factor de forma** define las dimensiones físicas, el diseño de los conectores y la organización interna de la placa base, lo que determina la compatibilidad con chasis, fuentes de alimentación y componentes. Elegir el adecuado afecta la capacidad de expansión, refrigeración, estética y futuro upgrade del sistema.

---

<div style="text-align: center;">
  <img src="assets/componentes/16.png" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

## 2.1 Concepto y importancia

- Un factor de forma es un estándar que dicta cómo se fabrican y disponen las placas base y sus componentes. Su objetivo es garantizar compatibilidad entre placas, torres y demás hardware modular.
- Afecta a: Número y tipo de ranuras de expansión (PCIe, M.2, RAM).

---

## 2.2 Factores de forma más utilizados (2025)

| Factor de forma   | Dimensiones (mm) | Puestos de expansión | Uso principal                | Compatibilidad chasis      |
|-------------------|------------------|----------------------|------------------------------|----------------------------|
| ATX               | 305 x 244        | 7 PCIe + 4–8 RAM     | Gaming, workstation, desktop | Universal                  |
| MicroATX          | 244 x 244        | 4 PCIe + 2–4 RAM     | Oficina, gaming compactos    | ATX/MicroATX               |
| MiniITX           | 170 x 170        | 1 PCIe + 2 RAM       | HTPC, ultracompactos, SFF    | Mini/micro ATX, ITX        |
| E-ATX             | 305 x 330        | 8 PCIe + 8 RAM       | Workstation, gaming extremo  | Full Tower, E-ATX          |
| XL-ATX            | Hasta 345 x 262  | 8+ PCIe + 8+ RAM     | Servidor         | Full Tower XL, server rack |
| DTX/Mini-DTX      | 203 x 244/170x203| 2 PCIe + 2 RAM       | SFF, embebidos, industria    | Mini/Micro ATX, DTX        |
| BTF/Back Connect  | Variable         | Mismas que ATX/ITX   | PC moderno cableado limpio   | Chasis BTF homologados     |
| CAMM2             | N/A (RAM modular)| —                    | Portátiles premium, SFF      | Cajas y disipadores específicos |

---

## 2.3 Detalle de factores actuales
**ATX:**
El estándar dominante: admite sistemas exigentes de gaming y trabajo, multiGPU, muchas unidades M.2/SATA y RAM. Excelente ventilación.

**MicroATX:**
Más compacto, ideal para equipos medios y oficinas; se puede instalar en cajas ATX. Permite menos expansión pero suficiente para la mayoría de usuarios.

**MiniITX:**
El más pequeño en desktop. Ideal en builds minimalistas, HTPC y setups compactos. Limitación clara de expansión y refrigeración.

**E-ATX / XL-ATX:**
Formato grande: más ranuras y espacio para refrigeración extrema, ideal para workstations, creadores, servidores domésticos.

**DTX / MiniDTX / NanoITX / PicoITX:**
Formatos industriales y embebidos. Usados en IoT, robótica, aplicaciones custom. Limitación absoluta de expansión.

**BTF/Back Connect:**
Concepto moderno donde el cableado va oculto en el reverso de la placa, facilitando airflow, limpieza visual y builds “premium”.

**CAMM2:**
Solo para portátiles premium y workstations compactas. Permite módulos de RAM plug&play, máxima densidad y fácil instalación.

**Formato propietario:**
Usado en OEM y all-in-one, dificultad de actualización e intercambios.

---

## 2.4 Tabla comparativa resumida

| Nombre     | Expansión Máx. | Dimensiones | Uso                       | Expansibilidad |
|------------|----------------|-------------|---------------------------|----------------|
| ATX        | Alta           | 305x244     | Gaming general, workstation| Muy alta        |
| MicroATX   | Media          | 244x244     | Oficina, gaming compacto  | Alta            |
| MiniITX    | Baja           | 170x170     | SFF, media center         | Media           |
| E-ATX      | Muy alta       | 305x330     | Workstation, multi-GPU    | Máxima          |
| BTF        | Variable       | Variable    | Builds cableado premium   | Muy alta        |
| CAMM2      | —              | —           | Portátiles premium        | Modular RAM     |

---

## 2.5 Recomendaciones
- Para gaming y workstation: ATX, E-ATX o BTF si buscas máxima capacidad y estética.
- Para oficinas o PCs compactos: MicroATX o MiniITX.
- Para portátiles o máquinas plug&play: verifica compatibilidad CAMM2 para upgrades futuros.
- Evita formatos propietarios salvo equipos OEM o necesidades muy específicas.

---

# 3 Chasis o Caja del pc

## 3.1 Partes principales modernas

- **Cubierta**: Acero galvanizado, paneles laterales de cristal templado, sistemas magnéticos y modulares.
- **Panel frontal**: Botones táctiles, displays LCD/AMOLED (monitoreo en tiempo real), puertos USB-C, USB 4.0, salida/entrada audio, pantalla de temperatura y carga.
- **Bahías internas**: Principalmente slots M.2 y 2.5"/3.5" (con tendencia a M.2). Las bahías externas (5,25") van desapareciendo.
- **Fuente alimentación**: Zona separada, formato ATX 3.0/SFX-L, modulable y con soporte para GPU PCIe 5.0.

---

## 3.2 Factor de Forma y Tipos

| Tipo                  | Fit/Expansión        | Ventajas                  | Limitaciones/Contexto                    |
|-----------------------|----------------------|---------------------------|------------------------------------------|
| Barebone/MiniPC       | 1–2 slots            | Compacto, bajo consumo    | Sin expansión, solo tareas ligeras       |
| Mini Torre/MiniITX    | 2–3 slots RAM, 1 GPU | Compacto y versátil       | Una sola GPU, limitada RL                |
| Mid Tower/Mediatorre  | 4–6 slots            | Balance expansión/tamaño  | Espacio justo para triple ventilador     |
| Torre/Full Tower      | 10+ slots, 3 GPU     | Workstation/gaming top    | Muy grande/pesada, para entusiastas      |
| Servidor/Rack         | Bayas U, redundantes | Eficiencia y redundancia  | Uso profesional, no doméstico            |

---

## 3.3 Paneles y cableado moderno

- **Panel trasero:** Salida múltiple para todos los periféricos.
- **Panel frontal:** Control RGB, pantalla LCD, puertos tipo C/a, quick charge, ranuras para docking SSD hot swap.
- **Paneles inteligentes:** Chasis actuales integran softwares propios y sensores.
- **Gestión cableado:** Sistema BTF y anclajes, todo oculto y preparado para montar/disponer fácil, seguro y exigente para IA y gaming de alto consumo.

---

## 3.4 Consejos prácticos

- **Airflow** primero: elige chasis con múltiples entradas/salidas de aire y zonas amplias para radiadores.
- **Compatibilidad**: Antes de comprar/montar, comprueba soportes de GPU largas, PSU potentes, y placas con headers modernizados.
- **RGB y monitoreo**: Aprovecha headers y software de placas/cajas modernas para crear un PC funcional y visualmente atractivo, además de seguro.

---

# 4. Conectores

## 4.1 Conectores Externos

| Conector        | Uso                    | Detalles técnicos        | Ejemplo de uso          |
|-----------------|------------------------|------------------------------|-------------------------|
| **RJ-45**       | Red LAN; Multi-Gig     | Hasta 10 GbE (Cat7/8)        | Conexión de red doméstica o profesional, transmisión 4K/8K |
| **Wi-Fi 6E/7**  | Inalámbrico            | Hasta 10 Gbps, baja latencia | Placas con antena integrada para gaming/pro y VR           |
| **USB-A/C/USB4**| Periféricos/alimentación| Hasta 80 Gbps (USB4 Type-C), Thunderbolt 4| Soporte para monitores, disks, móviles, hubs, carga rápida|
| **HDMI 2.1**    | Vídeo/audio digital    | Hasta 8K/120Hz, eARC         | Monitores 4K-8K, TVs, VR                                  |
| **DisplayPort 2.1**| Vídeo profesional   | Hasta 16K/60Hz, 240Hz en 4K  | Edición, simulación, triple monitor                       |
| **Audio analógico**| Audio multicanal    | Jack 3,5 mm, hasta 7.1 canales| Juegos, grabación, streaming                             |
| **TOSLINK**     | Audio óptico           | Multicanal sin ruido         | Cine en casa, audio digital puro                          |
| **Thunderbolt 4**| Datos/vídeo/energía   | 40 Gbps, hasta 240W de carga | Docking, monitores, red ultra rápida                      |

---

<div style="text-align: center;">
  <img src="assets/componentes/6.png" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

## 4.2 Conectores Internos (Desarrollado y Ampliado)
Los conectores internos conectan la placa base con todos los componentes críticos: almacenamiento, gráficos, alimentación y paneles del chasis. Son clave tanto en rendimiento como en facilidad de mantenimiento y actualización.

---

### 4.2.1   SATA III (Serial ATA Revisado)**

- **Definición**: Conector para discos HDD, SSD y unidades ópticas.
- **Características**:
  - Velocidad: **6 Gbps** máx.
  - Conexión punto a punto, con cables diferenciados para datos y alimentación (SATA power).
  - Persisten en placas modernas por compatibilidad, aunque pierden peso frente a M.2/NVMe.
- **Usos actuales**: HDD de almacenamiento barato, SSD económicos.

---

<div style="text-align: center;">
  <img src="assets/componentes/7.png" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

### 4.2.2   M.2 (Socket sobre placa base)**

- **Definición**: Ranura compacta multifunción (SSD NVMe/SATA, Wi-Fi, Bluetooth, expansión).
- **Características**:
  - Protocolos: **NVMe PCIe x4/x5/x8** o **SATA**.
  - Velocidad: Hasta **16 GB/s** (PCIe 5.0); PCIe 6.0 en sector servidor.
  - Longitudes: 2242, 2260, 2280, 22110 (nomenclatura: ancho-largo en mm).
  - Claves: B (SATA/PCIe x2), M (PCIe x4/x8), E (Wi-Fi/Bluetooth).
- **Ventajas**: Sin cables, máxima velocidad, ideal para gamer y ultrabooks.
- **Usos**: SSD ultrarrápidos, Wi-Fi 7, Bluetooth 5.3, aceleradoras compactas.

  ---

<div style="text-align: center;">
  <img src="assets/componentes/8.png" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

### 4.2.3  PCI Express (PCIe)

- **Definición**: Bus de expansión para GPU, red, sonido, capturadoras, almacenamiento avanzado.
- **Características**:
  - Ranuras: x1, x4, x8, x16, seleccionable según componente.
  - Velocidades: PCIe 4.0/5.0 mainstream; PCIe 6.0 (128 GB/s, x16) ya en workstation y servidores.
  - Modularidad y máxima velocidad para tarjetas gráficas y periféricos de alto caudal.
- **Usos actuales**: Gráficas RTX/RADEON, NVMe para IA, redes 10GbE+, tarjetas streaming.

  ---

<div style="text-align: center;">
  <img src="assets/componentes/17.png" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

### 4.2.4  Conectores de Alimentación internos

- **ATX 24 pines**: Alimenta la placa base completa.
- **EPS 4+4/8+8 pines**: Alimentación adicional directa para CPU multinúcleo/alto consumo.

---

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="assets/componentes/18.png" alt="Imagen 1" width="45%">
  <img src="assets/componentes/20.png" alt="Imagen 2" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

<div style="text-align: center;">
  <img src="assets/componentes/19.png" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

- **PCIe 6/8/12 pines (12VHPWR)**: Power para GPUs PCIe 5.0 y superiores (soportan hasta 600W).
- **SATA Power**: Discos, ventiladores especiales, accesorios modernos.
- **Molex**: Ya solo para relés y algunos ventiladores más antiguos o retroiluminación LED clásica.
- **Notas actuales**: Fuentes actuales (ATX 3.0 o SFX-L) son modulares: solo instalas los cables necesarios.

### 4.2.5 Headers para el panel frontal y periféricos

- **Front Panel Header (PWR_SW, RESET, LEDs, Speaker)**: Manejo del encendido, reseteo y diagnóstico acústico.

  ---

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="assets/componentes/21.png" alt="Imagen 1" width="45%">
  <img src="assets/componentes/22.png" alt="Imagen 2" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---
- **USB 2.0/3.x/4 Headers**: Permiten que el frontal o parte superior del chasis tenga puertos modernos.
- **HD Audio Header**: Conexión directa a placa para auriculares y micrófono frontal.
- **RGB/ARGB Headers (5V/12V)**: Control de toda la iluminación inteligente y sincronizable del equipo.
- **PWM Fan/Pump Headers**: Permiten monitorizar y regular automáticamente todos los ventiladores y bombas de agua (RL).

---

### 4.2.6 Otros conectores relevantes
- **U.2**: Para SSDs empresariales de máximo rendimiento.
- **TPM header**: Seguridad por hardware profesional.
- **Clear CMOS/BIOS Flashback**: Reajuste rápido del firmware de la placa (útil en overclocking o recuperaciones extremas).

---

# 5 **Zócalo del Procesador (Socket)**

**El socket es el tipo de conector eléctrico y mecánico donde se instala el procesador. Existen diferentes tecnologías y formatos:**

## 5.1. Tipos de Socket

- **LGA (Land Grid Array):**
  - *Pines en el socket, contactos planos en el procesador*.
  - **Ventajas:** Menor riesgo de dañar el procesador. Ideal para altas densidades de conexiones.
  - **Uso:** Todos los procesadores Intel de sobremesa y servidores actuales (desde hace varias generaciones), y la mayoría de AMD de gama alta actuales.
  - **Ejemplo 2025:** Intel LGA 1700 (Alder Lake/Raptor Lake), LGA 1851 (Arrow Lake), AMD AM5 (Ryzen 7000–9000).
    
---

<div style="text-align: center;">
  <img src="assets/componentes/25.jpg" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---


- **PGA (Pin Grid Array):**
  - *Pines en el procesador, agujeros en el socket*.
  - **Ventajas:** Reparabilidad relativa de pines doblados. Históricamente muy usado por AMD.
  - **Uso:** AMD AM4 en desktop y algunos modelos profesionales hasta 2022.
  - **Ejemplo:** AMD AM4 (Ryzen 1000–5000).

---

<div style="text-align: center;">
  <img src="assets/componentes/23.png" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

<div style="text-align: center;">
  <img src="assets/componentes/24.jpg" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

- **BGA (Ball Grid Array):**
  - *Procesador soldado directamente a la placa* (no intercambiable).
  - **Ventajas:** Máxima miniaturización, menor grosor.
  - **Desventajas:** No reparable ni actualizable por el usuario; habitual en portátiles ultracompactos, tablets y dispositivos embebidos.
  - **Ejemplo:** CPUs de portátiles de bajo consumo, mini PC OEM.

---

<div style="text-align: center;">
  <img src="assets/componentes/26.jpg" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---


## 5.2 Principales sockets modernos (2022–2025)

| Plataforma         | Socket     | Tipo | CPUs compatibles                  | Lanzam.  | Observaciones                   |
|--------------------|------------|------|-----------------------------------|----------|---------------------------------|
| **Intel Desktop**  | LGA 1200   | LGA  | 10ª/11ª Gen Core (Comet/Rocket)   | 2020     | DDR4, PCIe 3.0/4.0              |
|                    | LGA 1700   | LGA  | 12ª/13ª/14ª Gen (Alder/Raptor)    | 2021     | DDR4/DDR5, PCIe 5.0, actual transitional|
|                    | LGA 1851   | LGA  | Core Ultra (Arrow Lake)           | 2024-25  | DDR5, PCIe 5.0/6.0, Wi-Fi 7     |
|                    | LGA 4189   | LGA  | Xeon Scalable Ice/Cooper Lake     | 2020     | Servidores, DDR4/DDR5           |
| **AMD Desktop**    | AM4        | PGA  | Ryzen 1000–5000, Athlon           | 2017-22  | DDR4, PCIe 3.0/4.0              |
|                    | AM5        | LGA  | Ryzen 7000–9000 series            | 2022-25  | DDR5, PCIe 5.0/6.0, futuro AMD  |
| **AMD Workstation**| sTRX4      | LGA  | Threadripper 3000/5000            | 2019-24  | Quad/Octa RAM Channel, PCIe 4.0/5.0 |
|                    | SP3        | LGA  | EPYC (servidores/data center)     | 2017-22  | Octa-channel ECC                |
|                    | sWRX8      | LGA  | Threadripper Pro 3000WX/5000WX    | 2020-24  | Workstation extremo             |
| **Otros**          | BGA        | BGA  | CPUs soldadas portátiles/tablets   | Variable | No actualizable ni reparable    |

---

# 6 **Chipset**
- Controla buses, puertos y funciones base.
- Ejemplos: Intel Z890 (gaming/altas prestaciones), AMD X870/B650 (gaming/creator), ambos con Wi-Fi 7 y USB4 nativos.

---

# 7 Ranuras RAM y Arquitectura Multicanal

La **memoria RAM** (Random Access Memory) se instala en ranuras específicas de la placa base y juega un papel decisivo en el rendimiento, la capacidad multitarea y la velocidad general del sistema. En 2025, los tipos y arquitectura de memoria han experimentado avances notables para responder a las crecientes exigencias de software, gaming, IA y servicios profesionales.

---

## 7.1 Tipos de ranuras y módulos

- **DDR4:** Predominante hasta 2022, aún presente en equipos de gama media-baja. Capacidades comunes: 8, 16 y 32GB por módulo. Frecuencias hasta 4000 MHz.
- **DDR5:** Estándar actual, aporta frecuencias superiores (>8000 MHz), mayor eficiencia energética y capacidades mayores (módulos de 16, 32 y 48GB, hasta 256GB en workstation).
- **CAMM2:** Nueva tecnología sobre todo en portátiles y estaciones compactas, maximiza la densidad y la eficiencia en espacio reducido; supera a SO-DIMM en capacidad y velocidad.
- **SO-DIMM:** Compacta, usada en portátiles de gama media y ultra-compactos.

| Tipo         | Tamaños de módulos      | Capacidad máxima/placa | Aplicación            |
|--------------|------------------------|-----------------------|-----------------------|
| DDR4 DIMM    | 8/16/32GB (hasta 4000 MHz) | 128GB (ATX desk.)    | Desktop, básico/gaming|
| DDR5 DIMM    | 16/32/48GB (8000+ MHz) | 256+GB (ATX WS)       | Gaming extremo, WS    |
| CAMM2        | 32/64/128GB (10.000 MHz)| 128GB (portátil)      | Portable, premium     |
| SO-DIMM      | 8/16/32GB (DDR4/5)     | 64GB (ultracompacto)  | Laptop, MiniPC        |

---
<div style="text-align: center;">
  <img src="assets/componentes/28.jpg" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---
<div style="text-align: center;">
  <img src="assets/componentes/29.avif" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>
---
<div style="text-align: center;">
  <img src="assets/componentes/30.jpg" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

## 7.2 Número de ranuras

- **MiniITX:** 2 slots (limite de hasta 64GB DDR5/DDR4).
- **MicroATX/ATX:** 4 slots como estándar (hasta 128–256GB con DDR5).
- **Workstation/Servidor:** 8–16 slots (hasta 1TB o más, ECC Registered).

---

## 7.3 Arquitectura de canales (Channel Architecture)

La **arquitectura de canales** define cuántos caminos paralelos existen entre la memoria y el controlador de memoria (generalmente en la CPU). Un mayor número de canales implica mayor ancho de banda y rendimiento en cargas pesadas.

| Arquitectura Canal | Ranuras ocupadas (mín/máx) | Ancho de banda teórico | Ámbitos de uso     |
|--------------------|--------------------------|-----------------------|--------------------|
| Single Channel     | 1/2                      | 32 GB/s (DDR5)        | Ofimática básica   |
| Dual Channel       | 2/4                      | 64 GB/s (DDR5)        | Gaming, multitarea |
| Quad Channel       | 4/8                      | 128 GB/s (DDR5/ECC)   | Edición 4K, IA     |
| Hexa Channel       | 6/12                     | 192 GB/s              | Servidor, datos    |
| Octa Channel       | 8/16                     | 256+ GB/s             | Datacenter, HPC    |

- **Dual Channel:** Dos módulos idénticos; usado en casi todo desktop/gaming actual.
- **Quad Channel:** Cuatro módulos; workstation HEDT, edición/profesional.
- **Hexa/Octa Channel:** Workstation y servidores, maximiza el ancho de banda para tareas extremas (render, IA, simulación científica).

---

## 7.4 Cómo aprovechar la arquitectura multicanal

- Instala módulos en pares/grupos idénticos, siguiendo siempre la guía de colores del manual de la placa.
- Usa módulos de capacidad/frecuencia iguales.
- BIOS/UEFI detecta el número de canales activos y puede sugerir configuraciones óptimas.
- Para actualización, es mejor mantener la simetría: si tienes 2x8GB, amplía a 4x8GB (Dual/Quad Channel), NO mezcles 8+16GB.

---

## 7.5 Ejemplo de configuración óptima para gaming 2025

- **Placa ATX DDR5 con 4 ranuras:**
  - Instala 2x16GB DDR5-7200 (Dual Channel) para gaming de alto nivel.
  - Para edición/creación: 4x16GB o 4x32GB (Quad Channel) si la placa soporta.

---

## 7.6 Consejos prácticos

- DDR5 ahora soporta perfiles **XMP 3.0** (Intel) y **EXPO** (AMD) para configurar automáticamente la máxima frecuencia compatible.
- Workstations usan memoria **ECC Registered** para evitar errores y dar máxima fiabilidad.
- Las nuevas placas base pueden mostrar gráficamente en BIOS la arquitectura de canal activa y sugerir la mejor configuración.

---

# 8. Comunicación Interna

## 8.1 Concepto General

La **comunicación interna** de una placa base se refiere al conjunto de **buses, interfaces y enlaces** que permiten la **transferencia de datos, direcciones y señales de control** entre los distintos componentes: CPU, memoria, chipset, GPU, almacenamiento y periféricos.

Su eficiencia determina directamente el **rendimiento global del sistema**.

---

## 8.2 Arquitectura Moderna de Comunicación

En las placas base actuales, especialmente desde las arquitecturas **Intel Core** y **AMD Ryzen**, la comunicación interna se estructura en torno a:

- **CPU (Unidad Central de Procesamiento)**
  Es el centro del sistema; integra el controlador de memoria y la mayoría de las líneas **PCI Express**.

- **Chipset (PCH / Southbridge moderno)**
  Gestiona la comunicación con periféricos de menor velocidad: USB, SATA, LAN, Audio, etc.
  En la actualidad se conecta con la CPU mediante un **enlace DMI** (Intel) o **Infinity Fabric** (AMD).

---

## 8.3 Buses y Enlaces Principales

| Bus / Enlace | Fabricante / Arquitectura | Función Principal | Ancho de Banda Aprox. |
|---------------|---------------------------|-------------------|------------------------|
| **FSB (Front Side Bus)** | Intel (antiguo) | Comunicación CPU ↔ Northbridge | 1–6 GB/s |
| **QPI (Quick Path Interconnect)** | Intel (Xeon, i7 antiguos) | Sustituto del FSB | 25.6 GB/s |
| **DMI 3.0 / 4.0** | Intel moderno | CPU ↔ Chipset (PCH) | 3.93–7.86 GB/s |
| **Infinity Fabric** | AMD Ryzen / EPYC | CPU ↔ Chipset / CCX | Escalable, 18–64 GB/s |
| **PCI Express (PCIe 4.0 / 5.0 / 6.0)** | Estándar PCI-SIG | GPU, SSD NVMe, expansión | 16–128 GB/s |
| **DDR4 / DDR5 Bus** | JEDEC | CPU ↔ Memoria RAM | 25–60 GB/s por canal |

---

## 8.4 Diagrama Funcional Simplificado

```plaintext
+--------------------+       +----------------------+
|       CPU          |<----->|     Chipset (PCH)    |
| (PCIe + Memory Ctrl)| DMI  | (USB, SATA, LAN...)  |
+---------^----------+       +----------^-----------+
          |                             |
          | DDR4/DDR5 Channels          | Periféricos
          |                             v
     +----+----+                   +----------+
     |  RAM    |                   |  USB/LAN |
     +---------+                   +----------+
```

---

## 8.5 Consideraciones Técnicas

- La **latencia** del bus de memoria influye en el rendimiento global.
- El número de **líneas PCIe (lanes)** disponibles depende del procesador.
- En equipos de gama alta, la comunicación interna se optimiza mediante **buses dedicados** (por ejemplo, PCIe 5.0 exclusivo para GPU y NVMe).
- La eficiencia térmica y eléctrica del bus afecta la **estabilidad del sistema**.

---

# 9. VRM (Voltage Regulator Module)

El **VRM (Voltage Regulator Module, Módulo Regulador de Voltaje)** es un circuito fundamental en todas las placas base y tarjetas gráficas modernas. Su función principal es convertir y estabilizar la tensión de entrada (proveniente de la fuente de alimentación) a los valores precisos que requieren el procesador (CPU), la memoria (RAM) y otros chips sensibles del sistema.

---

## 9.1. Concepto y función esencial

- Los microprocesadores actuales operan a voltajes muy bajos (entre 1.0V y 1.5V), mientras que la fuente ATX suministra voltajes mucho mayores (12V, 5V, 3.3V).
- El **VRM** se encarga de modificar esa tensión y entregarla de forma completamente estable y limpia, adaptándose a las necesidades del procesador según el uso: más voltaje bajo carga, menos en reposo.
- Cualquier fluctuación o “ruido” puede provocar inestabilidad, errores, pérdida de rendimiento o incluso averías graves.

---

## 9.2.  Estructura de un VRM moderno

- **Fases de regulación:** El VRM está compuesto por varias “fases”. Cada fase incluye MOSFETs (interruptores electrónicos), bobinas (inductores) y condensadores. Cuantas más fases, más estable y eficiente la entrega de energía.
- **Controller PWM:** Un chip controla cuándo se activa cada fase, ajustando la potencia necesaria en tiempo real según la demanda del procesador.
- **Distribución:** Los VRM no solo alimentan la CPU, también hay circuitos específicos para RAM, chipset, GPU (en placas gráficas).

| Elemento      | Función                                         |
|---------------|-------------------------------------------------|
| PWM Controller| Gestiona las fases y adapta el voltaje y frecuencia|
| MOSFET        | Actúa como interruptor, regula el paso de corriente|
| Bobina        | Filtra y suaviza la entrega                      |
| Condensador   | Almacena energía, elimina interferencias         |
| Fase VRM      | Conjunto de los anteriores, repite el ciclo      |

---

## 9.3. Importancia del VRM en 2025

- **Procesadores multinúcleo** (12, 16 o más núcleos, CPUs y GPUs para IA) requieren VRMs robustos, capaces de entregar altas intensidades de corriente sin fluctuar.
- **Overclocking seguro:** Los VRM de alta calidad permiten aumentar la frecuencia y el voltaje de la CPU sin riesgo de fallo ni sobrecalentamiento.
- **Eficiencia energética:** Un VRM diseñado con componentes premium (bobinas planas, condensadores sólidos japoneses, MOSFETs de baja resistencia) mejora la vida útil y el consumo.
- **Monitorización:** Las placas modernas ofrecen monitorización digital del VRM: temperatura, voltaje, intensidad, advertencias en tiempo real via BIOS/UEFI y apps del fabricante.

---

## 9.4. Número de fases y su relevancia

| Uso y demanda         | Fases VRM recom. | Ejemplo real             |
|---------------------- |------------------|--------------------------|
| Ofimática/Básico      | 6–8              | Placa ATX económica      |
| Gaming avanzado       | 10–14            | B660/Z790/X670 "Gaming"  |
| Workstation/OC extremo| 16–24            | Z890/X870/Threadripper   |

- Más fases = Mejor estabilidad, menor calentamiento, distribución equilibrada de carga.
- No solo importa la cantidad, sino la calidad y el diseño de las fases.

---

## 9.5. Consejos de usuario y técnico

- Prioriza placas con VRMs de calidad si planeas usar CPUs de gama alta o hacer overclocking.
- Monta disipadores sobre el VRM y verifica airflow en chasis gaming/workstation.
- Consulta la monitorización en todo momento, especialmente en equipos exigentes o de larga duración en cargas.

---

# 10. Gestión Térmica

## 10.1 Introducción

La **gestión térmica** en una placa base consiste en el conjunto de **tecnologías, sensores y componentes** diseñados para mantener las **temperaturas óptimas** de trabajo de la CPU, VRM, chipset y unidades M.2.

Un control térmico adecuado prolonga la vida útil y evita reducciones automáticas de rendimiento (**thermal throttling**).

---

## 10.2 Elementos Clave

| Elemento | Función | Observaciones |
|-----------|----------|---------------|
| **Disipadores pasivos (heatsinks)** | Absorben y disipan calor del VRM, chipset o M.2 | Usan aluminio o cobre |
| **Ventiladores (fans)** | Generan flujo de aire sobre zonas críticas | Controlados por PWM |
| **Sensores térmicos (TMPIN, VRM, CPU, MOS)** | Miden temperatura en tiempo real | Integrados en el PCB |
| **Control por BIOS / UEFI** | Define curvas de ventilador y límites | Smart Fan, Q-Fan, etc. |

---

## 10.3 Tecnologías Modernas

- **Fan Curve Control**: permite definir curvas de velocidad del ventilador en función de la temperatura.
- **Zero RPM Mode**: los ventiladores se detienen completamente cuando el sistema está en reposo.
- **Thermal Armor / Shields**: cubiertas metálicas sobre VRM o M.2 que disipan y protegen del polvo.
- **Heatpipes y cámaras de vapor**: presentes en placas de gama alta para distribuir el calor uniformemente.

---

## 10.4 Recomendaciones Prácticas

- Evitar obstrucciones de flujo de aire en el interior del chasis.
- Comprobar que el disipador esté correctamente asentado sobre el chipset o el VRM.
- Usar **pasta térmica de calidad** y renovar cada 2–3 años.
- Supervisar temperaturas con herramientas como **HWMonitor**, **AIDA64** o desde la **UEFI**.

---

# 11. Instalación y Mantenimiento

El proceso de **instalación y mantenimiento** de una placa base y sus componentes asociados es una de las fases más importantes en la vida útil de un equipo informático.  
Un montaje correcto garantiza **rendimiento, estabilidad y durabilidad**, mientras que una manipulación inadecuada puede causar **averías irreparables** por descarga electrostática, sobrecalentamiento o mala conexión.

- Revisa compatibilidades: socket, chipset, RAM, disipación, VRMs.
- Consulta el manual para instalación correcta según socket (alineación pines/marcas, presión justa, configurar BIOS/UEFI tras montaje).
- Mantén BIOS actualizado para máximo soporte.
  
---

## 11.1 Precauciones ESD y manipulación segura

Las **ESD (Electrostatic Discharge)** o **descargas electrostáticas** son corrientes eléctricas de baja intensidad pero alto voltaje que se producen por la acumulación de carga en el cuerpo humano o en los objetos.  
Estas descargas pueden **dañar instantáneamente los chips electrónicos**, incluso sin ser perceptibles al tacto.

### Recomendaciones generales:

- **Usar pulsera antiestática** conectada a una superficie metálica o a tierra.  
- **Evitar alfombras, ropa sintética o zapatos aislantes** durante el montaje.  
- **Descargar la electricidad corporal** tocando una superficie metálica antes de manipular los componentes.  
- **Manipular la placa base y los módulos por los bordes**, nunca por las zonas de contacto o chips.  
- **Trabajar sobre una superficie limpia, seca y no conductora** (tapete antiestático o mesa de madera).  
- Mantener **las bolsas ESD originales** de los componentes hasta el momento de instalarlos.

### Causas comunes de daño ESD:

- Rozar tejidos sintéticos mientras se montan componentes.  
- Conectar cables con el equipo encendido.  
- Dejar módulos de RAM o CPU sin su protección conductora.  

**Recuerda:** una sola descarga estática de unos 100 V (imperceptible al tacto) puede destruir un microchip que opera a 1,2 V.

---

## 11.2 Montaje y desmontaje en banco de pruebas

El **banco de pruebas** (o “test bench”) es un entorno seguro que permite **ensamblar y verificar componentes fuera del chasis** antes del montaje final.  
Es la forma más eficiente de comprobar la compatibilidad y el correcto funcionamiento del hardware.

### Fases del montaje:

1. **Preparación del banco**
   - Coloca la placa base sobre una superficie aislante o sobre su caja (nunca directamente sobre metal).
   - Ten a mano: CPU, disipador, RAM, fuente ATX y cable HDMI o DisplayPort.

2. **Instalación del procesador**
   - Levanta el pestillo del socket y **alinea el triángulo de la CPU** con el del zócalo.
   - Coloca la CPU sin aplicar fuerza y baja el mecanismo de retención.

3. **Colocación del disipador**
   - Aplica una pequeña cantidad de **pasta térmica (del tamaño de un grano de arroz)**.
   - Asegura el disipador firmemente sin exceder el par de apriete.

4. **Instalación de la RAM**
   - Inserta los módulos **en los bancos alternos** si la placa soporta doble canal.
   - Asegúrate de que las pestañas laterales encajen correctamente.

5. **Conexión de alimentación**
   - Conecta el cable **ATX 24 pines** y el conector **EPS 8 pines** (CPU Power).
   - Añade temporalmente un botón de encendido o **puentea los pines POWER_SW**.

6. **Verificación inicial**
   - Conecta monitor y teclado.
   - Enciende y comprueba el **POST** (Power-On Self Test).
   - Si hay error, revisa: RAM, CPU o cableado del panel frontal.

### Desmontaje seguro:

- Desconecta la fuente de alimentación y **espera 30 segundos** antes de retirar cables.
- Retira primero GPU y RAM, luego CPU y disipador.
- Limpia y guarda los componentes en sus bolsas o cajas originales.

**Objetivo del banco de pruebas:** garantizar que **todos los componentes funcionan antes de montarlos dentro del chasis**.

---

## 11.3 Limpieza y mantenimiento preventivo

El mantenimiento periódico evita fallos prematuros y mejora la eficiencia térmica y eléctrica del sistema.  
Una placa base limpia y bien refrigerada mantiene su rendimiento óptimo durante más años.

### Tipos de mantenimiento:

#### 1. Limpieza física

- **Frecuencia:** cada 6 a 12 meses, según el entorno (más frecuente en zonas con polvo o humedad).  
- **Materiales recomendados:**
  - Aire comprimido o soplador antiestático.
  - Brochas suaves antiestáticas.
  - Alcohol isopropílico (≥90%) para contactos o restos de pasta térmica.  
- **Procedimiento:**
  - Desconecta la corriente y extrae los componentes.
  - Sopla el polvo de ventiladores, ranuras y disipadores.
  - Limpia suavemente los contactos con alcohol isopropílico y deja secar antes de montar.

#### 2. Mantenimiento térmico

- Sustituye la **pasta térmica del procesador** cada 2 años o si la temperatura supera los 85 °C.  
- Revisa el **estado de los ventiladores y sensores PWM**.  
- Comprueba que los **disipadores M.2 y VRM** estén bien fijados.

#### 3. Actualización y verificación

- Revisa el estado del **chipset, condensadores y VRM** visualmente (busca hinchazones o fugas).  
- Actualiza firmware y controladores desde fuentes oficiales.  
- Reemplaza cables dañados o doblados (especialmente SATA o EPS).

### Recomendaciones generales:
- Mantén una **temperatura ambiente entre 20 y 25 °C** en la zona de trabajo.  
- Evita acumular polvo con filtros antipolvo y flujo de aire positivo.  
- Documenta las **intervenciones realizadas** (fecha, componentes y observaciones).

---

### Conclusión

Una buena práctica de instalación y mantenimiento garantiza:
- **Menor tasa de fallos.**  
- **Mayor vida útil de los equipos.**  
- **Reducción de incidencias en entornos profesionales o educativos.**

El técnico debe aplicar siempre **protocolos ESD**, realizar **pruebas en banco** antes de ensamblar y establecer un **plan de mantenimiento periódico** adaptado al entorno.

---
