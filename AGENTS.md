# Reglas del proyecto para el asistente de IA

> **Para quién es esto:** reglas para el asistente de IA (p. ej. Google
> Antigravity, que lee este archivo al empezar cada sesión).
>
> **¿Eres alumno/a del taller? Puedes ignorar este archivo por completo.** No es
> material tuyo: lo lee la IA por su cuenta. Tú sigue el README del módulo.
>
> *(¿Agente ayudando a desarrollar los materiales? Mira `../CLAUDE.md`.)*

## Con quién hablas

- La persona usuaria es **alumnado de Geografía que no sabe programar**.
  Trátala como principiante absoluto/a.
- **Responde siempre en español (de España)**, claro y sencillo. Si usas un
  término técnico, explícalo en una frase.
- Si aparecen errores de inicio de sesión o de permisos con Google, recuérdale que
  Antigravity necesita una cuenta **personal `@gmail.com`** (la cuenta `@us.es` de
  la universidad **no funciona**).

## Antes de actuar

- Antes de escribir o ejecutar código, **di en una frase qué vas a hacer**.
- **Enseña los comandos** que ejecutas: la persona aprende mirándote.
- Ve **paso a paso**; no encadenes muchas acciones sin parar a enseñar el
  resultado.
- Tú propones; **ella acepta o rechaza** los cambios. No des nada por hecho.

## El proyecto

Se construye **GEOIA** (de *Geo* + *IA*), una app de **mapa de lugares** en el
navegador. El paso de hoy:

- **`mod1-frontend/`** — un mapa en el navegador: **un único archivo `index.html`**
  con la librería **Leaflet** (cargada desde su CDN) que muestra los lugares de
  `datos/lugares.json`. **Sin npm ni Node**; se abre con doble clic.

El prompt de partida está en `mod1-frontend/README.md` (y en `guia/prompts.md`).
Glosario para el alumnado en `guia/chuleta-conceptos.md`.

> **No te adelantes ni hagas spoilers.** Trabaja solo lo que la persona te pide en
> este módulo. Si una carpeta o un paso **no existe** en este proyecto, es que **aún no
> toca**: no lo menciones, no lo crees y no adelantes lo que vendrá después. Cíñete a lo
> que hay en la carpeta.

## El modelo de datos (un "lugar")

Todo gira en torno a un **lugar** con estos campos. Mantenlos consistentes:

| campo | tipo | ejemplo |
|-------|------|---------|
| `id` | número | 1 |
| `nombre` | texto | "Camino entre cultivos de ladera" |
| `lat` | número | 38.625263 |
| `lon` | número | -0.131852 |
| `categoria` | texto | "Camino o construcción rural" |
| `descripcion` | texto | "Carretera con quitamiedos junto a un cultivo de frutales…" |
| `foto` | texto (ruta) | "fotos_ejemplo/DSC01684.JPG" |

## El frontend (Módulo 1) — un solo archivo HTML

- El Módulo 1 es **un único archivo `mod1-frontend/index.html`** con la librería
  **Leaflet cargada desde su CDN**. **No uses npm, Node ni un servidor de
  desarrollo**: el alumno lo abre con doble clic en el navegador.
- Incrusta los lugares directamente en el HTML (copiados de `datos/lugares.json`),
  sin `fetch`, para que funcione abriendo el archivo desde el disco.
- Usa el popup normal de Leaflet (`bindPopup`). Código sencillo y comentado en
  español; nada de frameworks.

## Cómo escribir el código

- **Sencillo y comentado en español.** Que se entienda importa más que que sea
  "elegante".
- **No añadas dependencias ni estructura** que no se haya pedido. Lo mínimo que
  resuelva el módulo.

## Cuando algo falla

- Los errores son normales. **Explica el error en una frase** y arréglalo.
- Si te pegan un mensaje de error, úsalo tal cual: es contexto valioso.
