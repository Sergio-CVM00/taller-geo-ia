# Módulo 2 — El servidor de GEOIA
**Día 2 · normalmente lo monta el presentador y tú lo sigues**

> **Aquí va tu Módulo 2.** El agente creará el archivo **`main.py`** en esta misma
> carpeta. (Por eso la carpeta ya existe: para que sepas dónde va.)

## Qué vas a conseguir

Un **servidor**, como un **camarero**: un programita en **Python** que **sirve** la
lista de lugares y deja **añadir** nuevos. No se ve como una web; se prueba en una
página automática (**`/docs`**), sin escribir código.

## Antes de empezar

- Tu agente de IA abierto con la carpeta `taller-geo-ia` (ver
  [`../INSTRUCCIONES.md`](../INSTRUCCIONES.md)).
- Necesitas **uv** (para Python). Si no lo tienes, el agente lo prepara — o pega
  [`../prompts/antes-preparar-python.txt`](../prompts/antes-preparar-python.txt).

## El prompt de partida (cópialo y pégalo)

Copia y pega **[`../prompts/dia2-servidor.txt`](../prompts/dia2-servidor.txt)**. Creará
`modulo-2-servidor/main.py` y te enseñará cómo arrancarlo.

## Cómo saber que va bien

1. El agente te da una dirección tipo **`http://localhost:8722`**; le añades **`/docs`**.
2. En `/docs` aparecen **`GET /lugares`** (devuelve los **18**) y **`POST /lugares`**
   (tras añadir uno, hay **19**).
3. Si paras el servidor, los nuevos **se pierden**: es "en memoria". Eso lo arregla el
   **Módulo 3**.

> ¿Sale un error? **Cópialo entero y pégaselo al agente.**

## Ahora tú (retos)

Súbele el nivel de una mejora en una: pedir un lugar por su id, filtrar por categoría,
borrar, servir tu propio mapa desde el servidor… Todos los retos, con el detalle y cómo
saber que van bien, en **[`../guia/hoja-de-ruta.md`](../guia/hoja-de-ruta.md)**.
