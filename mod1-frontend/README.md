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
> internet): comprueba la conexión y díselo al agente. Si la wifi va bien y sigue en
> blanco, hay otra causa frecuente: que el agente haya puesto un "candado de seguridad"
> (un atributo `integrity`/SRI) en las etiquetas de Leaflet con un valor que no cuadra,
> y el navegador bloquee la librería sin avisar. Díselo así para que lo revise o lo quite.
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
  > Ojo con las carpetas: las fotos están en `fotos_ejemplo/`, que está **fuera** de
  > `mod1-frontend/`. Si la foto sale rota, dile al agente que las imágenes están una
  > carpeta por encima del `index.html` y que ajuste la ruta para que las encuentre.
- **C.** *"Ajusta el zoom automáticamente para que se vean todos los puntos al abrir."*
  > Sabrás que va bien cuando, al abrir, **todos** los marcadores quepan en pantalla sin
  > tener que alejar el zoom. El encuadre debe salir de los propios datos; si más adelante
  > añades un lugar lejano (reto del formulario) y se sale, pídele que lo recalcule.

**Nivel 2 · Interacción de verdad**
- **A.** *"Añade una cajita para buscar lugares por nombre y que filtre el mapa."*
- **B.** *"Pon botones para mostrar solo una categoría (olivares, bancales…)."*
- **C.** *"Haz una lista de lugares al lado; al pulsar uno, que el mapa vaya volando a él."*
  > Sabrás que va bien cuando, al pulsar un nombre de la lista, el mapa se desplace hasta
  > el punto y se abra su popup ahí. Si el popup sale descolocado o parpadea, díselo: suele
  > bastar con que espere a que termine el desplazamiento antes de abrirlo.

**Nivel 3 · Atrévete**
- **A.** *"Deja marcar lugares como favoritos y que se recuerden aunque cierre la página."*
  > Trampa típica: la estrella funciona la primera vez, pero al volver a pulsarla ya no hace
  > nada (hasta que cierras y reabres el popup). Si te pasa, díselo con esas palabras —*"la
  > estrella solo funciona una vez por apertura del popup"*— para que vuelva a dejar activo
  > el botón cada vez que cambia el popup.
- **B.** *"Quiero un formulario para añadir un lugar nuevo escribiendo su nombre y coordenadas."*
  > Si ya tienes búsqueda o filtros, al añadir un lugar puede parecer que "no aparece" porque
  > el filtro lo esconde. Pídele que, al añadir, el mapa y la lista queden **coherentes** (por
  > ejemplo, que quite los filtros o que el lugar nuevo respete el filtro activo).
- **C.** *"Añade un botón para cambiar entre modo claro y oscuro."*
  > Dos cosas que se suelen olvidar aquí: el mapa de fondo (las imágenes del terreno) **no se
  > oscurece solo** al cambiar los colores de la página, así que pide que también lo atenúe en
  > modo oscuro; y, como con los favoritos, pide que **recuerde el modo elegido** al recargar.

> Los retos **no son obligatorios**: elige los que te hagan ilusión. Y si uno se
> resiste, ya sabes — **copia el error y pégaselo al agente**.

> **Antes de dar un reto por bueno, pruébalo de verdad:** el caso normal y un caso límite
> (borra la búsqueda, recarga la página, pulsa dos veces). Estos retos se acumulan sobre el
> mismo `index.html`, así que comprueba que los anteriores siguen funcionando. ¿No sabes cómo
> comprobar uno? Pídeselo al agente: *"enséñame cómo probar este cambio"*.

> **Puente al Día 2:** ¿probaste a *añadir un lugar nuevo*? Recarga la página… ya no
> está. Para que tus datos se queden de verdad (y los pueda ver más gente) necesitas un
> **servidor** y una **base de datos**: es justo lo que montas en los **Módulos 2 y 3**
> —cada uno por su cuenta; si quieres, al final los conectas—.
