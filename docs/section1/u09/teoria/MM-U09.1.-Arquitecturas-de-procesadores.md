---
title: "UD 09 - 9.1 Arquitecturas de procesadores"
description: "Arquitecturas de procesadores"
summary: "Arquitecturas de procesadores"
authors:
    - Jose Manuel Gonzalez Castillo
date: 2025-10-01
icon: "material/file-document-outline"
permalink: /mm/u09/9-1-arquitecturas-de-procesadores
categories:
    - "Montaje y Mantenimiento de Equipos Informaticos"
tags:
    - "arquitecturas"
---

# Arquitecturas de procesadores: SISC, CISC y RISC

## Introducción

La **arquitectura de un procesador** define cómo está diseñado internamente y cómo ejecuta las instrucciones. No se trata solo de la velocidad, sino de **cómo se organizan las instrucciones**, **cómo se comunican los componentes internos** y **cómo se aprovechan los recursos del hardware**.

A lo largo de la evolución de los procesadores han aparecido diferentes enfoques arquitectónicos. Los más importantes son:

- **SISC (Single Instruction Set Computer)**
- **CISC (Complex Instruction Set Computer)**
- **RISC (Reduced Instruction Set Computer)**

Cada uno responde a una filosofía distinta de diseño y ha tenido su importancia en diferentes momentos de la historia de la informática.

---

## 1. Arquitectura SISC (Single Instruction Set Computer)

### 1.1 ¿Qué es SISC?

La arquitectura **SISC** se basa en una idea muy simple:  
👉 **el procesador dispone de una única instrucción o de un conjunto extremadamente reducido de instrucciones**.

Toda operación, por compleja que sea, se realiza repitiendo esa instrucción básica con distintos datos.

### 1.2 Características principales

- Conjunto de instrucciones **mínimo o único**.
- Funcionamiento muy simple a nivel conceptual.
- Gran dependencia del software para realizar tareas complejas.
- No está pensada para ordenadores modernos de propósito general.

### 1.3 Ventajas

- Diseño extremadamente sencillo.
- Fácil de implementar a nivel teórico.
- Útil para comprender conceptos básicos de arquitectura de computadores.

### 1.4 Desventajas

- Muy poco eficiente para tareas reales.
- Gran número de ciclos para realizar operaciones complejas.
- No es práctica para sistemas modernos.

### 1.5 Uso real

La arquitectura SISC **no se utiliza en procesadores comerciales modernos**.  
Su importancia es **principalmente educativa**, para explicar:
- Cómo funciona una CPU.
- Qué es una instrucción.
- Cómo se construyen operaciones complejas a partir de operaciones simples.

---

## 2. Arquitectura CISC (Complex Instruction Set Computer)

### 2.1 ¿Qué es CISC?

La arquitectura **CISC** se basa en la idea de que el procesador debe disponer de un **conjunto amplio y complejo de instrucciones**, capaces de realizar operaciones avanzadas en una sola instrucción.

El objetivo original de CISC era:
- Reducir el número de instrucciones por programa.
- Simplificar el trabajo del programador.
- Aprovechar mejor la memoria, que antiguamente era muy cara y limitada.

### 2.2 Características principales

- Conjunto de instrucciones **muy amplio**.
- Instrucciones de **longitud variable**.
- Instrucciones que pueden realizar varias operaciones a la vez.
- Uso intensivo de **microcódigo** interno.
- Mayor complejidad del hardware.

### 2.3 Ejemplo de funcionamiento

Una instrucción CISC puede:
- Leer datos de memoria.
- Operar con ellos.
- Guardar el resultado en memoria.

Todo en una sola instrucción.

### 2.4 Ventajas

- Programas más compactos.
- Menor número de instrucciones por tarea.
- Compatibilidad hacia atrás (muy importante en la industria).

### 2.5 Desventajas

- Hardware más complejo.
- Instrucciones más lentas de ejecutar.
- Dificultad para optimizar el paralelismo y el pipeline.

### 2.6 Ejemplos de procesadores CISC

- **Intel x86**
- **Intel x86-64 (AMD64)**

👉 Aunque internamente muchos procesadores modernos traducen estas instrucciones a operaciones más simples, **externamente siguen siendo CISC** por compatibilidad.

---

## 3. Arquitectura RISC (Reduced Instruction Set Computer)

### 3.1 ¿Qué es RISC?

La arquitectura **RISC** se basa en una filosofía opuesta a CISC:  
👉 **usar un conjunto reducido de instrucciones simples**, optimizadas para ejecutarse muy rápido.

La idea principal es que:
- Las instrucciones simples se ejecutan en **un solo ciclo**.
- El compilador se encarga de combinar instrucciones simples para lograr tareas complejas.
- El hardware se simplifica y se hace más eficiente.

### 3.2 Características principales

- Conjunto de instrucciones **reducido y uniforme**.
- Instrucciones de **longitud fija**.
- Arquitectura **load/store**:
  - Solo algunas instrucciones acceden a memoria.
  - El resto opera con registros.
- Fácil implementación de **pipeline** y paralelismo.
- Menor consumo energético.

### 3.3 Ventajas

- Hardware más simple y eficiente.
- Mayor facilidad para paralelizar instrucciones.
- Mejor rendimiento por vatio.
- Ideal para dispositivos móviles y sistemas embebidos.

### 3.4 Desventajas

- Programas más largos (más instrucciones).
- Mayor dependencia del compilador.
- En sus inicios, menor compatibilidad con software antiguo.

### 3.5 Ejemplos de procesadores RISC

- **ARM** (móviles, tablets, servidores)
- **RISC-V**
- **PowerPC**
- **SPARC**

---

## 4. Comparación directa entre SISC, CISC y RISC

| Característica | SISC | CISC | RISC |
|--------------|------|------|------|
| Nº de instrucciones | Una o muy pocas | Muy alto | Reducido |
| Complejidad del hardware | Muy baja | Alta | Media / baja |
| Longitud de instrucciones | Fija | Variable | Fija |
| Acceso a memoria | Muy limitado | Directo en muchas instrucciones | Solo load/store |
| Facilidad de pipeline | Muy baja | Baja | Muy alta |
| Consumo energético | Muy bajo | Alto | Bajo |
| Uso actual | Educativo/Industrial | PCs y servidores | Móviles, servidores, embebidos |

---

## 5. Situación actual: ¿RISC o CISC hoy en día?

En la práctica actual:
- **Intel y AMD** siguen siendo **CISC** por compatibilidad.
- Internamente, traducen instrucciones CISC a **microoperaciones tipo RISC**.
- **ARM** domina móviles y está creciendo en servidores.
- **RISC-V** emerge como alternativa abierta y educativa.

👉 Esto demuestra que **las fronteras entre RISC y CISC se han difuminado**, combinando ideas de ambas arquitecturas.

---
