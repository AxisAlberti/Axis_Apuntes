---
title: "UD 09 - 9.1 Tarjetas gráficas"
description: "Tarjetas gráficas"
summary: "Tarjetas gráficas"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2026-01-29
icon: "material/file-document-outline"
categories:
    - "MON"
tags:
    - "gpu"
    - "graficos"
    - "tarjeta-grafica"
---

## TEMA 9. TARJETAS GRÁFICAS

---

# Objetivos de aprendizaje

- Comprender el papel de la GPU en un sistema informático.
- Identificar los componentes básicos de una tarjeta gráfica.
- Explicar el flujo general de renderizado 2D/3D.
- Diferenciar interfaces y salidas de vídeo habituales.
- Aplicar criterios de selección, montaje y mantenimiento.

---

# 1. Qué es una tarjeta gráfica

La **tarjeta gráfica** es el componente encargado de **procesar y generar imágenes** para la pantalla. Está diseñada para ejecutar muchos cálculos en paralelo: dibuja píxeles, aplica texturas, calcula luces y sombras y muestra vídeo con fluidez.

Es importante distinguir:

- **GPU (Graphics Processing Unit)**: el procesador gráfico en sí.
- **Tarjeta gráfica**: la placa completa que integra la GPU, la VRAM, el VRM, la refrigeración y las salidas de vídeo.

Puede presentarse en dos formas:

- **GPU integrada**: está dentro del procesador o la placa base y comparte la memoria RAM del sistema.
- **GPU dedicada**: tarjeta independiente con su propia memoria de vídeo (VRAM) y mayor potencia.

<figure>
  <img src="../assets/gpu/rtx5090_fe.png" alt="Tarjeta gráfica NVIDIA reciente (ejemplo RTX 50)" style="width:100%;height:auto;max-width:800px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Tarjeta gráfica NVIDIA reciente (ejemplo RTX 50). Fuente: Wikimedia Commons.</figcaption>
</figure>

---

# 2. Componentes principales

## 2.1 GPU (procesador gráfico)

Es el chip principal. Contiene miles de unidades de ejecución en paralelo (núcleos de sombreado), además de **cachés**, **unidades de textura** y **ROP** (salida de render). Está optimizada para cálculos gráficos y de coma flotante.

## 2.2 Memoria de vídeo (VRAM)

Almacena texturas, buffers y datos necesarios para el renderizado. Su rendimiento depende de:

- **Capacidad** (GB).
- **Ancho de banda** (bus de memoria y velocidad efectiva).
- **Latencia y cachés** internas.

Una GPU con menos VRAM puede rendir mejor si su memoria es más rápida y el bus es más ancho.

## 2.3 VRM y alimentación

El **módulo regulador de voltaje (VRM)** convierte la energía de la fuente a niveles estables para la GPU y la VRAM. Las tarjetas potentes requieren conectores de alimentación adicionales y una fuente adecuada.

## 2.4 PCB y firmware (VBIOS)

La **placa (PCB)** conecta todos los componentes. El **VBIOS** define parámetros clave: frecuencias, límites de energía y curvas de ventilación.

## 2.5 Interfaz con la placa base

La conexión más habitual es **PCI Express (PCIe)** en formato **x16**. PCIe es un estándar mantenido por PCI-SIG y evoluciona por versiones (4.0, 5.0, 6.0, 7.0), manteniendo compatibilidad hacia atrás.

<figure>
  <img src="../assets/gpu/pcie5_trx50_slot.png" alt="Ranura PCI Express x16 en placa base reciente" style="width:100%;height:auto;max-width:800px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Ranura PCI Express x16 en placa base reciente. Fuente: Wikimedia Commons.</figcaption>
</figure>

## 2.6 Salidas de vídeo

Las más comunes son **HDMI** y **DisplayPort**. HDMI está muy extendido en televisores y monitores domésticos, mientras que DisplayPort es el estándar habitual en monitores de PC.

## 2.7 Refrigeración

