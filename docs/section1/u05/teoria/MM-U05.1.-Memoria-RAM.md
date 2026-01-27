---
title: "UD 05 - 5.1 Memoria RAM"
description: "Memoria RAM"
summary: "Memoria RAM"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2025-10-01
icon: "material/file-document-outline"
permalink: /mm/u05/5-1-memoria-ram
categories:
    - "MON"
tags:
    - "memoria"
---

## TEMA 5. MEMORIA DDR


---
# Jerarquía de memorias



---

## 0. **Definición y Vocabulario Fundamental (Memoria DDR)**

La **memoria DDR** es la tecnología dominante de **DRAM** que se usa como **memoria principal** en PC y servidores. Se llama *Double Data Rate* porque **transfiere datos en los dos flancos del reloj** (subida y bajada), duplicando la tasa efectiva. Su misión es ofrecer un **espacio de trabajo** de baja latencia y alto ancho de banda entre la CPU (y su jerarquía de cachés) y el almacenamiento masivo (SSD/HDD).

 > - DDR transmite datos en los flancos de subida y bajada del reloj, duplicando rendimiento por ciclo.
 > - Cada nueva generación de DDR mejora velocidad, disminuye consumo y maximiza la densidad.
 > - La RAM es volátil: al apagar el equipo, se borra la información.

## Vocabulario Fundamental

| Término | Definición |
|---|---|
| **DDR (Double Data Rate)** | Familia de DRAM síncrona que transmite datos en ambos flancos del reloj para duplicar la tasa efectiva (MT/s). |
| **DDR2 / DDR3 / DDR4 / DDR5** | Generaciones con cambios en voltaje, prefetch, topología y señalización; **incompatibles** entre sí a nivel físico/eléctrico. |
| **Prefetch (2n/4n/8n/16n)** | Bits leídos internamente por acceso y puestos en cola hacia el bus externo; crece con cada generación para elevar el rendimiento. |
| **MT/s** | Mega-transferencias por segundo (tasa efectiva de DDR). Ej.: *DDR4-3200* = 3200 MT/s. |
| **Frecuencia (MHz)** | Reloj base de la DRAM/IMC; en DDR, **MT/s = 2 × MHz**. |
| **Burst Length (BL)** | Tamaño de ráfaga por operación de datos (BL8 típico en DDR3/4; BL16 en DDR5). |
| **Bank / Bank Group** | Particiones internas que permiten paralelismo; los *bank groups* reducen contención entre accesos. |
| **Canal de memoria** | Camino de 64-bit entre la controladora y la RAM; doble/quad canal multiplica el ancho de banda. |
| **Subcanal (DDR5)** | División lógica de cada DIMM en **2×32-bit**, mejorando eficiencia y concurrencia. |
| **Rank (SR/DR/QR)** | Conjunto lógico de chips direccionados como unidad en un DIMM; afecta interleaving y compatibilidad. |
| **Timings (CL-tRCD-tRP-tRAS)** | Latencias internas (en ciclos) que gobiernan apertura, lectura, pre-carga y cierre de filas. |
| **CL (CAS Latency)** | Ciclos desde la orden de lectura hasta llegar el primer dato. |
| **SPD** | EEPROM del módulo con parámetros JEDEC y perfiles de fabricante leídos por UEFI/BIOS. |
| **XMP / EXPO** | Perfiles (Intel/AMD) con frecuencia/timings/voltaje validados por el fabricante del kit. |
| **ECC (de sistema)** | Detección/corrección de errores a nivel de DIMM/IMC (p. ej., SECDED); requiere CPU+placa+módulos compatibles. |
| **On-die ECC (DDR5)** | Corrección **interna al chip DRAM**; no sustituye el ECC de sistema. |
| **UDIMM / RDIMM / LRDIMM** | Módulos sin registro / con registro / con búfer de carga reducida; RDIMM/LRDIMM predominan en servidores. |

---

# 1. Estructura y Funcionamiento (bancos, filas/columnas, prefetch, bursts)

La memoria DDR (Double Data Rate) tiene una arquitectura interna diseñada para maximizar la velocidad de acceso, la eficiencia y la capacidad. Comprender cómo se organiza y opera la RAM DDR es clave para entender su rendimiento y limitaciones.

## Bancos, Filas y Columnas

