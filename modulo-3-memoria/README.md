# Módulo 3 — La memoria de GEOIA
**Día 2 · lo construyes tú**

> **Aquí va tu Módulo 3.** El agente creará el archivo **`main.py`** (y una base de
> datos `lugares.db`) en esta misma carpeta.

## Qué vas a conseguir

Una **base de datos**: la **memoria que no se borra**. Un archivo donde los lugares se
guardan **de verdad**, así que **apagas y enciendes** el servidor y **siguen ahí**.
Usas **SQLite**, que ya viene con Python (no instalas nada extra para esto).

## Antes de empezar

- Tu agente de IA abierto con la carpeta `taller-geo-ia` (ver
  [`../INSTRUCCIONES.md`](../INSTRUCCIONES.md)).
- Necesitas **uv** (para Python). Si no lo tienes, el agente lo prepara — o pega
  [`../prompts/antes-preparar-python.txt`](../prompts/antes-preparar-python.txt).

## El prompt de partida (cópialo y pégalo)

Copia y pega **[`../prompts/dia2-memoria.txt`](../prompts/dia2-memoria.txt)**. Creará
`modulo-3-memoria/main.py` y te enseñará cómo arrancarlo.

## Cómo saber que va bien

1. Aparece el archivo **`lugares.db`** y en `/docs` el **`GET /lugares`** da los **18**.
2. **El momento clave:** haces un **`POST`** con un lugar nuevo, **paras y arrancas** el
   servidor, vuelves a pedir `GET /lugares`… y **tu lugar sigue ahí**. 🎉

> ¿Sale un error? **Cópialo entero y pégaselo al agente.**

## Ahora tú (retos)

Borrar o editar un lugar, ordenarlos, guardar la fecha en que lo añadiste… y el **broche
final del taller: compartir tu app con un enlace** (pega
[`../prompts/dia2-compartir.txt`](../prompts/dia2-compartir.txt)). Todos los retos, con
el detalle, en **[`../guia/hoja-de-ruta.md`](../guia/hoja-de-ruta.md)**.