La GPU genera calor intenso. Por eso se usan disipadores, heatpipes y ventiladores; en equipos de alto rendimiento también hay refrigeración líquida. Una mala refrigeración provoca **thermal throttling** (bajada automática de rendimiento).

---

# 3. Funcionamiento básico del renderizado

El proceso gráfico simplificado sigue estas fases:

1. **Entrada de datos**: la CPU envía geometría y comandos de dibujo a la GPU.
2. **Procesado de vértices**: transformación de modelos 3D al espacio de pantalla.
3. **Rasterización**: conversión de primitivas (triángulos) a píxeles.
4. **Shaders de fragmento**: cálculo de color, iluminación, sombras y efectos.
5. **Frame buffer**: el frame final se guarda en memoria y se presenta al monitor.

Además del renderizado tradicional, las GPUs modernas incorporan **trazado de rayos** (ray tracing) para mejorar reflejos, sombras e iluminación con mayor realismo.

---

# 4. VRAM, ancho de banda y resolución

La **VRAM** no es solo cantidad. También importa el **ancho de banda**, que depende de la velocidad de la memoria y del ancho del bus.

- A mayor resolución y mayor calidad de texturas, más VRAM se necesita.
- El ancho de banda afecta a la fluidez en escenarios con muchas texturas y efectos.

## 4.1 GDDR frente a HBM (visión general)

- **GDDR**: memoria rápida montada en chips alrededor de la GPU. Es común en tarjetas de consumo por su coste y disponibilidad.
- **HBM (High Bandwidth Memory)**: memoria apilada (stack) muy cerca de la GPU, con gran ancho de banda y buena eficiencia energética; suele verse en tarjetas profesionales.

<figure>
  <img src="../assets/gpu/gddr5x_1080ti.jpg" alt="Chips de memoria GDDR en una GPU (ejemplo GeForce GTX 1080 Ti)" style="width:100%;height:auto;max-width:800px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Chips de memoria GDDR en una GPU (ejemplo GeForce GTX 1080 Ti). Fuente: Wikimedia Commons.</figcaption>
</figure>

<figure>
  <img src="../assets/gpu/hbm_stack_gp100.jpg" alt="Memoria HBM apilada junto a la GPU (ejemplo GP100/Tesla P100)" style="width:100%;height:auto;max-width:800px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Memoria HBM apilada junto a la GPU (ejemplo GP100/Tesla P100). Fuente: Wikimedia Commons.</figcaption>
</figure>

---

# 5. Interfaces y estándares de vídeo

## 5.1 HDMI

HDMI es el estándar más común en televisores y monitores domésticos. El HDMI Forum publica las versiones del estándar (HDMI 2.x), que van ampliando resolución, tasas de refresco y ancho de banda.

<figure>
  <img src="../assets/gpu/hdmi_connector.svg" alt="Conector HDMI (vista esquemática)" style="width:100%;height:auto;max-width:500px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Conector HDMI (vista esquemática). Fuente: Wikimedia Commons.</figcaption>
</figure>

## 5.2 DisplayPort

DisplayPort es el estándar de VESA para entornos PC. La versión 2.1 amplía el ancho de banda y la interoperabilidad con USB-C/USB4.

<figure>
  <img src="../assets/gpu/displayport_connector.svg" alt="Conector DisplayPort (vista esquemática)" style="width:100%;height:auto;max-width:500px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Conector DisplayPort (vista esquemática). Fuente: Wikimedia Commons.</figcaption>
</figure>

## 5.3 Compatibilidad y cables

- HDMI y DisplayPort son retrocompatibles entre versiones.
- Los cables certificados (DP40/DP80 en DisplayPort) garantizan el rendimiento declarado por el estándar.

---

# 6. APIs gráficas y drivers

Las **APIs gráficas** son el “idioma” que usan los programas para comunicarse con la GPU:

- **Direct3D (DirectX)**: estándar en Windows para juegos y software multimedia.
- **OpenGL**: API multiplataforma con largo recorrido.
- **Vulkan**: API moderna de bajo nivel, también multiplataforma.

