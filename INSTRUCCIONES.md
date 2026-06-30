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
| **uv** (de Astral) | preparar Python (Módulos 2 y 3) | **deja que lo instale el agente** con el prompt de abajo ↓ (lo pone con `winget`, sin que toques nada) |
| **ngrok** | compartir tu app al final | `ngrok.com/download` — el agente lo instala cuando llegues a ese reto |

<details>
<summary><b>Prompt: deja Python listo en casa</b> (opcional — cópialo y pégaselo al agente)</summary>

```text
Eres un asistente que me prepara el entorno para un taller. No sé programar, así que
hazlo tú y explícamelo en pasos sencillos.
Estoy en Windows 11. Comprueba si tengo uv instalado (con "uv --version"). Si no lo
tengo, instálalo tú con winget: "winget install --id=astral-sh.uv -e" (es el
instalador oficial de uv, https://docs.astral.sh/uv/getting-started/installation/).
Enséñame cada comando antes de ejecutarlo y, al terminar, vuelve a comprobar con
"uv --version" y dime en una frase si está todo listo o qué ha fallado.
```
</details>

> **¿Eliges OpenCode? (casi todos vais con Windows 11)** · Descarga: **`opencode.ai/download`**
> - **Instálalo como cualquier programa (sin terminal, sin Node):** descarga el
>   instalador `.exe` de Windows con este enlace directo →
>   **`opencode.ai/download/stable/windows-x64-nsis`** y ábrelo (doble clic →
>   *Siguiente* → *Siguiente* → abrir). Es la app de escritorio (está en *beta*, pero
>   va bien). *(Si el enlace no funciona, entra en `opencode.ai/download` y elige
>   Windows.)*
> - **Tokens (gratis):** al abrir la app, sigue el paso para **conectar tu cuenta**
>   (te lleva a `opencode.ai/auth`) y elige **OpenCode Zen**, su capa gratuita.
> - ¿Se te resiste? Usa **Antigravity** (no instala nada) o lo vemos juntos en la sala.

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
