# 🗒️ Todos los prompts del taller

Los prompts listos para copiar y pegar, en un solo sitio. Cada uno está también en la
guía de su módulo, con los pasos y cómo saber que va bien.

> Recuerda: **tarea nueva → chat nuevo**. Y si algo falla, **pega el error entero** al
> agente. ¿Una palabra rara? Mira la [chuleta](chuleta-conceptos.md).
>
> 🙌 **No hace falta entender los prompts**: cópialos tal cual y pégaselos al agente.
> Las palabras técnicas (`uvicorn`, `Path`, `SQLite`…) son cosa suya, no tuya.

---

## Día 1 · Módulo 1 — El mapa (`mod1-frontend/`)

> Un único `index.html` con Leaflet (CDN) que abres con doble clic. Necesitas wifi.

```text
Eres un desarrollador web que me ayuda paso a paso. No sé programar, así que hazlo
tú y explícame en español qué haces en cada paso. (PAPEL)

Estoy en la carpeta "taller-geo-ia". En "datos/lugares.json" hay 18 lugares con
estos campos: id, nombre, lat, lon, categoria, descripcion, foto. Algunos puntos
comparten coordenadas, así que verás marcadores apilados: es normal. (CONTEXTO)

Quiero un único archivo "mod1-frontend/index.html" que muestre un mapa interactivo
con un marcador por cada lugar. Al pulsar un marcador, usa el popup normal de Leaflet
(bindPopup) para mostrar su nombre y su descripción. (TAREA)

El archivo debe: cargar la librería Leaflet 1.9.4 desde su CDN (sin npm ni Node);
llevar los 18 lugares escritos directamente dentro del HTML como una lista de
JavaScript (sin fetch), copiados de datos/lugares.json; centrar el mapa en
lat 38.65, lon -0.10, zoom 12; y funcionar abriendo el archivo con doble clic, sin
servidor. (FORMATO)

Hazlo lo más simple posible: sin frameworks, comentado en español. No abras ningún
servidor ni añadas cosas que no haya pedido. Al final dime qué archivo abrir. (LÍMITES)
```

---

## Día 2 · Módulo 2 — El servidor (`mod2-backend/`)

> La API en memoria (camarero + menú). Lo enseña el presentador; puedes seguirlo.

```text
Eres un desarrollador backend que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Estoy en "taller-geo-ia". En "datos/lugares.json" hay lugares con los campos: id,
nombre, lat, lon, categoria, descripcion, foto. (CONTEXTO)

Quiero un archivo "mod2-backend/main.py" que: (1) al arrancar, cargue los lugares de
"datos/lugares.json" en una lista en memoria (usa la ruta
Path(__file__).parent.parent / "datos" / "lugares.json"); (2) los devuelva en
GET /lugares; y (3) permita añadir uno nuevo con POST /lugares. (TAREA)

Usa el entorno virtual del proyecto (si no existe, créalo con uv venv). Para instalar
usa siempre "uv pip install fastapi uvicorn" (nunca .venv/bin/pip). Arráncalo con
".venv/bin/uvicorn mod2-backend.main:app --port 8722" desde la carpeta "taller-geo-ia",
en un terminal normal (no en segundo plano), y dime cómo abrir la página de pruebas
/docs. (FORMATO)

Un solo archivo, sin subcarpetas, comentado en español, solo fastapi y uvicorn, paso
a paso enseñándome los comandos. (LÍMITES)
```

---

## Día 2 · Módulo 3 — La memoria (`mod3-base-de-datos/`)

> La API con base de datos SQLite: los lugares persisten al reiniciar.

```text
Eres un desarrollador que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Estoy en "taller-geo-ia". En "datos/lugares.json" hay lugares con los campos: id,
nombre, lat, lon, categoria, descripcion, foto. (CONTEXTO)

Quiero un archivo "mod3-base-de-datos/main.py" que:
(1) al arrancar, cree una base de datos SQLite "lugares.db" en la misma carpeta que
main.py (usa Path(__file__).parent / "lugares.db");
(2) si la tabla "lugares" no existe, la cree y la cargue con los 18 registros de
datos/lugares.json (Path(__file__).parent.parent / "datos" / "lugares.json"); si la
tabla ya tiene datos, NO inserte nada (para no duplicar al reiniciar);
(3) GET /lugares devuelva todos los registros;
(4) POST /lugares reciba un lugar en JSON (acéptalo con await request.json(), sin
clase Pydantic) y lo guarde. (TAREA)

Usa el entorno virtual (si no existe, créalo con uv venv). Para instalar usa
"uv pip install fastapi uvicorn". Arráncalo con
".venv/bin/uvicorn mod3-base-de-datos.main:app --port 8731" desde "taller-geo-ia",
en un terminal normal. Usa sqlite3, que ya viene con Python: no instales nada más
para la base de datos. (FORMATO)

Un solo main.py, sin subcarpetas, comentado en español, paso a paso. (LÍMITES)
```

---

## Día 2 · Comparte tu app (`guia/compartir-tu-app.md`)

> El broche final: un **enlace temporal** para que otra persona abra tu app desde su
> móvil u ordenador. Cambia el puerto (`8722`) si el tuyo es otro.

```text
Eres un desarrollador que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Acabo de construir una app en la carpeta "taller-geo-ia" y la tengo funcionando en mi
ordenador, en una dirección como http://localhost:8722. Quiero enseñársela a un
compañero desde SU móvil u ordenador, durante un rato. (CONTEXTO)

Dame un enlace público y temporal que abra mi app desde internet, usando ngrok. (TAREA)

Instala y configura ngrok tú mismo, enseñándome cada comando. Si ngrok necesita una
cuenta gratuita o un token de autenticación, guíame para conseguirlo paso a paso. Deja
encendido el servidor de mi app y arranca ngrok en OTRO terminal, apuntando al puerto
de mi app. (FORMATO)

Al terminar, dame el enlace para copiar y pegar. Recuérdame en una frase que es
temporal: deja de funcionar cuando lo cierre o apague el ordenador. (LÍMITES)
```

---

## Preparación del entorno (opcional, en casa)

> Solo para dejar Python listo antes del taller. El Módulo 1 no necesita nada de esto.

```text
Eres un asistente que me prepara el entorno para un taller. No sé programar, así que
hazlo tú y explícamelo en pasos sencillos.
Comprueba si tengo instalados uv y Python (para los módulos 2 y 3). Lo que falte,
instálalo tú, paso a paso, enseñándome los comandos. Al terminar, dime en una frase
si está todo listo o qué ha fallado.
```