- **Banco:**  
  La memoria DDR está dividida internamente en varios bancos (habitualmente 4, 8 o más según generación y capacidad). Cada banco puede ser accedido y gestionado de forma independiente, permitiendo operaciones simultáneas o en paralelo para mejorar el rendimiento.

- **Filas y columnas:**  
  Dentro de cada banco, la información se organiza en una matriz bidimensional de **filas** y **columnas**. Cada celda de esta matriz guarda 1 bit de información. Para acceder a un dato concreto, el controlador de memoria debe seleccionar primero la fila y luego la columna.

- **Activación de fila:**  
  Cuando se requiere un acceso, se activa una fila completa en un banco y se lee/escribe una columna (dato puntual o múltiple). Activar una nueva fila implica “cerrar” una (precharge) antes de “abrir” la siguiente (activation).

## Prefetch y Bursts

- **Prefetch:**  
  Para aumentar la eficiencia, la DDR utiliza la técnica de “prefetch”, que consiste en anticipar la lectura de varios bits de la fila seleccionada antes de que sean requeridos por el sistema. Así, puede cargar más información en menos ciclos y alimentar ráfagas de datos rápidas.

  - DDR: prefetch de 2 bits
  - DDR2: prefetch de 4 bits
  - DDR3/DDR4: prefetch de 8 bits

- **Burst:**  
  Cuando el controlador pide datos, la memoria envía en una “ráfaga” (**burst**) varios bits seguidos en una sola operación de acceso. El tamaño de esta ráfaga depende del tipo de DDR y la configuración del sistema, y es clave para aprovechar la velocidad real de la memoria.

## Resumen gráfico

+----------------------+
| Banco |
| +---------------+ |
| | Fila/Columna | |
| | (matriz) | |
| +---------------+ |
+----------------------+

Acceso:
Selección banco → activación de fila → selección columna → prefetch → burst de datos

## Implicaciones en el rendimiento

- Los bancos múltiples permiten acceder a distintas partes de la memoria en paralelo, reduciendo esperas y mejorando el throughput.
- Las ráfagas (bursts) ayudan a mover grandes bloques de datos (por ejemplo, gráficos, vídeo, bases de datos) en menos ciclos, optimizando la eficiencia.
- El prefetch mayor en DDR más modernas es clave: cuanto más bits se anticipan, mayor es la velocidad efectiva.

---

# 2. Generaciones DDR (de DDR a DDR5)
Cada generación aumenta la eficiencia con prefetch mayor, voltajes menores y mejoras de señalización/topología. Las generaciones **no son físicamente compatibles** (muesca, pines, voltajes).

| Generación | Prefetch | Voltaje nominal | Características clave | Data rate JEDEC (MT/s) | Notas |
|---|:---:|:---:|---|---:|---|
| **DDR (1.x)** | 2n | 2.5 V | Primera generación DDR | hasta ~400 | Punto de partida histórico |
| **DDR2** | 4n | 1.8 V | On-Die Termination (ODT) | ~400–800 (hasta 1066) | — |
| **DDR3** | 8n | 1.5 V *(1.35 V DDR3L)* | Topología *fly-by* | 800–1600 (hasta 2133) | — |
| **DDR4** | 8n | 1.2 V | Bank groups, mejoras de entrenamiento, DBI | 1600–3200 | — |
| **DDR5** | 16n | 1.1 V | PMIC en el módulo, **2×32-bit subcanales por DIMM**, on-die ECC | 3200–6400 | Kits comerciales pueden superar JEDEC |


---

# 3. Formatos físicos (DIMM, SO-DIMM), pines y muescas
Los módulos se presentan en **DIMM** (escritorio/servidor) y **SO-DIMM** (portátil/SFF). El **número de pines** y la **posición de la muesca** evitan combinaciones incompatibles.

- **DIMM**: 240 pines (DDR3) → **288 pines (DDR4/DDR5)**.  
- **SO-DIMM**: 204 pines (DDR3) → **260 (DDR4)** → **262 (DDR5)**.  
- **UDIMM** (usuario/estación) vs **RDIMM/LRDIMM** (servidor): con registro/búfer para **mayor estabilidad/capacidad** por canal.

---

# 4. Rendimiento: MT/s, timings y latencia absoluta (con ejemplos)
El rendimiento práctico depende de **dos conceptos**: *tasa de transferencia* (MT/s → ancho de banda) y *latencias internas* (timings → tiempo de respuesta inicial).

