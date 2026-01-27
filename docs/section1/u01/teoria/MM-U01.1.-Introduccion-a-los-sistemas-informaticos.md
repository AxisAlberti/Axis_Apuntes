---
title: "UD 01 - 1.1 Introduccion a los sistemas informaticos"
description: "Introduccion a los sistemas informaticos"
summary: "Introduccion a los sistemas informaticos"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2025-10-01
icon: "material/file-document-outline"
permalink: /mm/u01/1-1-introduccion-a-los-sistemas-informaticos
categories:
    - "MON"
tags:
    - "introduccion"
---

## TEMA 1. INTRODUCCIÓN




---

# 1. Vocabulario

En el ámbito de los sistemas informáticos y el PC, existen numerosos conceptos fundamentales:

- **Hardware:** Son los componentes físicos que conforman un PC, como la placa base, procesador, memoria RAM, disco duro, unidad de procesamiento gráfico, dispositivos de entrada/salida, etc.
- **Software:** Son los programas y aplicaciones que permiten gestionar el hardware y realizar tareas específicas. Incluye el sistema operativo y los programas de usuario.
- **PC (Personal Computer):** Equipo informático individual diseñado para uso personal y profesional.
- **Procesador o CPU (Unidad Central de Procesamiento):** Circuito principal que interpreta y ejecuta instrucciones de los programas.
- **Memoria RAM (Memoria de Acceso Aleatorio):** Almacena temporalmente los datos e instrucciones que está utilizando el procesador, facilitando acceso rápido.
- **Almacenamiento:** Espacio donde se guardan los datos y programas de forma permanente (HDD, SSD).
- **Bus:** Sistema de canales que permite la comunicación de datos, direcciones y señales de control entre los componentes del PC.
- **Sistema operativo:** Software que gestiona los recursos del PC y facilita la interacción entre el usuario y el hardware.
- **Periféricos:** Elementos de entrada/salida conectados al PC como teclado, ratón, pantalla, impresora, etc.
- **Registros:** Pequeñas áreas de almacenamiento ultrarrápido dentro del procesador que guardan temporalmente datos e instrucciones.
- **ALU (Unidad aritmético-lógica):** Parte de la CPU que realiza cálculos matemáticos y operaciones lógicas.
- **Unidad de control:** Parte de la CPU que interpreta instrucciones y dirige el resto de los componentes para su ejecución.
- **Placa base:** Tarjeta principal que conecta y comunica todos los componentes del PC.

---

# 2. Introducción a los sistemas informáticos

Un sistema informático es una combinación de dispositivos y programas que permiten el procesamiento automático de información. Se compone, por lo general, de hardware, software, usuarios y datos.

**Hardware** incluye todos los componentes físicos que hacen posible el funcionamiento del sistema, desde el procesador hasta los distintos periféricos.  
**Software** es el conjunto de instrucciones, órdenes y programas que gestionan el hardware y posibilitan la realización de tareas.  
**Usuarios** son quienes utilizan el sistema informático, ya sea para tareas cotidianas, profesionales o lúdicas.  
**Datos** representan la información que es procesada y almacenada por el sistema informático.

Estos sistemas están presentes en todos los sectores de la sociedad actual: educación, ciencia, medicina, industria, comunicación, entretenimiento, administración, entre otros. Su principal función es transformar datos en información útil mediante el procesamiento, almacenamiento y transmisión eficaces.

---

# 3. Funcionamiento del PC

El PC es una máquina electrónica capaz de recibir, procesar, almacenar y mostrar información. Su funcionamiento se basa en la colaboración de hardware y software bajo la coordinación del sistema operativo.

El ciclo básico de funcionamiento se compone de varias fases:

**Entrada:**  
Los datos llegan al PC a través de dispositivos de entrada como el teclado, el ratón, la cámara, el escáner, los micrófonos, etc.

**Procesamiento:**  
El procesador (CPU) recibe los datos desde la memoria RAM, los interpreta, ejecuta instrucciones y realiza las operaciones necesarias. En el procesamiento intervienen otros componentes como la ALU (que realiza cálculos y operaciones lógicas), la unidad de control (que coordina la ejecución de instrucciones) y los registros internos.

**Almacenamiento:**  
La información puede ser guardada de manera temporal en la memoria RAM o de manera permanente en dispositivos de almacenamiento como discos duros, unidades de estado sólido o medios extraíbles (USB, DVDs). El acceso a la información almacenada puede ser necesario para futuras operaciones.

**Salida:**  
Finalmente, los resultados del procesamiento se muestran al usuario a través de dispositivos de salida, como la pantalla, altavoces, impresora o mediante retroalimentación por otros periféricos.

**Sistema operativo:**  
Actúa de intermediario haciendo posible la comunicación entre el usuario y el PC, gestionando los recursos y facilitando la ejecución de programas, la gestión de archivos y la interacción con periféricos.

---

# 4. La máquina de Von Neumann
<br>

<img src="../assets/vn.png" alt="Mi imagen"
     style="width:100%;height:auto;display:block;" />
