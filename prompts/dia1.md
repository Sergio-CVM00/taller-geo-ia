# Día 1 — El mapa 🗺️

**Todo lo del Día 1 en un sitio:** el prompt para construir el mapa, dónde se crea el
archivo, cómo saber que va bien y los retos para subir el nivel.

> **No escribes código.** Le describes en español al agente lo que quieres y él lo
> programa. Tú **diriges, miras y decides.** *Imagínalo → pídeselo → inténtalo.*

**Qué vas a conseguir:** la **cara visible de GEOIA** — una página web con un **mapa
interactivo** que muestra los **18 lugares** de la Marina Baja (Alicante) como
marcadores; pulsas uno y ves su **nombre** y su **descripción**. Es **un solo
archivo** (`index.html`) que abres con **doble clic**, sin instalar nada.

**Dónde se crea:** tu archivo va en **`modulo-1-mapa/index.html`**.

---

## 0. Calentamiento (opcional, si es tu primera vez)

¿Nunca has usado un agente? Píerdele el miedo con una página tonta antes del mapa.
Copia esto, pégalo en el agente y juega un par de minutos pidiéndole cambios.

```text
Eres un desarrollador web que me ayuda paso a paso. No sé programar, así que hazlo
tú y explícame en español qué haces en cada paso. (PAPEL)

Es la primera vez que uso un agente de IA para crear algo; quiero perderle el miedo
con una página sencilla. (CONTEXTO)

Hazme una página web (un solo archivo HTML) con mi nombre bien grande y un botón que,
al pulsarlo, cambie el color de fondo de la página. (TAREA)

Un solo archivo que pueda abrir con doble clic, sin instalar nada, comentado en
español. (FORMATO)

Hazlo lo más simple posible. Cuando termines, dime qué archivo abrir; luego te pediré
algún cambio para practicar. (LÍMITES)
```

---

## 1. El prompt del mapa (cópialo y pégalo)

Fíjate en sus **5 ingredientes**: **Papel · Contexto · Tarea · Formato · Límites**.

