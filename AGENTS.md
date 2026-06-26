# Reglas del proyecto para el asistente de IA

> **Para quién es esto:** reglas para el asistente de IA (p. ej. Google
> Antigravity, que lee este archivo al empezar cada sesión).
>
> 🙋 **¿Eres alumno/a del taller? Puedes ignorar este archivo por completo.** No es
> material tuyo: lo lee la IA por su cuenta. Tú sigue los README de cada módulo.
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

## El proyecto: GEOIA, una app web en tres módulos

Se construye **GEOIA** (de *Geo* + *IA*), una app de **mapa de lugares**, en tres
módulos **independientes entre sí**:

1. **`mod1-frontend/`** — un mapa en el navegador: **un único archivo `index.html`**
   con la librería **Leaflet** (cargada desde su CDN) que muestra los lugares de
   `datos/lugares.json`. **Sin npm ni Node**; se abre con doble clic.
2. **`mod2-backend/`** — una API con **Python + FastAPI** que entrega y recibe
   lugares.
3. **`mod3-base-de-datos/`** — almacenamiento con **SQLite** para que los lugares
   persistan.

Cada módulo es **autónomo**: parte de `datos/lugares.json`, **no** del resultado de
otro módulo, de modo que se pueda empezar cualquiera desde cero. Respeta el módulo en
el que se está trabajando; no te adelantes a los siguientes salvo que te lo pidan.

## Mapa de pasos: dónde encontrar cada cosa

Para no perderte, este es el orden de los pasos y **dónde vive cada uno**. El prompt de
partida de cada paso está en el `README.md` de su carpeta y, todos juntos, en
`guia/prompts.md`:

1. **Mapa** → `mod1-frontend/README.md` (crea `mod1-frontend/index.html`).
2. **Servidor** → `mod2-backend/README.md` (crea `mod2-backend/main.py`).
3. **Memoria** → `mod3-base-de-datos/README.md` (crea `mod3-base-de-datos/main.py`).
4. **Compartir** → `guia/compartir-tu-app.md` (un enlace temporal para enseñar la app).

Glosario para el alumnado en `guia/chuleta-conceptos.md`.

> ⚠️ **No te adelantes ni hagas spoilers.** Trabaja solo el paso que la persona te pide.
> Si una carpeta o un paso **no existe** en este proyecto, es que **aún no toca**: no lo
> menciones, no lo crees y no adelantes lo que vendrá después. Cíñete a lo que hay.

## El modelo de datos (un "lugar")

Todo el proyecto gira en torno a un **lugar** con estos campos. Mantenlos consistentes
en frontend, backend y base de datos:

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

## Entorno de Python — IMPORTANTE (Módulos 2 y 3)

- El backend usa un entorno virtual **`.venv`** (creado con **uv**) en la raíz de la
  carpeta. **Usa siempre ese `.venv`, nunca el Python global** del sistema.
- Si no existe `.venv`, créalo con `uv venv`. Para instalar librerías usa
  **`uv pip install …`** (p. ej. `uv pip install fastapi uvicorn`); **no** uses
  `.venv/bin/pip`. Las del proyecto están en `requirements.txt` (**fastapi,
  uvicorn**). SQLite ya viene con Python.
- Arranca el servidor con `uvicorn` en un **terminal normal** (no en segundo plano) e
  indícale a la persona la dirección y cómo abrir la página `/docs`.
- En el **Módulo 3**, crea la tabla con `CREATE TABLE IF NOT EXISTS` y siembra los
  datos de `lugares.json` **solo si la tabla está vacía**, para no duplicarlos al
  reiniciar el servidor.

## Compartir la app (paso "Compartir", Día 2)

- El objetivo es que **otra persona abra la app desde su dispositivo**, de la forma más
  sencilla posible. Guíate por `guia/compartir-tu-app.md`.
- Si la app es **solo el mapa** (`mod1`, un `index.html` estático), lo más simple es
  **enviar el archivo** o abrirlo en el proyector; no hace falta servidor ni túnel.
- Si la app tiene **servidor** (`mod2`/`mod3` en `localhost`), dale un **enlace público
  temporal** con **ngrok**. **Instala y configura ngrok tú** (enseñando los comandos);
  si pide cuenta gratuita o token de autenticación, **guía a la persona paso a paso**
  para conseguirlo. Si ngrok no se pudiera usar, esta guía les sirve de referencia.
- **Deja el servidor de la app encendido** y arranca ngrok en **otro terminal**,
  apuntando al puerto de la app. Devuélvele el enlace listo para copiar y **avisa de
  que es temporal** (caduca al cerrarlo o apagar).

## Cómo escribir el código

- **Sencillo y comentado en español.** Que se entienda importa más que que sea
  "elegante".
- **No añadas dependencias ni estructura** que no se haya pedido. Lo mínimo que
  resuelva el módulo.

## Cuando algo falla

- Los errores son normales. **Explica el error en una frase** y arréglalo.
- Si te pegan un mensaje de error, úsalo tal cual: es contexto valioso.
