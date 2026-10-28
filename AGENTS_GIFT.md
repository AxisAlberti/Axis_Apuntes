# Normas para cuestiones en formato GIFT (Moodle)

Estas normas son obligatorias para cualquier cuestión generada en formato GIFT. Complementan a [AGENTS.md](AGENTS.md).

## 0. Normas generales de generación

- Las cuestiones generadas se guardarán en un fichero en la raíz del repositorio. El nombre del fichero debe incluir el nombre del módulo y el nivel de dificultad.
- Cuando se solicite generar cuestiones, se generará directamente el fichero `.gift` final; no se crearán módulos ni scripts en Python para esa tarea.
- Siempre se generarán 30 cuestiones de tipo cuestionario en formato GIFT.
- Al finalizar cada generación de cuestiones, se validará el fichero con las reglas de este documento.
- En cuestiones tipo test y de desarrollo, no se incluirán preguntas que obliguen a memorizar datos numéricos concretos (por ejemplo, nº de núcleos, tasas, latencias u otros valores específicos de dispositivos o conceptos).
- En preguntas tipo test y de desarrollo, los enunciados deben empezar por ¿ y terminar en ? y respetar tildes y ortografía correcta.
- En preguntas tipo test no se incluirán casos de taller. Si excepcionalmente se incluyen, deberán ser menos del 10% del total de preguntas del fichero.

## 1. Preguntas tipo test con penalización (formato GIFT)

Las preguntas tipo test para cuestionarios se generarán en **formato GIFT** de Moodle, con **una única respuesta correcta y varias incorrectas con penalización**.

### 1.0. Fuentes para generar preguntas

- Las preguntas deben basarse en los apuntes indicados.
- Complementar siempre con información actualizada de Internet.

### 1.1. Estructura básica de la pregunta

Cada pregunta seguirá esta estructura:

```gift
::Texto corto identificador de la pregunta::
Texto de la pregunta, lo más descriptiva posible. Puede plantear una situación práctica
relacionada con el contenido del archivo de teoría al que acompaña. {

=Respuesta correcta #Feedback formativo: explica por qué es correcta.
~%-33.3333%Respuesta incorrecta 1 #Feedback formativo: explica por qué NO es correcta.
~%-33.3333%Respuesta incorrecta 2 #Feedback formativo: explica por qué NO es correcta.
~%-33.3333%Respuesta incorrecta 3 #Feedback formativo: explica por qué NO es correcta.
}
```

### 1.2. Categorías Moodle (GIFT)

- Al generar cuestiones tipo test, la **primera línea** del fichero debe ser `$CATEGORY: SMR/Test/Nombre_de_la_unidad/Nivel`, donde `Nivel` es `Basico`, `Medio` o `Alto` según indique el usuario.
- Cada vez que se genere una unidad nueva, se deberá crear también su entrada de categoría en `scripts/SMR-categorias.gift` con el nombre normalizado de la unidad para Moodle.

```gift
$CATEGORY: SMR/Test/Nombre_de_la_unidad/Basico
```

El nombre de la unidad en la categoría debe estar **normalizado**:

- Sin tildes ni caracteres especiales
- Espacios reemplazados por `_`
- Solo letras, números, `_` y `-`
### 1.3 Obligatorio cuestiones (GIFT)

- Siempre se generarán exactamente 30 cuestiones.
- Cuando se pidan cuestiones, se entregará únicamente el fichero `.gift`; no se generarán scripts ni módulos de apoyo en Python.

- Evita enunciados del tipo ¿Qué describe mejor... y ¿Qué decisión es adecuada...

- Cualquier carácter usado en el formato GIFT que pueda generar conflicto, como los símbolos de porcentaje (%), tilde (~), igual (=), almohadilla (#), llaves ({, }), o dos puntos (::), deben ser escapados con una barra invertida \ para evitar errores de interpretación.

- En la retroalimentación de las cuestiones si se usan  símbolos de porcentaje (%), tilde (~), igual (=), almohadilla (#), llaves ({, }), o dos puntos (::), deben ser escapados con una barra invertida \ para evitar errores de interpretación.

- Estas dos reglas de escape deben comprobarse siempre al generar un fichero de cuestiones. Es obligatorio validar que se cumplen.

- El fichero con las cuestiones se almacena en el raíz del repositorio.

- Estás autorizado a buscar información en fuentes externas como internet.

### 1.4 Notación de bases en preguntas

- En las cuestiones de numeración, usar subíndice para indicar la base (por ejemplo: 1010₂, 3A₁₆, 725₈, 37₁₀).

### 1.5 Checklist de validación obligatoria (GIFT)

- 30 cuestiones exactamente.
- Primera línea con `$CATEGORY` correcto.
- Una única respuesta correcta y varias incorrectas con penalización.
- Fichero en la raíz del repositorio y nombre con módulo + dificultad.
- Escape de caracteres especiales en enunciados.
- Escape de caracteres especiales en retroalimentación.
- Subíndice para bases en numeración.


## 2. Preguntas tipo ensayo con editor HTML (formato GIFT Moodle)

Las preguntas de **tipo ensayo** con editor HTML en Moodle se representan en GIFT siguiendo este patrón:

```gift
$CATEGORY: RUTA/CATEGORIA

// question: ID_INTERNO  name: TÍTULO_VISIBLE_EN_MOODLE
::TITULO_INTERNO::[html]ENUNCIADO_EN_HTML{}
```

### 2.1 Categoría en cuestiones de ensayo

- Si el fichero contiene cuestiones tipo test, la primera línea sigue la regla de la sección 1.2 (`SMR/Test/Nombre_de_la_unidad/Nivel`), no la de esta sección.
- Esta regla se aplicará **a partir de ahora** a todas las nuevas cuestiones de **ensayo** (no aplica a tipo test).
- La cabecera `$CATEGORY` debe ser siempre: `SMR/Desarrollo/Titulo_del_tema`.
- El `Titulo_del_tema` debe corresponder al título del tema sobre el que se hacen las cuestiones.
- Normalizar el título del tema:
  - Sin tildes ni caracteres especiales.
  - Espacios reemplazados por `_`.
  - Solo letras, números, `_` y `-`.

Ejemplo para U10 (Tarjetas Gráficas):

```gift
$CATEGORY: SMR/Desarrollo/Tarjetas_Graficas
```

**Fecha de actualización:** 23/10/2026

**Fecha de actualización:** 23/10/2026
