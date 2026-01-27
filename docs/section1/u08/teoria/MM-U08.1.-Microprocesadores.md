---
title: "UD 08 - 8.1 Microprocesadores"
description: "Microprocesadores"
summary: "Microprocesadores"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2025-10-01
icon: "material/file-document-outline"
permalink: /mm/u08/8-1-microprocesadores
categories:
    - "MON"
tags:
    - "microprocesadores"
---

## TEMA 8. MICROPROCESADOR

### Consulta también  [Guia Eleccion](../../A4/teoria/A4-1-Guia-para-elegir-procesador.md).
### Nomenclatura procesadores  [Sufijos](../../A5/teoria/A5-1-Nomenclatura-de-procesadores.md).
### Arquitectura [Arquitectura](../../A1/teoria/A1-1-Arquitecturas-de-procesadores.md)
### Procesos [Procesos](../../A2/teoria/A2-1-Procesos-e-hilos.md)



---

# 1. Qué es el microprocesador

El **microprocesador**, también conocido como **CPU (Central Processing Unit)**, es el componente fundamental de cualquier sistema informático moderno. Su función principal es **interpretar, procesar y ejecutar instrucciones**, que son las órdenes básicas que indican al ordenador qué operaciones debe realizar.

Cada acción que realiza un ordenador —desde escribir una letra en un teclado hasta reproducir un vídeo o ejecutar un programa— pasa directa o indirectamente por el microprocesador. Por este motivo, se le suele llamar el *cerebro del ordenador*, ya que controla y coordina el funcionamiento del resto de componentes.

Desde el punto de vista físico, el microprocesador es un **circuito integrado** fabricado sobre una oblea de silicio. En su interior contiene **millones o miles de millones de transistores**, que funcionan como interruptores electrónicos capaces de representar valores binarios (0 y 1). A partir de combinaciones de estos valores binarios, el procesador puede realizar cualquier cálculo lógico o matemático.

El microprocesador no trabaja de forma aislada, sino que mantiene una comunicación constante con:
- La **memoria RAM**, donde se almacenan los programas y datos en uso.
- Los **dispositivos de entrada** (teclado, ratón, sensores).
- Los **dispositivos de salida** (pantalla, impresora, altavoces).
- Los sistemas de **almacenamiento** (SSD, HDD).
- El resto de controladoras y buses del sistema.

Sin microprocesador, un ordenador no puede arrancar ni ejecutar ninguna tarea.

---

# 2. CPU y GPU: diferencias y complementariedad

Aunque tanto la **CPU** como la **GPU** son tipos de procesadores, su diseño interno y su finalidad son muy distintos.

La **CPU** está diseñada para:
- Ejecutar instrucciones complejas.
- Tomar decisiones lógicas.
- Controlar el flujo de ejecución de los programas.
- Gestionar memoria, procesos y dispositivos.
- Cambiar rápidamente de una tarea a otra.

Por ello, la CPU suele tener **pocos núcleos**, pero cada núcleo es muy potente y flexible.

La **GPU**, en cambio, está diseñada para:
- Realizar una enorme cantidad de cálculos simples en paralelo.
- Trabajar con grandes bloques de datos.
- Procesar gráficos, vídeo, aprendizaje automático e inteligencia artificial.

Una GPU puede tener **cientos o miles de núcleos simples**, capaces de ejecutar la misma operación sobre muchos datos al mismo tiempo.

En los sistemas actuales, CPU y GPU trabajan juntas:
- La CPU coordina y gestiona.
- La GPU acelera tareas altamente paralelizables.

---

# 3. Funcionamiento interno del microprocesador

El microprocesador funciona siguiendo un **ciclo de instrucción**, que se repite millones o miles de millones de veces por segundo.

Este ciclo consta de varias fases bien definidas:

## 3.1 Prefetch
El procesador intenta anticiparse a las necesidades futuras, cargando instrucciones antes de que sean necesarias. Esto reduce tiempos de espera.

## 3.2 Fetch
La instrucción se obtiene desde la memoria, normalmente desde la caché, y se introduce en el procesador.

## 3.3 Decodificación
La unidad de control interpreta la instrucción, determina qué operación se debe realizar y qué unidades internas se deben utilizar.

## 3.4 Lectura de operandos
Se obtienen los datos necesarios para ejecutar la instrucción, ya sea desde registros internos, caché o memoria RAM.

## 3.5 Ejecución
Las unidades de ejecución (ALU, FPU, unidades vectoriales, etc.) realizan la operación correspondiente.