Los **drivers** traducen las órdenes de la API a instrucciones que entiende la GPU. Por eso es clave mantenerlos actualizados.

---

# 7. Panorama actual (2025-2026): NVIDIA y AMD

## 7.1 NVIDIA (GeForce RTX 50 Series - Blackwell)

NVIDIA anunció la serie **GeForce RTX 50** basada en **Blackwell**, con mejoras en renderizado asistido por IA, nuevas tecnologías de sombreado y DLSS 4.

## 7.2 AMD (Radeon RX 9000 - RDNA 4)

AMD presentó la arquitectura **RDNA 4** con la serie **Radeon RX 9000**, destacando mejoras en ray tracing y aceleradores de IA, junto con FSR 4.

<figure>
  <img src="../assets/gpu/amd_radeon_rx9060xt.png" alt="Tarjeta gráfica AMD reciente (ejemplo RX 9000)" style="width:100%;height:auto;max-width:800px;display:block;margin:0 auto;" />
  <figcaption style="font-size:0.85em;color:#666;text-align:center;">Tarjeta gráfica AMD reciente (ejemplo RX 9000). Fuente: Wikimedia Commons.</figcaption>
</figure>

## 7.3 Comparativa rápida (NVIDIA vs AMD, generación actual)

| Fabricante | Arquitectura (2025) | Serie actual | Enfoque principal | Tecnologías destacadas |
|-----------|----------------------|-------------|-------------------|------------------------|
| NVIDIA | Blackwell | GeForce RTX 50 | Renderizado neuronal e IA en juegos y creación | DLSS 4, RT Cores y Tensor Cores avanzados |
| AMD | RDNA 4 | Radeon RX 9000 | Rendimiento y valor en gaming con IA integrada | FSR 4, aceleradores de IA y ray tracing mejorado |

**Nota:** las características y rendimiento exactos dependen del modelo concreto.

---

# 8. Criterios de selección de una tarjeta gráfica

## 8.1 Uso previsto

- **Ofimática**: integrada suele ser suficiente.
- **Gaming 1080p/1440p**: GPU dedicada de gama media o alta.
- **Edición de vídeo/3D**: GPU potente con buena VRAM y ancho de banda.
- **IA local y creación de contenido**: GPU con buena VRAM y soporte de aceleración.

## 8.2 Compatibilidad y conectividad

- Resolución y tasa de refresco del monitor.
- Puertos disponibles (HDMI/DisplayPort).
- Versión de PCIe compatible con la placa base.

## 8.3 Consumo y fuente

Verificar la potencia de la fuente (PSU), el número de conectores necesarios y la eficiencia energética.

## 8.4 Tamaño físico y refrigeración

Comprobar longitud y grosor: algunas tarjetas ocupan 2 o 3 ranuras. Una mejor refrigeración aumenta la vida útil y reduce el thermal throttling.

---

# 9. Montaje y mantenimiento básico

- Descargar el driver más reciente antes de instalar.
- Instalar la tarjeta en la ranura PCIe x16 principal.
- Conectar correctamente los cables de alimentación.
- Revisar temperaturas con software de monitorización.
- Limpiar polvo de disipadores y ventiladores de forma periódica.

---

# 10. Diagnóstico de fallos frecuentes

- **Artefactos en pantalla**: posible sobrecalentamiento o VRAM inestable.
- **Apagones o reinicios**: fuente insuficiente o conectores mal puestos.
- **Bajo rendimiento**: drivers antiguos o modo de energía incorrecto.

---

# Ejemplos prácticos

**Caso 1: Aula de ofimática**
- Requisitos: navegación web, ofimática, vídeo básico.
- Solución: GPU integrada, bajo consumo y coste mínimo.

**Caso 2: Taller de edición de vídeo**
- Requisitos: renderizado acelerado, filtros en tiempo real.
- Solución: GPU dedicada con buena VRAM y soporte de APIs actuales.

**Caso 3: Equipo gaming**
- Requisitos: 1080p/1440p, altas tasas de refresco.
- Solución: GPU dedicada con salidas DisplayPort y buena refrigeración.