```text
Eres un desarrollador web que me ayuda paso a paso. No sé programar, así que hazlo
tú y explícame en español qué haces en cada paso. (PAPEL)

Estoy en la carpeta "taller-geo-ia". En "datos/lugares.json" hay 18 lugares con
estos campos: id, nombre, lat, lon, categoria, descripcion, foto. Algunos puntos
comparten coordenadas, así que verás marcadores apilados: es normal. (CONTEXTO)

Quiero un único archivo "modulo-1-mapa/index.html" que muestre un mapa interactivo
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

---

## 2. Cómo saber que va bien

1. El agente crea **`modulo-1-mapa/index.html`**. Lo abres con **doble clic** y se ve
   un **mapa**.
2. Se ven **18 marcadores** en la **Marina Baja (Alicante)**, alrededor de lat 38.6,
   lon -0.1. (Algunos quedan uno encima de otro: es normal.)
3. Al pulsar un marcador aparece el **nombre** y la **descripción**.

---

## 3. Si algo falla

Es normal. **Copia el mensaje de error entero y pégaselo al agente**: pegar el error
es darle contexto, y con contexto lo arregla.

| Lo que ves | Qué hacer |
|---|---|
| Los **puntos salen en el mar** o en otro continente | Coordenadas mal leídas: díselo — *"los puntos salen en el mar, revísalo"*. |
| El **mapa sale en blanco** | Casi siempre es la **wifi** (Leaflet viene de internet): comprueba la conexión y díselo. |
| El mapa sigue en blanco con buena wifi | El agente pudo poner un "candado de seguridad" (atributo `integrity`/SRI) en las etiquetas de Leaflet con un valor que no cuadra, y el navegador bloquea la librería sin avisar. Díselo así para que lo revise o lo quite. |
| El mapa se ve pero **no aparecen los marcadores** (o salen como cuadritos rotos) | Díselo tal cual: *"el mapa se ve pero no aparecen los marcadores"*. |
| Un **error** en rojo | Cópialo entero y pégaselo al agente. |

---

## 4. Los retos — súbele el nivel 🚀

Cuando el mapa funcione, pídele mejoras **de una en una** (en el mismo chat; si se
empieza a liar, abre uno nuevo). **No necesitas saber cómo se hace: descríbelo en
español y deja que el agente lo monte.** Sube por la escalera tanto como te apetezca:
**no son obligatorios.**

### Nivel 1
- **A.** *"Pon un color distinto a los marcadores según su categoría."*
- **B.** *"Muestra la foto del lugar dentro del popup, debajo del nombre."*
  > Ojo con las carpetas: las fotos están en `fotos_ejemplo/`, que está **fuera** de
  > `modulo-1-mapa/`. Si la foto sale rota, dile que las imágenes están una carpeta por
  > encima del `index.html` y que ajuste la ruta para que las encuentre.
- **C.** *"Ajusta el zoom automáticamente para que se vean todos los puntos al abrir."*
  > Va bien cuando, al abrir, **todos** los marcadores quepan en pantalla sin alejar el
  > zoom. El encuadre debe salir de los propios datos; si más adelante añades un lugar
  > lejano (reto del formulario) y se sale, pídele que lo recalcule.

### Nivel 2
- **A.** *"Añade una cajita para buscar lugares por nombre y que filtre el mapa."*
- **B.** *"Pon botones para mostrar solo una categoría (olivares, bancales…)."*
- **C.** *"Haz una lista de lugares al lado; al pulsar uno, que el mapa vaya volando a él."*
  > Va bien cuando, al pulsar un nombre de la lista, el mapa se desplaza al punto y se
  > abre su popup ahí. Si el popup sale descolocado o parpadea, díselo: suele bastar con
  > que espere a que termine el desplazamiento antes de abrirlo.

### Nivel 3
- **A.** *"Deja marcar lugares como favoritos y que se recuerden aunque cierre la página."*
  > Trampa típica: la estrella funciona la primera vez, pero al volver a pulsarla ya no
  > hace nada (hasta que cierras y reabres el popup). Si te pasa, díselo con esas
  > palabras —*"la estrella solo funciona una vez por apertura del popup"*— para que
  > vuelva a dejar activo el botón cada vez que cambia el popup.
- **B.** *"Quiero un formulario para añadir un lugar nuevo escribiendo su nombre y coordenadas."*
  > Si ya tienes búsqueda o filtros, al añadir un lugar puede parecer que "no aparece"
  > porque el filtro lo esconde. Pídele que, al añadir, el mapa y la lista queden
  > **coherentes** (que quite los filtros, o que el lugar nuevo respete el filtro activo).
- **C.** *"Añade un botón para cambiar entre modo claro y oscuro."*
  > Dos cosas que se olvidan: el mapa de fondo (las imágenes del terreno) **no se
  > oscurece solo** al cambiar los colores de la página, así que pide que también lo
  > atenúe en modo oscuro; y, como con los favoritos, pide que **recuerde el modo
  > elegido** al recargar.

> **Antes de dar un reto por bueno, pruébalo de verdad:** el caso normal y un caso
> límite (borra la búsqueda, recarga la página, pulsa dos veces). Los retos se
> **acumulan** sobre el mismo `index.html`, así que comprueba que los anteriores siguen
> funcionando. ¿No sabes cómo comprobar uno? Pídeselo al agente: *"enséñame cómo probar
> este cambio"*.

### ¿Te atascas en un reto?
Tienes un **prompt de solución para cada reto** (A, B y C de los tres niveles) en
**[`retos/`](retos/)** — uno por archivo, con su módulo, nivel y letra
(`mod1-nivel1-A.txt`…). Y un mapa de ejemplo con los **9 retos ya hechos** en
**[`../ejemplo-terminado/`](../ejemplo-terminado/)**. Míralos **cuando ya lo hayas
intentado tú**: son la red de seguridad, no el atajo.

---

## El puente al Día 2

¿Probaste a **añadir un lugar** con el formulario? Recargas la página… y ya no está.
Para que tus datos se **queden de verdad** hace falta un **servidor** y una **base de
datos**. Eso es lo del Día 2 → **[`dia2.md`](dia2.md)**.

> El límite ya no es saber programar; es lo que te atrevas a imaginar.