La **tasa de transferencia** en DDR expresa cuántas **transferencias de datos por segundo** realiza la memoria. En DDR se mide en **MT/s** (*MegaTransfers per second*) porque la tecnología “double data rate” envía datos **dos veces por ciclo de reloj** (en los flancos de subida y de bajada).  
Por eso, si el reloj interno va a *f* MHz, la tasa efectiva es aproximadamente **MT/s = 2 × f**.

**Relación con el ancho de banda.** Cada canal de memoria mueve **64 bits = 8 bytes** por transferencia. El **ancho de banda teórico** de un canal puede aproximarse así:

## Ancho de banda (por canal)
Fórmula (base 10):  
`BW (GB/s) ≈ MT/s × 8 ÷ 1000` 

> Ejemplos:
> 
> **DDR4-3200** → `3200 × 8 ÷ 1000 ≈ 25,6 GB/s` por canal → **≈ 51,2 GB/s** en **dual channel**.  
> **DDR5-5600** → `5600 × 8 ÷ 1000 ≈ 44,8 GB/s` por canal → **≈ 89,6 GB/s** en **dual channel**.

## Latencia absoluta

Las **latencias** indican los **tiempos de espera internos** que necesita la DRAM para preparar y servir datos. Se publican en **ciclos** de reloj y suelen mostrarse como un conjunto:  

> **CL–tRCD–tRP–tRAS** (por ejemplo, *16-18-18-38*).

- **Cómo trabaja la DRAM.** Los datos están en una matriz de **filas** y **columnas** dentro de **bancos**. Para leer:

1) se **activa** una fila (tRCD),  
2) se **lee** una columna (CL),  
3) y al cambiar de fila se **pre-carga/cierra** la anterior (tRP).
El tiempo mínimo que una fila debe permanecer abierta es **tRAS**.

Formula:  
`tCL (ns) ≈ (CL × 2000) ÷ MT/s`  

> **Nota aclaratoria — ¿De dónde sale el “2000” en** `tCL(ns) ≈ (CL × 2000) / MT/s`?
>
> 1) **DDR duplica el reloj**  
>    En DDR la tasa se anuncia en **MT/s** (mega transfer por segundo) porque hay transferencia en **ambos flancos** del reloj.  
>    `MT/s = 2 × f(MHz)`  ⇒  `f(MHz) = MT/s ÷ 2`
>
> 2) **De MHz a nanosegundos**  
>    El periodo de un ciclo es `T = 1/f`. Si `f` está en MHz:  
>    `T(ns) = 1000 / f(MHz)`  
>    Sustituyendo `f(MHz) = MT/s ÷ 2`:  
>    `T(ns) = 1000 / (MT/s ÷ 2) = 2000 / MT/s`
>
> 3) **Latencia CAS en ns**  
>    La latencia publicada **CL** está en **ciclos**. En tiempo real:  
>    `tCL(ns) = CL × T(ns) = CL × (2000 / MT/s)`
>
> **Ejemplos**
>
> | Memoria | CL | MT/s | `T(ns) = 2000/MT/s` | `tCL(ns) ≈ CL × T` |
> |---|---:|---:|---:|---:|
> | DDR4-3200 | 16 | 3200 | 0.625 | 10.0 |
> | DDR5-5600 | 36 | 5600 | 0.357 | 12.9 |
>
> **Importante:** esta fórmula estima la **latencia inicial de lectura** en la DRAM.  
> La latencia “de punta a punta” puede ser mayor por colas del **controlador de memoria**, modos de reloj (p. ej., **Gear modes** / **FCLK:MCLK:UCLK**), y otros factores de la plataforma.


**Interpretación:** más **MT/s** acelera transferencias largas; **timings** más ajustados reducen el tiempo hasta el **primer dato**. En la práctica, **capacidad suficiente** y **doble canal** tienen impacto mayor que micro-ajustes de timings.

---

# 5. Canales, Ranks, Bank Groups y Subcanales (DDR5)
Son “trucos de organización” para **aumentar el paralelismo** y aprovechar mejor el bus.