## 3.6 Escritura
El resultado se almacena en un registro o se escribe de nuevo en memoria.

Este proceso se sincroniza con el **reloj del procesador**, cuya frecuencia se mide en **GHz**. Sin embargo, el rendimiento real depende más de la arquitectura que de la frecuencia bruta.

---

# 4. Unidad aritmético-lógica (ALU) y unidad de coma flotante (FPU)

La **ALU (Arithmetic Logic Unit)** es la unidad encargada de realizar operaciones matemáticas básicas (suma, resta, multiplicación, división) y operaciones lógicas (AND, OR, NOT, comparaciones).

La **FPU (Floating Point Unit)** es una unidad especializada que realiza cálculos con **números en coma flotante**, es decir, números con decimales. Estos cálculos son mucho más complejos y requieren una precisión especial.

Las operaciones en coma flotante son fundamentales en:
- Ingeniería y ciencia.
- Gráficos 3D.
- Simulación física.
- Edición de vídeo y audio.
- Inteligencia artificial.

En procesadores modernos, la FPU está integrada dentro de cada núcleo, permitiendo ejecutar varias operaciones de coma flotante en paralelo y con gran precisión.

---

# 5. Memoria caché y jerarquía de memoria

La **memoria caché** existe porque hay una enorme diferencia de velocidad entre el microprocesador y la memoria RAM. Si la CPU tuviera que esperar siempre a la RAM, gran parte de su potencia se desperdiciaría.

La caché actúa como un **almacén intermedio ultrarrápido**, donde se guardan datos e instrucciones que se usan con frecuencia.

## 5.1 Caché L1
- Extremadamente rápida.
- Muy pequeña.
- Situada dentro del núcleo.
- Contiene datos e instrucciones inmediatas.

## 5.2 Caché L2
- Más grande que la L1.
- Algo más lenta.
- Reduce accesos a RAM cuando la L1 falla.

## 5.3 Caché L3
- Compartida entre varios núcleos.
- Gran tamaño.
- Fundamental en procesadores multinúcleo.

La correcta gestión de la caché es clave para el rendimiento real del sistema.

---

# 6. Núcleos, hilos y tecnologías de multihilo

El rendimiento de un microprocesador moderno no depende únicamente de su frecuencia de reloj. Uno de los factores más importantes es la forma en la que el procesador **divide y ejecuta el trabajo en paralelo**, lo cual se consigue mediante el uso de **núcleos**, **hilos** y **tecnologías de multihilo**.

Comprender correctamente estos conceptos es fundamental para entender cómo funcionan los sistemas actuales, por qué ciertos programas se ejecutan más rápido que otros y cómo se aprovecha realmente la potencia de una CPU.

---

## 6.1 Núcleos (cores)

Un **núcleo** es una **unidad de procesamiento física independiente** dentro de un microprocesador. Cada núcleo dispone de sus propias unidades de ejecución (ALU, FPU, registros, etc.) y puede ejecutar instrucciones de forma autónoma.

En los primeros ordenadores personales, los procesadores eran **mononúcleo**, es decir, solo podían ejecutar una tarea de forma real en cada instante. La multitarea se conseguía mediante cambios rápidos de contexto, dando la sensación de que varias aplicaciones se ejecutaban a la vez.

Con la aparición de los **procesadores multinúcleo**, un mismo chip puede contener varios núcleos físicos, lo que permite:
- Ejecutar varios programas al mismo tiempo.
- Repartir la carga de trabajo entre núcleos.
- Mejorar el rendimiento en aplicaciones paralelas.
- Aumentar la eficiencia energética frente a subir únicamente la frecuencia.

Ejemplos habituales:
- Doble núcleo (dual-core)
- Cuádruple núcleo (quad-core)
- Seis, ocho o más núcleos en CPUs modernas

Cada núcleo puede ejecutar un proceso o hilo distinto, lo que permite un verdadero paralelismo.

---

## 6.2 Hilos (threads)

Un **hilo (thread)** es una **línea de ejecución dentro de un proceso**. Un proceso (por ejemplo, un navegador web) puede dividir su trabajo en varios hilos para ejecutarse de forma más eficiente.

Ejemplos de uso de hilos:
- Un navegador puede usar un hilo por pestaña.
- Un juego puede usar hilos separados para gráficos, física, sonido e inteligencia artificial.
- Un servidor puede usar un hilo por cada cliente conectado.

El **sistema operativo** es el encargado de:
- Crear los hilos.
- Asignarlos a los núcleos disponibles.
- Cambiar entre hilos cuando es necesario.

