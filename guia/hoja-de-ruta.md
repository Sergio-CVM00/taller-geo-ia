# Hoja de ruta del taller — lo que vas a construir

Esto es el **mapa del viaje**: qué construyes en cada paso, **para qué sirve** y
**cómo sabrás que va bien**. No es la solución (eso lo montas tú con el agente), son
las **metas** — para que las tengas a mano sin depender de la presentación.

> Recuerda la idea de siempre: **tú no escribes código.** Le describes en español al
> agente lo que quieres y él lo programa. Tú **diriges, miras y decides.**
> **Imagínalo → pídeselo → inténtalo.**

Cada módulo tiene una **escalera de retos** en tres niveles —
**Para coger confianza · Interacción de verdad · Atrévete**— con tres tareas (A, B, C)
cada uno. **No son obligatorios:** subes lo que te apetezca, de una mejora en una.
Los prompts listos para copiar están en **[`prompts/`](../prompts/)**.

---

## GEOIA, de un vistazo

**GEOIA** (de *Geo* + *IA*) es una **app web de verdad** que vas montando por piezas:
primero la cara que se ve, luego el motor que la sirve y, por último, la memoria que
no se borra. Al final, la compartes con un enlace.

| Pieza | Qué es | Quién la monta |
|---|---|---|
| **Módulo 1 · El mapa** | La **cara visible**: un mapa con los lugares. | Tú (Día 1) |
| **Módulo 2 · El servidor** | El **camarero** que sirve los datos. | Demo del presentador (puedes seguirlo) |
| **Módulo 3 · La memoria** | La **base de datos** que lo recuerda todo. | Tú (Día 2) |
| **Broche final · Compartir** | Un **enlace** para abrir tu app desde otro móvil. | Tú, guiado por el agente |

---

## Día 1 — Módulo 1 · El mapa

**Qué es:** la **cara visible** de GEOIA — una página web con un **mapa interactivo**
que muestra los **18 lugares** como marcadores; pulsas uno y ves su nombre y su
descripción. Es **un solo archivo** (`index.html`) que abres con **doble clic**, sin
instalar nada.

**Tu meta de partida:** que aparezca `modulo-1-mapa/index.html`, lo abras y veas un
mapa con **18 marcadores** en la **Marina Baja (Alicante)**; al pulsar uno, salen su
**nombre** y su **descripción**. La guía con el prompt listo está en
**[`modulo-1-mapa/`](../modulo-1-mapa/README.md)**.

**La escalera de retos**

| Nivel | A | B | C |
|---|---|---|---|
| Para coger confianza | Color distinto por categoría | Foto del lugar en el popup | Ajustar el zoom para ver todos los puntos |
| Interacción de verdad | Buscador por nombre que filtra el mapa | Botones para mostrar solo una categoría | Lista al lado; al pulsar, el mapa vuela ahí |
| Atrévete | Favoritos que se recuerdan al cerrar la página | Formulario para añadir un lugar nuevo | Botón de modo claro/oscuro |

> ¿Te atascaste en algún reto? Hay un prompt de ayuda por cada uno en
> **[`prompts/soluciones/`](../prompts/soluciones/)**, y un mapa de ejemplo con los 9
> retos ya hechos en **[`ejemplo-terminado/`](../ejemplo-terminado/)**. Míralos **cuando ya lo hayas
> intentado tú**: son la red de seguridad, no el atajo.

**El puente al Día 2:** ¿probaste a **añadir un lugar** con el formulario? Recargas la
página… y ya no está. Para que tus datos se **queden de verdad** hace falta un
**servidor** y una **base de datos**. Eso es lo de mañana.

---

## Día 2 — Por dentro: servidor, memoria y compartir

> Empieza el Día 2 **descargando la versión nueva** del repositorio y trayendo tu
> trabajo de ayer. Y el hábito de oro: **tarea nueva → chat nuevo**, con la cabeza
> despejada.

### Módulo 2 · El servidor  ·  *demo del presentador (puedes seguirlo)*

**Qué es:** un **servidor** es como un **camarero**: espera peticiones y responde; la
**API** es su **menú**. Montas un camarero pequeño en **Python** que **sirve** la lista
de lugares y deja **añadir** nuevos. Es la parte que **no se ve**; se prueba en una
página automática (**`/docs`**), sin escribir código.

**Tu meta de partida:** el agente te da una dirección como `http://localhost:8722`; le
añades `/docs` y aparece un formulario con `GET /lugares` (devuelve los **18**) y
`POST /lugares` (tras añadir uno, hay **19**). Si paras el servidor, los nuevos se
pierden: es "en memoria" — eso lo arregla el Módulo 3.

**La escalera de retos**

| Nivel | A | B | C |
|---|---|---|---|
| Para coger confianza | Pedir un lugar por su id (`GET /lugares/{id}`) | Un endpoint `/salud` que diga que el servidor está vivo | Cambiar el título y la descripción de `/docs` |
| Interacción de verdad | Filtrar por categoría (`/lugares?categoria=Olivar`) | Búsqueda por texto en nombre y descripción | Borrar un lugar (`DELETE /lugares/{id}`) |
| Atrévete | Servir tu mapa en `http://localhost:8722/` | Lista de categorías con su recuento | Conectar el mapa para que pida los lugares a la API |

### Módulo 3 · La memoria  ·  *lo construyes tú*

**Qué es:** una **base de datos** es la **memoria que no se borra**: un archivo donde
los lugares se guardan **de verdad**, así que **apagas y enciendes** el servidor y
**siguen ahí**. Usas **SQLite**, que ya viene con Python.

**Tu meta de partida:** aparece el archivo `lugares.db` y en `/docs` el `GET /lugares`
da los **18**. **El momento clave:** haces un `POST` con un lugar nuevo, **paras y
arrancas** el servidor, vuelves a pedir `GET /lugares`… y **tu lugar sigue ahí**.

**La escalera de retos** *(el último es el broche final del taller)*

| Nivel | A | B | C |
|---|---|---|---|
| Para coger confianza | Borrar un lugar | Editar un lugar | Ver un lugar por su id |
| Interacción de verdad | Filtrar por categoría (`/lugares?categoria=Olivar`) | Búsqueda por texto | Ordenar los lugares por nombre |
| Atrévete | Servir tu mapa leyendo de la base de datos (**¡la app entera!**) | Guardar la fecha en que añadiste cada lugar | **Compartir tu app con un enlace (ngrok)** |

### Broche final · Comparte tu app (ngrok)  ·  *dirigido por el agente*

**La idea:** conseguir un **enlace temporal** para que otra persona abra tu app desde
**su móvil**. El agente se encarga de todo; tú solo: **inicia sesión → pega el token →
pruébalo**. Es un enlace **temporal**: deja de funcionar cuando lo cierras.

---

## El cierre

Habrás construido una **app web completa hablando en español**: mapa, servidor y
memoria, y la habrás **compartido** con alguien.

> El límite ya no es saber programar; es lo que te atrevas a imaginar.
> **Imagínalo → pídeselo → inténtalo.**