La **arquitectura de Von Neumann** es el modelo sobre el que se basan la mayoría de los PC modernos. Propone que tanto los datos como las instrucciones se almacenan en la misma memoria, permitiendo que el procesador ejecute diversos programas sin necesidad de modificar el hardware.

## 4.1 Unidad Central de Procesamiento (CPU)

La CPU es el “cerebro” del PC, encargada de interpretar y ejecutar instrucciones. Está compuesta por varios subsistemas clave:

### 4.1.1 Unidad de control

- Lee y decodifica las instrucciones almacenadas en memoria.
- Determina qué acción debe ejecutarse y coordina el flujo de datos entre el resto de los componentes.
- Genera señales de control, activa/desactiva partes del hardware, gestiona el orden de ejecución y controla el acceso a los buses.
- Supervisa el ciclo de instrucción: captura, decodificación, ejecución y almacenamiento.

### 4.1.2 Unidad aritmético-lógica (ALU)

- Realiza cálculos matemáticos: sumas, restas, multiplicaciones, divisiones.
- Lleva a cabo operaciones lógicas: comparaciones, operaciones AND, OR, NOT, etc.
- Procesa datos binarios según las instrucciones recibidas y devuelve resultados al sistema.
- Es esencial para todas las operaciones que impliquen procesamiento de datos.

### 4.1.3 Registros

- Pequeñas memorias internas muy rápidas situadas dentro de la CPU.
- Almacenan datos de uso inmediato o temporal, como operandos, resultados intermedios y direcciones.
- Tipos típicos de registros: contador de programa (indica la instrucción actual), acumulador (almacena resultados), registros de propósito general (almacenan datos o direcciones temporales).
- Su acceso es casi instantáneo, mucho más rápido que la memoria principal.

---

## 4.2 Memoria principal

- Es el área donde se almacenan tanto las instrucciones (programas) como los datos que utiliza el sistema.
- Permite el acceso rápido desde la CPU.
- Generalmente, la memoria principal es la RAM, aunque también incluye cachés y otras tecnologías.
- Organizada en direcciones secuenciales; cada celda contiene un dato o instrucción.
- Ofrece capacidad de lectura y escritura: la CPU puede recuperar información o modificarla.

---

## 4.3 Dispositivos de entrada/salida (I/O)

- Permiten la comunicación entre el PC y el entorno externo (usuario, otros sistemas).
- Dispositivos de **entrada**: teclado, ratón, micrófono, escáner, cámaras, sensores.
- Dispositivos de **salida**: pantalla, impresora, altavoces, paneles LED, etc.
- Gestionados por controladores especializados que coordinan el acceso y la transferencia de datos entre el PC y los periféricos.
- El intercambio de información entre CPU y periferia se realiza a través de los buses correspondientes.

---

## 4.4 Buses

Son canales o conjuntos de líneas que transportan datos, instrucciones y señales de control entre los diferentes componentes.

- **Bus de datos:** Transfiere la información (datos binarios) entre la memoria, la CPU y los periféricos.
- **Bus de direcciones:** Determina la ubicación concreta de memoria o periférico que se va a utilizar.
- **Bus de control:** Transmite señales para coordinar la lectura, escritura, interrupciones y sincronización entre los distintos elementos del sistema.

Los buses integran la arquitectura, asegurando la comunicación efectiva y el funcionamiento conjunto de todos los módulos.

---

# 5. Tipos de buses en el PC

Los **buses** son sistemas de líneas de comunicación que conectan los diferentes componentes internos del PC, permitiendo la transferencia de información.

## 5.1 Bus de datos

El **bus de datos** se encarga de transportar la información (datos binarios) entre la CPU, la memoria y los periféricos.  
Su ancho (normalmente en bits) determina cuántos datos pueden transferirse simultáneamente. Por ejemplo, un bus de 8 bits permite transferir 8 bits en paralelo; uno de 64 bits, 64 bits a la vez.

## 5.2 Bus de direcciones

El **bus de direcciones** indica la posición de memoria o periférico a la que la CPU quiere acceder.  
Esto permite seleccionar un lugar concreto para leer o escribir datos. La cantidad de líneas de direcciones determina el número máximo de ubicaciones accesibles. Por ejemplo, un bus de direcciones de 32 líneas puede direccionar \(2^{32}\) posiciones de memoria.

## 5.3 Bus de control

El **bus de control** transporta señales que coordinan y regulan el funcionamiento interno del PC, gestionando órdenes de lectura/escritura, interrupciones, selección de dispositivos, señalización del reloj y otras tareas de sincronización.

## 5.4 Interacciones

Estos tres tipos de buses trabajan de forma coordinada:

- Cuando la CPU necesita leer un dato de memoria, utiliza el bus de direcciones para indicar la ubicación, el bus de control para enviar la señal de lectura y el bus de datos para recibir la información.
- Para escribir un dato, la CPU marca la dirección y usa el bus de control para enviar la señal de escritura, transfiriendo el dato por el bus de datos.

Además, los buses permiten la expansión y actualización de sistemas mediante la incorporación de periféricos, tarjetas de expansión, y otros componentes.

---
