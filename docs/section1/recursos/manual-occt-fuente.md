# 🔌 Mini manual: prueba de fuente de alimentación con OCCT

Para probar la fuente con OCCT, en realidad se somete al equipo a una carga combinada alta de CPU y GPU para comprobar si la alimentación se mantiene estable bajo estrés real.

<figure markdown>
  ![](assets/occt_logomark.svg){ width="120" }
  <figcaption>OCCT es una herramienta de estrés y monitorización útil para validar estabilidad.</figcaption>
</figure>

## 1. Preparación previa

1. Descarga e instala OCCT desde su web oficial.
2. Cierra programas innecesarios para evitar interferencias.
3. Revisa que ventiladores, filtros y flujo de aire estén limpios.
4. Abre monitorización de sensores (OCCT, HWiNFO o HWMonitor).

Antes de empezar, conviene anotar temperaturas en reposo (CPU y GPU), voltajes reportados por placa y comportamiento acústico del equipo. Así tendrás una referencia para comparar.

## 2. Selección de la prueba en OCCT

1. Abre OCCT.
2. En el panel de pruebas, elige `Power` o `Power Supply` (según versión).
3. Este modo carga CPU y GPU a la vez para exigir consumo elevado.

Ajustes recomendados:

- Duración inicial: 15-20 minutos.
- Si todo es estable: repetir entre 30 y 60 minutos.
- Modo: `Auto` o `Normal` (solo usar modos extremos para escenarios concretos de overclock).

<figure markdown>
  ![](assets/occt_testing_cpu.png)
  <figcaption>Vista de pruebas de OCCT para configurar carga y tiempo de ejecución.</figcaption>
</figure>

## 3. Qué vigilar durante la prueba

OCCT mostrará gráficas de:

- Voltajes: 12 V, 5 V y 3.3 V (lectura de sensores de placa).
- Temperaturas: CPU, GPU y, si está disponible, placa base/VRM.
- Frecuencias y porcentaje de carga de CPU/GPU.

Señales de funcionamiento correcto:

- El equipo no se apaga, no reinicia y no se congela.
- No aparecen errores de cálculo ni alertas críticas.
- Las temperaturas se estabilizan sin sobrepasar límites seguros del fabricante.

Rangos de referencia habituales:

- 12 V: entre 11.4 V y 12.6 V.
- 5 V: entre 4.75 V y 5.25 V.
- 3.3 V: entre 3.14 V y 3.47 V.

Nota: las lecturas por software orientan, pero no sustituyen una comprobación con multímetro si hay sospecha de fallo eléctrico.

<figure markdown>
  ![](assets/occt_monitoring.png)
  <figcaption>Panel de monitorización de OCCT para revisar voltajes, temperatura y estabilidad.</figcaption>
</figure>

## 4. Interpretación rápida de resultados

- Sin cuelgues, sin reinicios y sin caídas bruscas de voltaje: la fuente parece estable en carga.
- Reinicios, apagones, pantallazos o descenso acusado de 12 V: posible problema de PSU, VRM o placa.
- Si hay síntomas repetidos: repetir prueba y contrastar con otra fuente conocida o medición eléctrica.

## 5. Seguridad y buenas prácticas

- No prolongues pruebas innecesariamente: 30-60 minutos suelen bastar.
- Si oyes ruidos eléctricos anómalos (chasquidos, zumbidos intensos) detén la prueba.
- Si aparece olor a quemado, para inmediatamente y corta alimentación.
- En equipos con fuente ajustada en potencia, usa pruebas más cortas y supervisadas.
- No dejes el test sin vigilancia continua.

**Fecha de actualización:** 17/02/2026
