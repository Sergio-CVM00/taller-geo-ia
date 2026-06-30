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
| **uv** (de Astral) | preparar Python (Módulos 2 y 3) | `astral.sh/uv` — o deja que lo haga el agente con el prompt de abajo ↓ |
| **ngrok** | compartir tu app al final | `ngrok.com/download` — el agente lo instala cuando llegues a ese reto |

<details>
<summary><b>Prompt: deja Python listo en casa</b> (opcional — cópialo y pégaselo al agente)</summary>

```text
Eres un asistente que me prepara el entorno para un taller. No sé programar, así que
hazlo tú y explícamelo en pasos sencillos.
Comprueba si tengo instalados uv y Python (para los módulos 2 y 3). Lo que falte, instálalo tú, paso a paso,
enseñándome los comandos. Al terminar, dime en una frase si está todo listo o qué ha
fallado.
```
</details>

> **¿Eliges OpenCode? (casi todos vais con Windows 11)** · Descarga: **`opencode.ai/download`**
> - **Lo más fácil (recomendado):** descarga el instalador de Windows con este enlace
>   directo → **`opencode.ai/download/stable/windows-x64-nsis`** e instálalo como
>   cualquier programa (doble clic → *Siguiente* → *Siguiente* → abrir). Es una app
>   directa, sin terminal (está en *beta*, pero va bien). *(Si el enlace no funciona,
>   entra en `opencode.ai/download` y elige Windows.)*
> - **Tokens (gratis):** al abrir la app, sigue el paso para **conectar tu cuenta**
>   (te lleva a `opencode.ai/auth`) y elige **OpenCode Zen**, su capa gratuita.
> - *Vías avanzadas (terminal), por si prefieres:* `npm i -g opencode-ai@latest` (antes
>   Node.js), o Scoop/Chocolatey — o deja que lo haga el agente con el prompt de abajo ↓.
> - ¿Se te resiste? Usa **Antigravity** (no instala nada) o lo vemos juntos en la sala.

<details>
<summary><b>Prompt: instala OpenCode por terminal en Windows 11</b> (solo si vas por la vía avanzada — cópialo y pégaselo al agente)</summary>

```text
Eres un experto que instala programas en Windows 11 paso a paso. No sé programar, así
que hazlo tú, enséñame cada comando y explícame en español qué hace antes de
ejecutarlo. (PAPEL)

Estoy en Windows 11 y quiero instalar OpenCode, el agente de IA del taller (de la
página opencode.ai). Voy a abrir la aplicación "Windows Terminal" (ya viene con
Windows 11) y partir de cero: no tengo nada instalado. (CONTEXTO)

Quiero terminar con OpenCode funcionando. Sigue el CAMINO 1 y, solo si algo falla,
pásate al CAMINO 2:

CAMINO 1 (recomendado) — con npm:
  1) Instala Node.js (incluye "npm"): primero comprueba si ya lo tengo con
     "node --version"; si no aparece, instálalo con "winget install OpenJS.NodeJS" y
     luego cierra y vuelve a abrir Windows Terminal.
  2) Instala OpenCode con "npm i -g opencode-ai@latest".

CAMINO 2 (si el camino 1 da error) — con un gestor de paquetes:
  - con Scoop: "scoop install opencode", o
  - con Chocolatey: "choco install opencode".

Cuando termines, comprueba que ha quedado instalado con "opencode --version". (TAREA)

Ejecuta los comandos de uno en uno, esperando a que acabe cada uno antes del
siguiente, y dime qué debería ver si va bien. Al final, ayúdame a entrar para tener
modelos gratis: abro OpenCode, escribo "/connect" y me logueo en opencode.ai/auth
eligiendo "OpenCode Zen" (su capa gratuita). (FORMATO)

No instales nada que no haga falta para esto. Si un comando da error, explícamelo en
una frase, prueba el otro camino y dime cómo ha quedado. (LÍMITES)
```
</details>

---

## 2. Descarga el material

Botón verde **`Code` → `Download ZIP`** → **descomprime** → abre la carpeta
**`taller-geo-ia`** en tu agente (arrástrala a la ventana o usa su botón de abrir carpeta).

---

## 3. Construye GEOIA — los pasos

Cada día tiene **un solo fichero** con todo: el prompt para copiar, dónde va tu
archivo, cómo saber que va bien y los retos. Ábrelo y sigue el orden. Recuerda:
**tarea nueva → chat nuevo**.

1. **Día 1 · El mapa** → **[`prompts/dia1.md`](prompts/dia1.md)** *(tu archivo va en
   `modulo-1-mapa/`)*. Trae también un **calentamiento** opcional por si es tu primera vez.
2. **Día 2 · Servidor, memoria y compartir** → **[`prompts/dia2.md`](prompts/dia2.md)**
   *(tus archivos van en `modulo-2-servidor/` y `modulo-3-memoria/`; y al final, el
   enlace temporal con ngrok)*.

> Cada módulo tiene además su **carpeta con un `README`** que te recuerda qué construir ahí.

---

## 4. Los retos — súbele el nivel

El taller sube por **niveles numerados** (Nivel 1 · 2 · 3). En el **Día 1** son retos
opcionales sobre el mapa; en el **Día 2** cada módulo se monta en **3 prompts**, uno por
nivel, que suman de uno en uno.

- **Mapa (Día 1):** color por categoría · foto en el popup · buscador · filtros · favoritos · modo oscuro…
- **Servidor (Día 2):** servir los lugares → añadir lugares → servir tu mapa entero.
- **Memoria (Día 2):** guardar en base de datos → que persista → la app entera; y el broche final: **compartir con ngrok**.

> Los retos completos, con el detalle y **cómo saber que van bien**, van en el fichero
> de cada día: **[`prompts/dia1.md`](prompts/dia1.md)** y **[`prompts/dia2.md`](prompts/dia2.md)**.
> ¿Te atascas en el Módulo 1? Tienes un prompt de solución por reto en
> **[`prompts/retos/`](prompts/retos/)** y un mapa de ejemplo en
> **[`ejemplo-terminado/`](ejemplo-terminado/)** (míralo *cuando ya lo hayas intentado tú*).

---

## Si algo no sale

- **Pega el error entero** al agente: es contexto, y con contexto lo arregla.
- **Tarea nueva → chat nuevo** (cabeza despejada).
- ¿Una palabra te suena rara (mapa, marcador, prompt…)? Pídele al agente que te la
  explique en una frase: para eso está.

> **El límite ya no es saber programar; es lo que te atrevas a imaginar.**

---

> *(Para la IA: el agente lee **`AGENTS.md`** por su cuenta —responde en español, va
> paso a paso y sabe dónde crear cada archivo—. Tú no tienes que abrirlo.)*