Si hay más hilos que núcleos físicos, el procesador alterna rápidamente entre ellos mediante **cambio de contexto**, dando la sensación de ejecución simultánea.

Cuantos más hilos pueda gestionar eficientemente un procesador, mejor será su capacidad de multitarea.

---

## 6.3 Relación entre núcleos e hilos

La relación entre núcleos e hilos es clave para entender el rendimiento real de un procesador.

- Un procesador **sin multihilo** ejecuta un hilo por núcleo.
- Un procesador **con multihilo** puede ejecutar varios hilos por núcleo.

Ejemplo sencillo:
- CPU de 4 núcleos sin multihilo → 4 hilos simultáneos
- CPU de 4 núcleos con multihilo → 8 hilos simultáneos (dependiendo de la tecnología)

Es importante entender que **un hilo no es un núcleo físico**. Los hilos comparten recursos internos del núcleo, por lo que su rendimiento depende de cómo se aprovechen dichos recursos.

---

## 6.4 Tecnologías de multihilo: Hyper-Threading y SMT

**VIDEO EXPLICATIVO https://www.youtube.com/watch?v=A621YkxaejY **

Las tecnologías de multihilo permiten que **un único núcleo físico ejecute más de un hilo al mismo tiempo**.

---
<div style="text-align: center;">
  <img src="../assets/micro/ht1.jpg" alt="Descripción de la imagen" style="display: block; margin: 0 auto; max-width: 100%; height: auto;">
</div>
---

### 6.4.1 Hyper-Threading (Intel)

**Hyper-Threading** es una tecnología desarrollada por Intel que permite que cada núcleo físico se comporte como **dos núcleos lógicos** desde el punto de vista del sistema operativo.

Esto se consigue duplicando ciertos elementos internos del núcleo (como registros y contadores), mientras que otros recursos se comparten (ALU, FPU, caché, etc.).

Ejemplo:
- CPU con 4 núcleos físicos y Hyper-Threading activado
- El sistema operativo detecta 8 procesadores lógicos

Ventajas:
- Mejor aprovechamiento de los recursos internos.
- Aumento del rendimiento en aplicaciones multihilo.
- Mejora de la multitarea.

Limitaciones:
- No duplica la potencia del núcleo.
- El aumento de rendimiento depende del tipo de aplicación.
- En tareas muy intensivas puede no haber mejora significativa.

---

### 6.4.2 SMT (Simultaneous Multithreading)

**SMT** es el nombre genérico de esta técnica y es utilizado por otros fabricantes, como AMD.

El principio es el mismo:
- Ejecutar varios hilos de forma simultánea en un mismo núcleo.
- Aprovechar ciclos de ejecución que quedarían desaprovechados.

En algunos procesadores avanzados, un núcleo puede manejar más de dos hilos simultáneos, aunque lo habitual en equipos de sobremesa es **2 hilos por núcleo**.

---

## 6.5 Ventajas del multihilo

El uso de núcleos múltiples y tecnologías de multihilo ofrece numerosas ventajas:

- Mayor rendimiento en aplicaciones paralelas.
- Mejor respuesta del sistema bajo carga.
- Mejor aprovechamiento del hardware.
- Mayor eficiencia energética comparada con aumentar solo la frecuencia.

Estas ventajas son especialmente importantes en:
- Servidores.
- Estaciones de trabajo.
- Edición de vídeo.
- Virtualización.
- Compilación de software.

---

## 6.6 Limitaciones y consideraciones

Aunque el multihilo ofrece muchas ventajas, también tiene limitaciones:

- No todas las aplicaciones están programadas para usar múltiples hilos.
- Algunos programas solo pueden ejecutarse de forma secuencial.
- Los hilos comparten recursos, lo que puede generar cuellos de botella.
- El rendimiento depende del sistema operativo y del software.

Por este motivo, un procesador con muchos hilos no siempre es más rápido en todas las tareas que uno con menos núcleos pero mayor rendimiento por núcleo.



---

# 7. Integración de controladoras y evolución del northbridge

En arquitecturas antiguas, funciones clave como la controladora de memoria estaban en el **northbridge**, un chip separado.

En las CPUs modernas, estas funciones se han **integrado directamente en el procesador**, lo que ha supuesto una gran mejora de rendimiento.

## 7.1 Controladora de memoria integrada (IMC)

La IMC permite que la CPU se comunique directamente con la RAM:
- Reduce latencia.
- Aumenta ancho de banda.
- Mejora rendimiento multinúcleo.

