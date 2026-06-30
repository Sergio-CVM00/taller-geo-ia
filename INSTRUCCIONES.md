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
| **Un agente de IA** *(elige uno; valen los dos)* | hablarle y que construya por ti | **Antigravity** → `antigravity.google` (entra con una cuenta **`@gmail` personal**, la **`@us.es` NO** funciona) · **OpenCode** → `opencode.ai` (capa gratuita; pasos justo aquí abajo ↓) |
| **uv** (de Astral) | preparar Python (Módulos 2 y 3) | `astral.sh/uv` — o pega `prompts/antes-preparar-python.txt` y el agente lo deja listo |
| **ngrok** | compartir tu app al final | `ngrok.com/download` — el agente lo instala cuando llegues a ese reto |

> **¿Eliges OpenCode? (casi todos vais con Windows 11)** · Página oficial: **`opencode.ai`**
> - **Instalar** (abre la app **Windows Terminal**, que ya viene en Windows 11):
>   - con **npm** → primero Node.js (`winget install OpenJS.NodeJS`), luego `npm i -g opencode-ai@latest`
>   - o con **Scoop** (`scoop install opencode`) o **Chocolatey** (`choco install opencode`)
> - **Requisitos:** Node.js (para la vía npm) y una terminal moderna (**Windows Terminal** vale).
> - **Tokens (gratis):** abre OpenCode, escribe `/connect` y entra en **`opencode.ai/auth`**;
>   elige **OpenCode Zen**, su capa gratuita para empezar.
> - ¿Se te resiste? Usa **Antigravity** (no instala nada) o lo vemos juntos en la sala.

---

## 2. Descarga el material

Botón verde **`Code` → `Download ZIP`** → **descomprime** → abre la carpeta
**`taller-geo-ia`** en tu agente (arrástrala a la ventana o usa su botón de abrir carpeta).

---

## 3. Construye GEOIA — los pasos

Copia el prompt de cada paso y **pégaselo al agente**. De uno en uno, y recuerda:
**tarea nueva → chat nuevo**.

1. **Día 1 · El mapa** → `prompts/dia1-mapa.txt` *(crea `modulo-1-mapa/`)*.
   ¿Primera vez con un agente? Calienta con `prompts/dia1-calentamiento.txt`.
2. **Día 2 · El servidor** → `prompts/dia2-servidor.txt` *(crea `modulo-2-servidor/`)*.
3. **Día 2 · La memoria** → `prompts/dia2-memoria.txt` *(crea `modulo-3-memoria/`)*.
4. **Día 2 · Compártelo** → `prompts/dia2-compartir.txt` *(un enlace temporal con ngrok)*.

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