**Caso 4: Laboratorio de IA básica**
- Requisitos: entrenamiento ligero y pruebas de modelos.
- Solución: GPU dedicada con suficiente VRAM y drivers actualizados.

---

# Resumen (ideas clave)

- La GPU es el motor del procesamiento gráfico y paralelo en el PC.
- Una tarjeta gráfica integra GPU, VRAM, VRM, interfaz PCIe y salidas de vídeo.
- El rendimiento depende de la potencia de la GPU y del ancho de banda de la VRAM.
- HDMI y DisplayPort son las interfaces digitales más habituales.
- Drivers y APIs gráficas son esenciales para el funcionamiento correcto.

---

# Referencias y enlaces

- [Wikibooks - Mantenimiento y Montaje de Equipos Informáticos (Tema 2: La tarjeta gráfica)](https://es.wikibooks.org/wiki/Mantenimiento_y_Montaje_de_Equipos_Inform%C3%A1ticos/Tema_2/La_tarjeta_gr%C3%A1fica)
- [NVIDIA - Blackwell GeForce RTX 50 Series (nota de prensa, 2025)](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Blackwell-GeForce-RTX-50-Series-Opens-New-World-of-AI-Computer-Graphics/default.aspx)
- [NVIDIA Newsroom - GeForce RTX 50 Series (2025)](https://nvidianews.nvidia.com/news/nvidia-blackwell-geforce-rtx-50-series-opens-new-world-of-ai-computer-graphics)
- [AMD - RDNA 4 y Radeon RX 9000 Series (nota de prensa, 2025)](https://www.amd.com/en/newsroom/press-releases/2025-2-28-amd-unveils-next-generation-amd-rdna-4-architectu.html)
- [PCI-SIG - PCI Express Base Specification](https://pcisig.com/specification-overview/pci-express-base)
- [HDMI - HDMI Specification (HDMI 2.x)](https://hdmi.org/spec/hdmi2_1)
- [VESA - DisplayPort 2.1 Specification](https://www.displayport.org/pr/vesa-releases-displayport-2-1-specification/)
- [Microsoft Learn - Direct3D](https://learn.microsoft.com/en-us/windows/win32/getting-started-with-direct3d)
- [Khronos - OpenGL](https://www.khronos.org/opengl/)
- [Khronos - Vulkan 1.4](https://www.vulkan.org/news/auto-23155-a676f167a3982c6a4f6d36a46284cad8)
- [Wikimedia Commons - HDMI_Connector_2.svg](https://commons.wikimedia.org/wiki/File:HDMI_Connector_2.svg)
- [Wikimedia Commons - DisplayPort_Connector.svg](https://commons.wikimedia.org/wiki/File:DisplayPort_Connector.svg)
- [Wikimedia Commons - GDDR5X_1080ti.jpg](https://commons.wikimedia.org/wiki/File:GDDR5X_1080ti.jpg)
- [Wikimedia Commons - HBM stack (GP100/Tesla P100)](https://commons.wikimedia.org/wiki/File:Nvidia@16nm@Pascal@GP100@Tesla_P100@T_Taiwan_1912A1_PN9G70.S6W_GP100-897-A1_DSCx11_HBM-Stack_notes.jpg)

## Créditos de imágenes

- rtx5090_fe.png - ZMASLO, CC BY 3.0, Wikimedia Commons (captura de vídeo de Founders Edition).
- amd_radeon_rx9060xt.png - Akb432, CC BY-SA 4.0, Wikimedia Commons.
- pcie5_trx50_slot.png - PantheraLeo1359531, CC BY 4.0, Wikimedia Commons.
- hdmi_connector.svg - Wyzzymoon, CC BY 4.0, Wikimedia Commons.
- displayport_connector.svg - Wyzzymoon, CC BY 4.0, Wikimedia Commons.
- gddr5x_1080ti.jpg - Geni (recorte) / Fritzchens Fritz (foto), CC0, Wikimedia Commons.
- hbm_stack_gp100.jpg - FritzchensFritz, CC0, Wikimedia Commons.
