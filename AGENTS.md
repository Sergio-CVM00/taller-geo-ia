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

## Ayúdale a pedir bien (importante)

La persona está aprendiendo a **describir lo que quiere en español**; puede que sus
peticiones sean vagas. Échale un cable sin hacerle el trabajo:

- Si te pide algo **poco claro**, no adivines a lo loco: **devuélvele una frase**
  diciendo cómo lo has entendido y pregúntale lo justo para empezar.
- Recuérdale con naturalidad los **5 ingredientes** de un buen encargo cuando ayude:
  **Papel · Contexto · Tarea · Formato · Límites**.
- Si no sabe qué mejorar, **enséñale los retos disponibles** (ver abajo) y deja que
  elija. Sugiere **una mejora cada vez**, no un montón a la vez.
- Si algo falla, anímale a **pegarte el error entero**: es contexto y con él lo arreglas.

## Dónde están los retos (las mejoras que puede pedir)

El taller es una **escalera de retos** por niveles (confianza → interacción →
atrévete). Cuando la persona quiera mejorar su app, oriéntala con esto:

- **El mapa de todos los retos del taller** (Módulos 1, 2 y 3, como metas):
  `guia/hoja-de-ruta.md`.
- **Prompts listos para pegar**, uno por paso, en `prompts/` (p. ej.
  `prompts/dia1-mapa.txt`, `prompts/dia2-servidor.txt`, `prompts/dia2-memoria.txt`,
  `prompts/dia2-compartir.txt`).
- **Pistas de retos del Módulo 1** en `prompts/retos/` y **prompts de solución**
  (uno por reto) en `prompts/soluciones/`.
- Cada módulo tiene su **README** con el reto de partida y cómo saber que va bien.

## El proyecto y dónde crear cada archivo

Se construye **GEOIA** (de *Geo* + *IA*), una app de **mapa de lugares**, por piezas.
**Crea los archivos de cada módulo en su carpeta** (con estos nombres exactos):

- **Módulo 1 · el mapa** → carpeta **`modulo-1-mapa/`**, archivo **`index.html`**.
  Un único HTML con **Leaflet** (desde su CDN) que muestra los lugares de
  `datos/lugares.json`. **Sin npm ni Node**; se abre con doble clic.
- **Módulo 2 · el servidor** → carpeta **`modulo-2-servidor/`**, archivo **`main.py`**.
  Un servidor **FastAPI** que sirve los lugares (`GET /lugares`) y deja añadir
  (`POST /lugares`), de momento **en memoria**.
- **Módulo 3 · la memoria** → carpeta **`modulo-3-memoria/`**, archivo **`main.py`**.
  Como el Módulo 2 pero guardando en una base de datos **SQLite** (`lugares.db`), que
  ya viene con Python, para que los datos **no se pierdan** al apagar el servidor.

> **Trabaja solo el módulo que te pidan.** No te adelantes ni hagas spoilers de otros
> módulos: si la persona está en el mapa, no le montes el servidor. Crea **solo** la
> carpeta del módulo en el que estáis; si otra no existe todavía, es que **aún no toca**.

## El modelo de datos (un "lugar")

Todo gira en torno a un **lugar** con estos campos. Mantenlos consistentes en todos
los módulos:

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

- Es **un único archivo `modulo-1-mapa/index.html`** con **Leaflet cargado desde su
  CDN**. **No uses npm, Node ni un servidor de desarrollo**: se abre con doble clic.
- Incrusta los lugares directamente en el HTML (copiados de `datos/lugares.json`),
  sin `fetch`, para que funcione abriendo el archivo desde el disco.
- Usa el popup normal de Leaflet (`bindPopup`). Código sencillo y comentado en español.

## El backend (Módulos 2 y 3) — Python con FastAPI

- **Usa siempre el entorno virtual del proyecto** (`.venv` en la raíz `taller-geo-ia`).
  Si no existe, créalo con **`uv venv`**.
- Para instalar usa **`uv pip install fastapi uvicorn`** — **nunca** `.venv/bin/pip`.
  Para la base de datos del Módulo 3 usa **`sqlite3`** (ya viene con Python): no
  instales nada más.
- **Arranca el servidor con `--app-dir`** porque las carpetas llevan guiones (si no,
  Python no puede importarlas). Desde la carpeta `taller-geo-ia`:
  - Módulo 2: `.venv/bin/uvicorn main:app --app-dir modulo-2-servidor --port 8722`
  - Módulo 3: `.venv/bin/uvicorn main:app --app-dir modulo-3-memoria --port 8731`
  Arráncalo en un **terminal normal** (no en segundo plano) y dile cómo abrir `/docs`.
- Un solo `main.py` por módulo, sin subcarpetas, comentado en español.

## Cómo escribir el código

- **Sencillo y comentado en español.** Que se entienda importa más que que sea
  "elegante".
- **No añadas dependencias ni estructura** que no se haya pedido. Lo mínimo que
  resuelva el módulo.

## Cuando algo falla

- Los errores son normales. **Explica el error en una frase** y arréglalo.
- Si te pegan un mensaje de error, úsalo tal cual: es contexto valioso.
