![GEOIA - Taller de la Universidad de Sevilla](portada-readme.svg)

# Construye tu primera app web hablando en español

**Universidad de Sevilla · Cátedra de IA US-Google · Cactus Accelerative Innovation**
29 y 30 de junio de 2026 · 17:00 · Facultad de Geografía e Historia

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

## El plan del taller

**GEOIA** se construye por piezas, una por módulo:

- **Día 1 — El mapa** (`modulo-1-mapa/`): un mapa en el navegador con los lugares
  marcados; pulsas uno y ves su nombre y su descripción. Su guía trae el prompt listo
  para pegar.
- **Día 2 — El servidor y la memoria** (`modulo-2-servidor/`, `modulo-3-memoria/`):
  el motor que sirve los datos y la base de datos que los recuerda; y al final,
  **compartes tu app** con un enlace.

> ¿Quieres el **mapa completo del viaje** (qué construyes cada día, los prompts y cómo
> sabrás que va bien)? Está en los ficheros de cada día:
> **[`prompts/dia1.md`](prompts/dia1.md)** y **[`prompts/dia2.md`](prompts/dia2.md)**.
> El Día 1 montas el mapa; lo demás lo descubrimos en directo.
>
> *(Por curiosidad: el mapa usa una librería llamada Leaflet. No necesitas saber qué
> es: el agente se encarga.)*

## Cómo empezar (3 pasos)

1. **Antes del taller** → lee **[`INSTRUCCIONES.md`](INSTRUCCIONES.md)** e instala los
   requisitos (el agente de IA, `uv`). Son 15–20 minutos. (Si te atascas, no pasa nada:
   abrimos la sala a las 16:30 para echarte una mano.)
2. **En el taller** → abre tu **agente de IA** (Antigravity u OpenCode) y carga esta
   carpeta `taller-geo-ia` (arrástrala a la ventana o usa su botón de abrir carpeta).
3. **Sigue el día** → abre **[`prompts/dia1.md`](prompts/dia1.md)**: trae el prompt
   para copiar, dónde va tu archivo, cómo saber que va bien y los retos. Todo junto.

> ¿Es tu primera vez con un agente? El propio `prompts/dia1.md` empieza con un
> **calentamiento** opcional (una página web sencilla para perderle el miedo).

## Los datos del mapa

Para no empezar con un mapa vacío, viene **sembrado con 18 lugares reales**: puntos de
trabajo de campo en la **Marina Baja (Alicante)**. Las coordenadas salen del GPS de
fotos reales. Mira **[`datos/README.md`](datos/README.md)**. No tienes que tocarlos:
el agente los usa por ti.

## Qué hay en esta carpeta

- **`INSTRUCCIONES.md`** — empieza aquí (requisitos, pasos y retos, todo junto).
- **`modulo-1-mapa/`** — Día 1: el mapa (aquí creas tu `index.html`).
- **`modulo-2-servidor/`** — Día 2: el servidor (aquí creas tu `main.py`).
- **`modulo-3-memoria/`** — Día 2: la base de datos (aquí creas tu `main.py`).
- **`datos/`** — los 18 lugares de ejemplo.
- **`fotos_ejemplo/`** — las fotos de esos lugares.
- **`prompts/`** — **un fichero por día** con todo (`dia1.md`, `dia2.md`) y, en
  `prompts/retos/`, un prompt de solución por cada reto del Módulo 1.
- **`ejemplo-terminado/`** — un mapa de ejemplo con los retos del Módulo 1 ya hechos.
- **`presentacion/`** — la presentación del taller para repasarla a tu ritmo.

> Cada módulo **ya tiene su carpeta con un `README`** que te dice qué construir ahí.
> Las de los Módulos 2 y 3 empiezan vacías (solo el `README`): el archivo lo creas tú
> el Día 2 hablando con el agente.

---

Las fotos y coordenadas de ejemplo son de **B. Zaragozí (Alicante)** —
gracias por compartirlas. Los materiales del taller son de uso libre. Los detalles
están en [`ATRIBUCION-DATOS.md`](ATRIBUCION-DATOS.md).