## 7.2 Integración del northbridge

La CPU moderna integra:
- Controlador de memoria.
- Líneas PCI Express.
- Comunicación con GPU integrada.

Esto simplifica el diseño y mejora la eficiencia.

---

# 8. Gráficos, entrada y salida integrados en la CPU

Muchas CPUs incluyen una **GPU integrada**, lo que permite:
- Reducir costes.
- Reducir consumo.
- Simplificar equipos.

Además, la CPU gestiona directamente buses de alta velocidad como **PCIe**, **NVMe**, **DMI** o **Infinity Fabric**, reduciendo cuellos de botella.

---

# 9. Mejoras internas de rendimiento en procesadores modernos

Las CPUs actuales incluyen técnicas como:
- Ejecución fuera de orden.
- Predicción de saltos avanzada.
- Prefetching inteligente.
- Cachés compartidas.
- Políticas dinámicas de ejecución.

Estas técnicas permiten hacer más trabajo por ciclo sin aumentar excesivamente la frecuencia.

---

# 10. Virtualización asistida por hardware

Las extensiones **Intel VT-x** y **AMD-V** permiten ejecutar máquinas virtuales con menor sobrecarga.

Las tecnologías **VT-d** e **IOMMU** permiten asignar dispositivos físicos a máquinas virtuales, mejorando rendimiento y seguridad.

---

# 11. Seguridad y confiabilidad a nivel hardware

Las CPUs modernas incluyen:
- Bit NX/DEP.
- Arranque seguro.
- Cifrado de memoria.
- Enclaves seguros.

En entornos profesionales:
- Soporte ECC.
- Corrección de errores.
- Scrubbing de memoria.

---

# 12. Gestión avanzada de energía y temperatura

En los microprocesadores modernos, el rendimiento ya no se basa únicamente en ejecutar instrucciones lo más rápido posible, sino en **hacerlo de forma eficiente**, controlando cuidadosamente el **consumo energético** y la **temperatura**. Por este motivo, las CPUs actuales incorporan sistemas avanzados de **gestión dinámica de energía y temperatura**, que ajustan su funcionamiento en tiempo real según la carga de trabajo.

Esta gestión es fundamental para:
- Evitar daños físicos en el procesador.
- Reducir el consumo eléctrico.
- Mejorar la eficiencia energética.
- Aumentar la vida útil del equipo.
- Mantener un equilibrio entre rendimiento y ruido (ventiladores).

---

## 12.1 Ajuste dinámico de frecuencia

La **frecuencia de reloj** de una CPU indica cuántos ciclos puede ejecutar por segundo y se mide en **GHz**. Tradicionalmente, los procesadores funcionaban siempre a una frecuencia fija, pero esto resultaba ineficiente cuando el equipo estaba en reposo o realizando tareas ligeras.

Las CPUs modernas pueden:
- **Aumentar la frecuencia** cuando se necesita más rendimiento.
- **Reducir la frecuencia** cuando la carga es baja.

Este ajuste dinámico permite ahorrar energía y reducir la temperatura sin sacrificar rendimiento cuando realmente se necesita.

Ejemplo:
- Navegar por Internet → frecuencia baja.
- Compilar un programa o jugar → frecuencia alta (modo turbo).

---

## 12.2 Ajuste dinámico de voltaje

El **voltaje** es la energía eléctrica que alimenta al microprocesador. A mayor voltaje:
- Mayor consumo eléctrico.
- Mayor generación de calor.

Las CPUs actuales ajustan el voltaje **junto con la frecuencia**, ya que ambos están estrechamente relacionados. Si la frecuencia baja, el voltaje también puede reducirse, lo que disminuye significativamente el consumo energético.

Este ajuste dinámico es clave para:
- Mejorar la eficiencia.
- Reducir el calentamiento.
- Evitar un consumo innecesario en tareas simples.

---

## 12.3 Estados de energía: P-states y C-states

Los procesadores utilizan **estados de energía** para adaptarse a la carga de trabajo del sistema.

### P-states (Performance States)

Los **P-states** controlan el **nivel de rendimiento del procesador**:
- Frecuencia.
- Voltaje.

Ejemplo:
- P0 → máximo rendimiento.
- P1, P2, P3… → rendimiento progresivamente menor.

Cuando el sistema necesita potencia, la CPU sube a un P-state alto. Cuando la carga baja, desciende a estados más eficientes.

---

### C-states (Idle States)

