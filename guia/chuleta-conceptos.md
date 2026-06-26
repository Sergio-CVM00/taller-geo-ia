# 🧭 Chuleta del taller — para llevar

Una hoja para consultar cuando una palabra te suene rara o algo no salga.
**No hay que memorizar nada.**

## Las ideas clave

- **Vibe coding / "programar hablando":** tú no escribes código; le **dices en
  español** a un agente de IA lo que quieres y él lo escribe y lo ejecuta. Tú
  diriges, miras y decides.
- **Agente (Antigravity):** el asistente de IA que **escribe y ejecuta** por ti. Le
  hablas en su panel de chat.
- **Prompt:** lo que le escribes al agente. Un buen prompt tiene **5 ingredientes**:
  - **Papel** — qué rol toma ("eres un desarrollador que me ayuda paso a paso").
  - **Contexto** — dónde estás y con qué datos ("en datos/lugares.json hay…").
  - **Tarea** — qué quieres ("un mapa con un marcador por cada lugar").
  - **Formato** — cómo lo quieres ("un solo archivo HTML", "coméntalo en español").
  - **Límites** — qué NO hacer ("sin añadir cosas que no haya pedido").

## Las palabras que oirás

- **Frontend / "la cara":** la parte que se ve en el navegador. Aquí, el **mapa**.
- **Marcador:** cada punto del mapa. Al pulsarlo se abre un **popup** con el nombre y
  la descripción del lugar.
- **JSON:** una forma sencilla de guardar datos en texto (lo que hay en
  `lugares.json`). No tienes que editarlo.
- **Leaflet:** la librería (un trozo de programa ya hecho) que **dibuja el mapa**.
- **CDN:** un sitio de internet desde donde se carga una librería ya hecha (por eso el
  mapa necesita wifi).
- **Carpeta del taller:** la carpeta `taller-geo-ia` que descargaste.
- **Cuota:** las peticiones gratis que tienes con el agente. Un buen prompt gasta menos.

## Dos hábitos que valen oro

- 🩹 **Pega el error entero al agente.** Si algo falla, copia el mensaje completo y
  pégaselo: **pegar el error es darle contexto**, y con contexto lo arregla.
- 🧹 **Tarea nueva → chat nuevo.** Al empezar otra cosa, abre un **chat nuevo** en
  Antigravity: el agente arranca despejado (y gastas menos cuota).

## Qué verás al abrir Antigravity

La ventana principal con un **panel de chat** (donde le escribes) y, al cargar la
carpeta `taller-geo-ia`, sus archivos a un lado. Si te pide iniciar sesión, usa tu
cuenta **personal `@gmail.com`** (la `@us.es` no vale).

## Si algo no sale (lo más común)

| Lo que ves | Qué hacer |
|---|---|
| El **mapa sale en blanco** | Casi siempre es la **wifi** (Leaflet viene de internet). Comprueba la conexión y díselo al agente. |
| Los **puntos salen en el mar** | Coordenadas mal leídas: dile *"los puntos salen en el mar, revísalo"*. |
| Sale un **error** en rojo | Cópialo entero y pégaselo al agente. |
| **No puedes entrar** en Antigravity | Usa una cuenta **`@gmail.com` personal**, no la `@us.es`. |

> El límite ya no es saber programar; es lo que te atrevas a imaginar.
> **Imagínalo → pídeselo → inténtalo.**
