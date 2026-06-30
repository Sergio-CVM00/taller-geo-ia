# INSTRUCCIONES — Taller GEOIA

Tu guía de bolsillo: **qué instalar, qué hacer y los retos.** Construyes **GEOIA**,
una app web (un mapa de lugares), **hablando en español con una IA**. No programas:
**diriges, miras y decides.** *Imagínalo → pídeselo → inténtalo.*

---

## 1. Requisitos — instala esto primero

> No te agobies: **el agente puede instalar casi todo por ti.** Si algo se resiste, lo
> vemos juntos (abrimos la sala 30 min antes, a las 16:30).

| Qué | Para qué | Dónde |
|---|---|---|
| **Un agente de IA** *(elige uno; valen los dos)* | hablarle y que construya por ti | **Antigravity** → `antigravity.google` (entra con una cuenta **`@gmail` personal**, la **`@us.es` NO** funciona) · **OpenCode** → `opencode.ai/download` (app de escritorio, lo más fácil; pasos abajo ↓) |
| **uv** (de Astral) | preparar Python (Módulos 2 y 3) | `astral.sh/uv` — o pega `prompts/antes-preparar-python.txt` y el agente lo deja listo |
| **ngrok** | compartir tu app al final | `ngrok.com/download` — el agente lo instala cuando llegues a ese reto |

> **¿Eliges OpenCode? (casi todos vais con Windows 11)** · Descarga: **`opencode.ai/download`**
> - **Lo más fácil (recomendado):** descarga el instalador de Windows con este enlace
>   directo → **`opencode.ai/download/stable/windows-x64-nsis`** e instálalo como
>   cualquier programa (doble clic → *Siguiente* → *Siguiente* → abrir). Es una app
>   directa, sin terminal (está en *beta*, pero va bien). *(Si el enlace no funciona,
>   entra en `opencode.ai/download` y elige Windows.)*
> - **Tokens (gratis):** al abrir la app, sigue el paso para **conectar tu cuenta**
>   (te lleva a `opencode.ai/auth`) y elige **OpenCode Zen**, su capa gratuita.
> - *Vías avanzadas (terminal), por si prefieres:* `npm i -g opencode-ai@latest` (antes
>   Node.js), o Scoop/Chocolatey — o pega `prompts/instalar-opencode.txt` y lo hace un agente.
> - ¿Se te resiste? Usa **Antigravity** (no instala nada) o lo vemos juntos en la sala.

---

## 2. Descarga el material

Botón verde **`Code` → `Download ZIP`** → **descomprime** → abre la carpeta
**`taller-geo-ia`** en tu agente (arrástrala a la ventana o usa su botón de abrir carpeta).

---

## 3. Construye GEOIA — los pasos

Copia el prompt de cada paso y **pégaselo al agente**. De uno en uno, y recuerda:
**tarea nueva → chat nuevo**.

1. **Día 1 · El mapa** → `prompts/dia1-mapa.txt` *(tu archivo va en `modulo-1-mapa/`)*.
   ¿Primera vez con un agente? Calienta con `prompts/dia1-calentamiento.txt`.
2. **Día 2 · El servidor** → `prompts/dia2-servidor.txt` *(en `modulo-2-servidor/`)*.
3. **Día 2 · La memoria** → `prompts/dia2-memoria.txt` *(en `modulo-3-memoria/`)*.
4. **Día 2 · Compártelo** → `prompts/dia2-compartir.txt` *(un enlace temporal con ngrok)*.

> Cada módulo tiene su **carpeta con un `README`** que explica qué construir ahí.

---

## 4. Los retos — súbele el nivel

Cada módulo tiene retos en tres niveles (**confianza · interacción · atrévete**).
**No son obligatorios:** sube por la escalera lo que te apetezca, una mejora cada vez.

- **Mapa:** color por categoría · foto en el popup · buscador · filtros · favoritos · modo oscuro…
- **Servidor:** pedir un lugar por su id · filtrar por categoría · borrar · servir tu mapa…
- **Memoria:** borrar/editar · ordenar · guardar la fecha · y el broche final: **compartir con ngrok**.

> Todos los retos, con el detalle y **cómo saber que van bien**, en
> **[`guia/hoja-de-ruta.md`](guia/hoja-de-ruta.md)**.
> ¿Te atascas en el Módulo 1? Tienes un prompt de solución por reto en
> **[`prompts/soluciones/`](prompts/soluciones/)** y un mapa de ejemplo en
> **[`ejemplo-terminado/`](ejemplo-terminado/)** (míralo *cuando ya lo hayas intentado tú*).

---

## Si algo no sale

- **Pega el error entero** al agente: es contexto, y con contexto lo arregla.
- **Tarea nueva → chat nuevo** (cabeza despejada).
- ¿Una palabra te suena rara? Mira la **[chuleta](guia/chuleta-conceptos.md)**.

> **El límite ya no es saber programar; es lo que te atrevas a imaginar.**

---

> *(Para la IA: el agente lee **`AGENTS.md`** por su cuenta —responde en español, va
> paso a paso y sabe dónde crear cada archivo—. Tú no tienes que abrirlo.)*