Los **C-states** controlan el comportamiento del procesador cuando **no está ejecutando instrucciones**.

- C0 → el núcleo está activo.
- C1 → reposo ligero.
- C6, C7… → reposo profundo, con partes del núcleo apagadas.

Cuanto más profundo es el C-state:
- Menor consumo.
- Mayor ahorro energético.
- Mayor latencia al volver a estar activo.

Estos estados son especialmente importantes en:
- Portátiles.
- Servidores.
- Equipos encendidos muchas horas.

---

## 12.4 Sensores térmicos y protección del procesador

Las CPUs modernas incorporan **sensores térmicos internos** distribuidos por todo el chip. Estos sensores:
- Miden la temperatura en tiempo real.
- Detectan puntos calientes.
- Informan al sistema de control energético.

Si la temperatura supera ciertos límites:
- Se reduce automáticamente la frecuencia (thermal throttling).
- Se limita el voltaje.
- En casos extremos, el sistema se apaga para evitar daños.

Estas protecciones evitan:
- Daños permanentes en el silicio.
- Fallos del sistema.
- Reducción drástica de la vida útil del procesador.

---

## 12.5 Consumo energético y vatios (W)

El **consumo energético** de un procesador se mide en **vatios (W)** y representa la cantidad de energía que utiliza durante su funcionamiento.

Es importante entender que:
- Un procesador no consume siempre la misma cantidad de vatios.
- El consumo varía según la carga, la frecuencia y el voltaje.
- En reposo, el consumo puede ser muy bajo.
- En carga máxima, el consumo puede aumentar considerablemente.

Por ejemplo:
- Un procesador puede consumir 10–15 W en reposo.
- Bajo carga intensa, puede superar ampliamente los 100 W.

---

## 12.6 Qué es el TDP y qué significa realmente

El **TDP (Thermal Design Power)** es uno de los conceptos más importantes —y a la vez más malinterpretados— en los procesadores.

El TDP:
- Se expresa en vatios (W).
- Indica el **calor máximo que el sistema de refrigeración debe ser capaz de disipar**.
- No es exactamente el consumo real máximo, sino una **referencia térmica**.

Ejemplo:
- Un procesador con TDP de 65 W necesita un sistema de refrigeración capaz de disipar al menos esa cantidad de calor.

En procesadores modernos:
- El consumo real puede superar el TDP durante picos de rendimiento (modo turbo).
- Esto es normal y está previsto por el fabricante.

---

## 12.7 Importancia actual del TDP en la elección de procesadores

Hoy en día, el TDP es clave para:
- Elegir correctamente el sistema de refrigeración.
- Diseñar equipos silenciosos.
- Montar equipos compactos o portátiles.
- Optimizar consumo energético en servidores.

Un procesador con alto TDP:
- Ofrece más rendimiento sostenido.
- Genera más calor.
- Requiere mejor refrigeración.
- Consume más energía eléctrica.

Un procesador con bajo TDP:
- Consume menos.
- Genera menos calor.
- Es ideal para equipos pequeños, portátiles o de bajo ruido.

---

## 12.8 Tecnologías de turbo dinámico

Los fabricantes incluyen tecnologías como:
- **Intel Turbo Boost**
- **AMD Precision Boost**

Estas tecnologías permiten que la CPU:
- Supere su frecuencia base.
- Aumente el consumo y la temperatura temporalmente.
- Aproveche el margen térmico disponible.

El sistema decide automáticamente:
- Cuándo subir la frecuencia.
- Cuánto tiempo mantenerla.
- Cuándo reducirla para proteger el procesador.

---

## 12.9 Importancia para el montaje y mantenimiento

Para el alumnado de montaje y mantenimiento, comprender la gestión energética es esencial para:
- Elegir una fuente de alimentación adecuada.
- Seleccionar un disipador correcto.
- Diagnosticar problemas de sobrecalentamiento.
- Entender por qué un procesador baja su rendimiento (throttling).
- Optimizar equipos según su uso.


---

# 13. Procesamiento multinúcleo y multiprocesador

Los sistemas modernos utilizan:
- Múltiples núcleos.
- Varias CPUs físicas en servidores.

Esto permite ejecutar múltiples tareas simultáneamente y mejorar rendimiento y disponibilidad.

---

## Conclusión

El microprocesador moderno es un sistema extremadamente complejo que integra cálculo, memoria, gráficos, entrada/salida, seguridad, virtualización y gestión energética. Comprender su funcionamiento interno es fundamental para cualquier estudiante de informática, sistemas o mantenimiento de equipos.