- **Canales**: 1×64-bit por canal. Con **dual channel** (2 módulos) doblas el caudal.  
- **Ranks** (SR/DR/QR): agrupaciones lógicas; más ranks pueden facilitar **interleaving** y mejorar ocupación del bus (dentro de los límites de la IMC).  
- **Bank Groups**: permiten servir operaciones solapadas en bancos distintos con menos contención.  
- **Subcanales (DDR5)**: cada DIMM se parte en **2×32-bit** independientes a ciertos efectos, lo que suaviza burbujas y mejora eficiencia en accesos pequeños.

---

# 6. ECC, RDIMM/LRDIMM y fiabilidad
Son mecanismos para **detectar/corregir errores** y estabilizar señales cuando crecen densidades/capacidades.

- **ECC de sistema**: añade bits extra por palabra (72-bit por canal en ECC típico) y corrige errores de 1 bit (SECDED). Necesita **CPU + placa + módulos ECC** compatibles.  
- **On-die ECC (DDR5)**: corrige fallos **internos** del chip, transparente al sistema; **no** reemplaza al ECC de sistema.  
- **RDIMM/LRDIMM**: el **registro** y el **búfer** “limpian” señales y permiten **más módulos/capacidad** por canal; se usan en **servidores**.

---

# 7. Tabla comparativa de generaciones DDR


| Generación | Prefetch | Voltaje nominal | Data rate JEDEC (MT/s) | Pines **DIMM / SO-DIMM** | Organización de bus | PMIC | On-die ECC | Rasgos distintivos |
|---|:--:|:--:|:--:|:--:|---|:--:|:--:|---|
| **DDR**  | 2n  | 2.5 V | 200–400 | 184 / —   | 64-bit por DIMM | No | No | Origen DDR; obsoleta. |
| **DDR2** | 4n  | 1.8 V | 400–800 *(~1066)* | 240 / 200 | 64-bit por DIMM | No | No | ODT; mejoras de señalización. |
| **DDR3** | 8n  | 1.5 V *(1.35 V L)* | 800–1600 *(~2133)* | 240 / 204 | 64-bit por DIMM | No | No | Topología *fly-by*; mayor densidad. |
| **DDR4** | 8n  | 1.2 V | 1600–3200 | 288 / 260 | 64-bit por DIMM | No | No | **Bank groups**, DBI, entrenamiento. |
| **DDR5** | 16n | 1.1 V | 3200–6400 | 288 / 262 | **2×32-bit por DIMM** | **Sí** | **Sí** | **PMIC**, subcanales, más densidad. |


---

# 8. Pirámide jerárquica de memorias
Jerarquía por **latencia, ancho de banda, capacidad, coste/GB**. Cuanto más arriba, **más rápido y caro**; cuanto más abajo, **más grande y lento**.


El rendimiento y la eficiencia de los sistemas informáticos modernos dependen de una organización inteligente de las distintas tecnologías de memoria. Este modelo se representa habitualmente mediante una **pirámide de jerarquías de memoria**, como se ilustra a continuación:

---

<div style="text-align: center;">
  <img src="assets/memoria/piramide_memoria.webp" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>

---

En la cúspide de la pirámide se posicionan los **dispositivos más rápidos y costosos por byte**, pero de baja capacidad, tales como los **registros** (L0) y las **cachés** (L1, L2, L3, normalmente SRAM). Estos almacenan los datos e instrucciones de acceso más inmediato, acelerando así la ejecución del procesador.

A medida que se baja en la pirámide, se accede a memorias de **mayor capacidad y menor coste por byte**, pero menos veloces. En este contexto, la **memoria principal (L4)** corresponde a módulos **DDR SDRAM (Double Data Rate Synchronous Dynamic RAM)**, ampliamente extendidos en computadores actuales.

## El papel de la memoria DDR

- **Ubicación:** La memoria DDR se encuentra debajo de las cachés de último nivel (L3) y por encima del almacenamiento secundario (discos duros, SSD).
- **Función:** Aloja la mayoría de datos y programas activos; es accedida directamente por la CPU para operaciones en curso.
- **Velocidad:** Si bien es menos rápida que la caché, la memoria DDR ofrece un equilibrio óptimo entre velocidad, capacidad y coste, superando ampliamente el rendimiento de dispositivos de almacenamiento masivo.
- **Evolución:** Desde DDR hasta DDR5, cada generación ha incrementado aún más la velocidad y el ancho de banda disponible, mejorando el rendimiento global del sistema.

