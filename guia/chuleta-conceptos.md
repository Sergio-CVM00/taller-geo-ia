# Chuleta del taller — para llevar

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

- **GEOIA:** la app que construyes en el taller — un **mapa de lugares** (de *Geo* + *IA*).
- **Frontend / "la cara":** la parte que se ve en el navegador. Aquí, el **mapa** de GEOIA.
- **Backend / servidor:** la parte que no se ve y hace el trabajo. Como un
  **camarero** que espera peticiones y responde.
- **API:** el **menú** del camarero: la lista de cosas que puedes pedirle (p. ej.
  "dame los lugares", "guarda este lugar").
- **Base de datos (SQLite):** la **memoria que no se borra**. Un archivo donde los
  datos se guardan de verdad y siguen ahí aunque apagues el programa.
- **localhost:** **tu propio ordenador**. Una dirección como `http://localhost:8722`
  es una página que vive en tu máquina, no en internet.
- **/docs:** una página de **pruebas** que el servidor crea solo; un formulario
  naranja para probar la API **sin escribir código**.
- **JSON:** una forma sencilla de guardar datos en texto (lo que hay en
  `lugares.json`). No tienes que editarlo.
- **Leaflet:** la librería (un trozo de programa ya hecho) que **dibuja el mapa**.
- **Carpeta del taller:** la carpeta `taller-geo-ia` que descargaste.

## Palabras de los Módulos 2 y 3 (Python)

No tienes que saber usarlas: **el agente las maneja por ti**. Solo para que no te
asusten si aparecen:

- **uv:** el programa que prepara Python para el proyecto. El agente lo usa por ti.
- **Entorno virtual (`.venv`):** una "cajita" aislada de Python para este proyecto, así
  no toca el resto de tu ordenador. El agente la crea sola.
- **uvicorn:** el programa que **arranca el servidor**. El agente lo lanza por ti.
- **FastAPI / Pydantic:** piezas de Python para montar la API. Si salen en un error,
  **pégaselo al agente**: él lo arregla.
- **CDN:** un sitio de internet desde donde se carga una librería ya hecha (por eso el
  mapa del Módulo 1 necesita wifi).
- **ngrok (enlace temporal):** una herramienta que el agente instala y usa para darte
  un **enlace** con el que tu app se ve **desde internet** un rato (para enseñársela a
  un compañero). Es temporal: se apaga cuando lo cierras. Lo tienes paso a paso en
  [`compartir-tu-app.md`](compartir-tu-app.md).

## Dos hábitos que valen oro

- **Pega el error entero al agente.** Si algo falla, copia el mensaje completo y
  pégaselo: **pegar el error es darle contexto**, y con contexto lo arregla.
- **Tarea nueva → chat nuevo.** Al empezar otro módulo, abre un **chat nuevo** en
  Antigravity: el agente arranca despejado y se centra en lo nuevo.

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
| Dice algo de **CORS** | Es un bloqueo de seguridad rutinario; dile *"arréglalo en la API"*. No es culpa tuya. |
| El **servidor no arranca** | Pega el error; suele faltar instalar algo: dile *"prepáralo con uv pip install"*. |
| **No puedes entrar** en Antigravity | Usa una cuenta **`@gmail.com` personal**, no la `@us.es`. |

> El límite ya no es saber programar; es lo que te atrevas a imaginar.
> **Imagínalo → pídeselo → inténtalo.**
