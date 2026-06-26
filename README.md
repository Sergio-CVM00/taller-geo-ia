# Construye tu primera app web hablando en español 🌍🗺️

**Universidad de Sevilla · Cátedra de IA US-Google · Cactus Accelerative Innovation**
📅 29 y 30 de junio de 2026 · 🕔 17:00 · Facultad de Geografía e Historia

---

## ¿Qué vas a construir? — **GEOIA**

**GEOIA** (de *Geo* + *IA*), una **app web de verdad**: un **mapa interactivo** con
lugares marcados que, poco a poco, aprende a **guardar** los tuyos. Y lo importante:
**no vas a escribir ni una sola línea de código.** Le hablas en español a un asistente
de IA (**Google Antigravity**) y él lo programa por ti. Tú **diriges, miras y decides.**

> El objetivo no es que te conviertas en programador/a. Es que salgas con otra
> cabeza: **si se me ocurre algo, lo puedo prototipar.** El límite ya no es saber
> programar; es lo que te atrevas a imaginar.
> **Imagínalo → pídeselo → inténtalo.**

## El plan, en dos días

Montas **GEOIA** en **tres piezas**, de lo más visible a lo más profundo. Cada una en
su carpeta, con su guía y su prompt listo para pegar:

- 🗺️ **Día 1 — El mapa** (`mod1-frontend/`): la parte que se ve. Un mapa en el
  navegador con los lugares marcados; pulsas uno y ves su nombre y su descripción.
- ⚙️ **Día 2 — El servidor** (`mod2-backend/`): la parte que no se ve pero hace el
  trabajo. Un programita que entrega y recibe lugares (como un camarero que te trae
  lo que le pides).
- 💾 **Día 2 — La memoria** (`mod3-base-de-datos/`): donde los lugares se **guardan
  de verdad** y no se pierden aunque apagues todo.

Y el broche del Día 2: 🌍 **comparte GEOIA** con un enlace temporal para que otra
persona la abra desde su móvil (guía en [`guia/compartir-tu-app.md`](guia/compartir-tu-app.md)).

> 💡 Cada pieza es **independiente**: todas parten de los mismos datos de ejemplo
> (`datos/`). Puedes hacerlas en orden o **saltar a la siguiente** aunque no hayas
> terminado la anterior. No te quedas atascado/a.
>
> *(Por curiosidad: el mapa usa una librería llamada Leaflet; el servidor, Python;
> la memoria, SQLite. No necesitas saber qué son: el agente se encarga.)*

## Cómo empezar (3 pasos)

1. **Antes del taller** → lee y haz **[`00-ANTES-DEL-TALLER.md`](00-ANTES-DEL-TALLER.md)**.
   Son 15–20 minutos y así el primer día arrancas con todo listo. (Si te atascas, no
   pasa nada: abrimos la sala a las 16:30 para echarte una mano.)
2. **En el taller** → abre **Google Antigravity** y carga esta carpeta
   `taller-geo-ia` (arrástrala a la ventana, o usa su botón de abrir/añadir carpeta).
3. **Sigue la guía de cada pieza** → empieza por **[`mod1-frontend/`](mod1-frontend/README.md)**
   el Día 1; sigue con **[`mod2-backend/`](mod2-backend/README.md)** y
   **[`mod3-base-de-datos/`](mod3-base-de-datos/README.md)** el Día 2. Cada guía trae
   el prompt para copiar y pegar.

> 🧭 ¿Te pierde alguna palabra (mapa, servidor, base de datos, prompt…)? Tienes una
> **chuleta** de bolsillo en **[`guia/chuleta-conceptos.md`](guia/chuleta-conceptos.md)**
> y todos los prompts juntos en **[`guia/prompts.md`](guia/prompts.md)**.

## Los datos del mapa

Para no empezar con un mapa vacío, viene **sembrado con 18 lugares reales**: puntos de
trabajo de campo en la **Marina Baja (Alicante)**. Las coordenadas salen del GPS de
fotos reales. Mira **[`datos/README.md`](datos/README.md)**. No tienes que tocarlos:
el agente los usa por ti.

## Qué hay en esta carpeta

- 📄 **`00-ANTES-DEL-TALLER.md`** — empieza aquí (preparación, en casa).
- 🗺️ **`mod1-frontend/`** — Día 1: el mapa.
- ⚙️ **`mod2-backend/`** — Día 2: el servidor.
- 💾 **`mod3-base-de-datos/`** — Día 2: la memoria.
- 📊 **`datos/`** — los 18 lugares de ejemplo.
- 📸 **`fotos_ejemplo/`** — las fotos de esos lugares.
- 📝 **`prompts/`** — los prompts listos para copiar y pegar (un `.txt` por paso).
- 🧭 **`guia/`** — la chuleta de conceptos y cómo **compartir GEOIA**.

---

📷 Las fotos y coordenadas de ejemplo son de **B. Zaragozí (Alicante)** —
gracias por compartirlas. Los materiales del taller son de uso libre. Los detalles
están en [`ATRIBUCION-DATOS.md`](ATRIBUCION-DATOS.md).
