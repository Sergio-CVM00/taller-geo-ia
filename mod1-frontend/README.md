# Módulo 1 — El frontend de GEOIA: tu mapa en el navegador
**Día 1 · lo construyes con Antigravity, sin escribir código**

> **Pieza independiente.** Solo usa los datos de
> [`../datos/lugares.json`](../datos/lugares.json). Aunque empieces por aquí, funciona.

## Qué vas a conseguir

La **cara visible de GEOIA**: una **página web con un mapa interactivo** que muestra
los 18 lugares de ejemplo como marcadores. Pulsas un marcador y ves el **nombre** y la
**descripción** del lugar. Es lo que se ve y se toca.

Será **un solo archivo** (`index.html`) que abres con **doble clic** en el navegador.
Sin instalar nada.

> Hoy no buscamos algo perfecto; buscamos **ver tu idea funcionando en pantalla.**

## Antes de empezar

- Tienes Antigravity abierto con la carpeta `taller-geo-ia` (ver
  [`../00-ANTES-DEL-TALLER.md`](../00-ANTES-DEL-TALLER.md)).
- Los datos ya están en [`../datos/lugares.json`](../datos/lugares.json). No tienes
  que crearlos.
- **Necesitas wifi:** el mapa (las imágenes del terreno y la librería que lo
  dibuja) se cargan de internet.

## El prompt de partida (cópialo y pégalo)

Fíjate en sus **5 ingredientes**: **papel · contexto · tarea · formato · límites**.
(¿Alguno te suena a chino? Mira la [chuleta](../guia/chuleta-conceptos.md).)

```text
Eres un desarrollador web que me ayuda paso a paso. No sé programar, así que hazlo
tú y explícame en español qué haces en cada paso. (PAPEL)

Estoy en la carpeta "taller-geo-ia". En "datos/lugares.json" hay 18 lugares con
estos campos: id, nombre, lat, lon, categoria, descripcion, foto. Algunos puntos
comparten coordenadas, así que verás marcadores apilados: es normal. (CONTEXTO)

Quiero un único archivo "mod1-frontend/index.html" que muestre un mapa interactivo
con un marcador por cada lugar. Al pulsar un marcador, usa el popup normal de Leaflet
(bindPopup) para mostrar su nombre y su descripción. (TAREA)

El archivo debe: cargar la librería Leaflet 1.9.4 (su CSS y su JS) desde su CDN (sin npm ni Node);
llevar los 18 lugares escritos directamente dentro del HTML como una lista de
JavaScript (sin fetch), copiados de datos/lugares.json; centrar el mapa en
lat 38.65, lon -0.10, zoom 12; y funcionar abriendo el archivo con doble clic, sin
servidor. (FORMATO)

Hazlo lo más simple posible: sin frameworks, comentado en español. No abras ningún
servidor ni añadas cosas que no haya pedido. Al final dime qué archivo abrir. (LÍMITES)
```

> **Truco:** pensar bien el prompt antes de enviarlo funciona mucho mejor que
> reintentar a ciegas. Un buen prompt vale por diez.

## Cómo saber que va bien

1. El agente crea un archivo **`mod1-frontend/index.html`**. Lo abres con **doble
   clic** y se ve un **mapa**.
2. Se ven **18 marcadores** en la **Marina Baja (Alicante)**, alrededor de lat 38.6,
   lon -0.1. (Algunos quedan uno encima de otro: es normal.)
3. Al pulsar un marcador aparece el **nombre** y la **descripción**.

> Si los puntos salen en el mar o en otro continente, las coordenadas se leyeron
> mal: **díselo al agente** ("los puntos salen en el mar, revísalo").
> Si el mapa sale **en blanco**, casi siempre es la wifi (Leaflet viene de
> internet): comprueba la conexión y díselo al agente.
> Si el mapa se ve pero **no aparecen los marcadores** (o salen como cuadritos
> rotos): **díselo al agente** ("el mapa se ve pero no aparecen los marcadores").

## Si algo falla

Es normal. **Copia el mensaje de error entero y pégaselo al agente**: pegar el error
es darle contexto, y con contexto lo arregla. Por ejemplo: *"Me sale esto, ¿qué pasa?
[pega el error]"*.

## Ahora tú (retos)

Cuando el mapa funcione, pídele mejoras **de una en una** (en el mismo chat; si se
empieza a liar, abre uno nuevo). **No necesitas saber cómo se hace: descríbelo en
español y deja que el agente lo monte.** Sube por la escalera tanto como te apetezca.

> ¿Te atascas en el **reto A** de algún nivel? Tienes un prompt de ejemplo en
> [`../prompts/retos/`](../prompts/retos/) (`mod1-nivel1-confianza-A.txt` … `mod1-nivel3-atrevete-A.txt`). Míralo
> solo si lo necesitas: lo suyo es **describir tú la mejora en español**.

**Nivel 1 · Para coger confianza**
- **A.** *"Pon un color distinto a los marcadores según su categoría."*
- **B.** *"Muestra la foto del lugar dentro del popup, debajo del nombre."*
- **C.** *"Ajusta el zoom automáticamente para que se vean todos los puntos al abrir."*

**Nivel 2 · Interacción de verdad**
- **A.** *"Añade una cajita para buscar lugares por nombre y que filtre el mapa."*
- **B.** *"Pon botones para mostrar solo una categoría (olivares, bancales…)."*
- **C.** *"Haz una lista de lugares al lado; al pulsar uno, que el mapa vaya volando a él."*

**Nivel 3 · Atrévete**
- **A.** *"Deja marcar lugares como favoritos y que se recuerden aunque cierre la página."*
- **B.** *"Quiero un formulario para añadir un lugar nuevo escribiendo su nombre y coordenadas."*
- **C.** *"Añade un botón para cambiar entre modo claro y oscuro."*

> Los retos **no son obligatorios**: elige los que te hagan ilusión. Y si uno se
> resiste, ya sabes — **copia el error y pégaselo al agente**.

> **Puente al Día 2:** ¿probaste a *añadir un lugar nuevo*? Recarga la página… ya no
> está. Para que tus datos se queden de verdad (y los pueda ver más gente) necesitas un
> **servidor** y una **base de datos**: es justo lo que montas en los **Módulos 2 y 3**
> —cada uno por su cuenta; si quieres, al final los conectas—.
