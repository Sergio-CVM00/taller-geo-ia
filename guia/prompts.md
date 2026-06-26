# 🗒️ Los prompts del taller

Los prompts listos para copiar y pegar, en un solo sitio. Cada uno está también en la
guía de su módulo, con los pasos y cómo saber que va bien.

> Recuerda: **tarea nueva → chat nuevo**. Y si algo falla, **pega el error entero** al
> agente. ¿Una palabra rara? Mira la [chuleta](chuleta-conceptos.md).
>
> 🙌 **No hace falta entender los prompts**: cópialos tal cual y pégaselos al agente.

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

> 🔜 **El Día 2** seguiremos en directo y aparecerán más prompts aquí. Hoy, con el del
> mapa te sobra. 🙂