## Importancia de la jerarquía

La existencia de niveles de memoria con diferentes características permite a los sistemas maximizar el rendimiento y la eficiencia:
- Las memorias superiores proporcionan acceso ultrarrápido a los datos críticos.
- Las memorias intermedias (DDR) ofrecen un gran volumen de almacenamiento rápido para la ejecución eficiente de múltiples tareas.
- Los almacenamientos secundarios y remotos (L5, L6) proporcionan capacidad masiva a un coste bajo, aunque su acceso es mucho más lento.

---

**Resumen:**  
> La memoria DDR, como memoria principal dentro de la jerarquía, constituye el punto de equilibrio entre la rapidez de la caché y la capacidad del almacenamiento secundario. Su
> correcta selección y comprensión es esencial para el funcionamiento fluido y eficiente de cualquier sistema informático.


# 9. Compatibilidad, instalación y UEFI (checklist)

Una correcta instalación y configuración de la memoria DDR es clave para el funcionamiento y el rendimiento del sistema. Aquí tienes una lista para asegurar la compatibilidad y éxito en el proceso:

**Checklist práctico:**
- Verifica la **generación DDR** compatible con tu placa base (DDR3/DDR4/DDR5…).
- Comprueba el **voltaje** soportado.
- Consulta la **capacidad máxima** soportada (por módulo y total) en el manual de la placa.
- Confirma el **formato físico** (DIMM para escritorio, SO-DIMM para portátil).
- Instala los módulos en los **slots indicados** para aprovechar el canal dual/quad.
- Activa el perfil **XMP/DOCP** en UEFI/BIOS si tu memoria lo soporta.
- Prioriza módulos **certificados en la QVL** del fabricante.
- Actualiza la **UEFI/BIOS** antes de instalar RAM de alta frecuencia o capacidad.
- Coloca los módulos correctamente; ambos clips deben hacer “clic”.

---

# 10. Diagnóstico, pruebas y sintomatología típica

Los módulos de memoria defectuosos o mal instalados se manifiestan con síntomas concretos. Así puedes detectar y probar problemas:

**Síntomas habituales:**
- El PC no arranca o emite pitidos continuos (beeps POST).
- Reinicios inesperados, pantallas azules (BSOD), bloqueos de programas.
- Menos memoria reconocida de la instalada.
- Artefactos gráficos o errores aleatorios.

**Herramientas y acciones de diagnóstico:**
- **MemTest86+ / MemTest86:** testea la RAM fuera del sistema operativo.
- **Diagnóstico de memoria de Windows:** disponible en el menú de inicio.
- **CPU-Z / HWiNFO:** monitoriza frecuencias, latencias y canales activos.
- **Registro de eventos del SO:** busca errores relacionados con la RAM.
- **Pasos prácticos:**
   1. Apaga y desconecta el PC.
   2. Extrae y recoloca los módulos, prueba diferentes slots y módulos individualmente.
   3. Limpia contactos de RAM/ránuras.
   4. Actualiza la BIOS/UEFI.
   5. Ejecuta pruebas de memoria prolongadas.

---

# 11. Recomendaciones de compra y casos de uso

La selección de memoria DDR depende de tu equipo y necesidades. Aquí tienes ideas y consejos por perfil:

**Recomendaciones generales:**
- Escoge la **generación DDR** exacta según tu placa base.
- Preferiblemente compra módulos **de fabricantes reconocidos** y consultando la QVL.
- Mejor dos módulos iguales en **dual channel** excepto en sistemas muy limitados.
- Frecuencia y latencia: busca el equilibrio entre rendimiento y precio.
- **ECC** solo si es una exigencia de servidor o entorno crítico.

**Casos recomendados:**
- **Ofimática/básico:** 8-16GB DDR4/DDR5, dual channel, frecuencias estándar.
- **Gaming y edición:** 16-32GB DDR4/DDR5, mínimo 3000MT/s, latencia baja y perfil XMP.
- **Trabajo profesional:** 32-64GB+ DDR4/DDR5, quad channel si es posible, latencia mínima.
- **Servidor/virtualización:** RAM ECC, alto volumen (64GB~512GB), siempre verificar compatibilidad QVL.

> **Consejo:** Consulta siempre compatibilidad, lee los manuales y aprovecha ofertas en kits/módulos dobles.
