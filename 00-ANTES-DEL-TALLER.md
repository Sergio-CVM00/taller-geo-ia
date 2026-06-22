# ⚠️ ANTES DEL TALLER — léelo y hazlo en casa

Para no perder tiempo el primer día, **tienes que llegar con esto preparado**.
Son unos 20–25 minutos. Si te atascas, no pasa nada: abriremos la sala 30 minutos
antes (16:30) para ayudarte.

> Necesitas: tu **portátil** (Windows o Mac), el **cargador** y conexión a internet.

---

## ✅ Checklist (haz los 5 pasos)

### Paso 1 — Instala Google Antigravity
1. Entra en **https://antigravity.google** y descarga la versión para tu sistema
   (Windows / Mac).
2. Instálalo como cualquier programa.
3. **En Windows** puede salir una pantalla azul que dice *"Windows protegió tu PC"*.
   Es normal. Pulsa **"Más información"** y luego **"Ejecutar de todas formas"**.

### Paso 2 — Instala Google Chrome
Antigravity usa Chrome para algunas funciones. Si no lo tienes:
**https://www.google.com/chrome**

### Paso 3 — Ten lista una cuenta de Google PERSONAL
Antigravity te pedirá iniciar sesión con Google.

> 🚨 **MUY IMPORTANTE:** usa una cuenta **personal** de `@gmail.com`.
> La cuenta de la universidad (**`@us.es`** / Google Workspace) **NO funciona**
> para entrar en Antigravity. Si no tienes una `@gmail.com`, créate una gratis
> antes de venir: https://accounts.google.com/signup

### Paso 4 — Descarga el material del taller
1. En la página del repositorio, pulsa el botón verde **`Code`** → **`Download ZIP`**.
2. **Descomprime** el ZIP (clic derecho → *Extraer todo*). Guárdalo en un sitio
   fácil de encontrar (por ejemplo, el Escritorio).

> 💡 ¿Prefieres *clonar* el repositorio con Git en vez de descargar el ZIP?
> Perfecto también: acabas con la misma carpeta `taller-geo-ia`.

### Paso 5 — Prepara el entorno de Python (con **uv**)

El proyecto usa unas pocas librerías de Python. Para que el primer día **todo
funcione a la primera**, las dejamos ya instaladas en una "cajita" propia dentro
de la carpeta del taller (un *entorno virtual*: la carpeta `.venv`). Usamos
**uv**, una herramienta gratuita de Astral que se encarga de Python y de las
librerías por ti.

#### 🤖 La forma fácil (recomendada) — que lo haga la IA

Ya tienes Antigravity (Paso 1) y la carpeta (Paso 4): deja que el agente lo
prepare. **Esto es, además, tu primer prompt del taller.**

1. Abre **Antigravity** y abre la carpeta del taller (`taller-geo-ia`).
2. En el panel del agente, **copia y pega este texto** y dale a enviar:

```text
Eres un asistente que me prepara el entorno de Python para un taller. No sé
programar, así que hazlo tú y explícamelo en pasos sencillos.

En esta carpeta hay un archivo "requirements.txt" con las librerías del
proyecto. Quiero que:
1. Instales "uv" (de Astral) si todavía no está, en mi sistema (Windows o Mac).
2. Crees un entorno virtual de Python dentro de esta carpeta, llamado ".venv".
3. Instales en ese entorno las librerías de "requirements.txt".
4. Al terminar, me digas en una frase si ha ido todo bien o qué ha fallado.

Hazlo paso a paso y enséñame los comandos que vas ejecutando.
```

> 💡 Fíjate en cómo está escrito: papel ("eres un asistente"), contexto ("hay un
> requirements.txt"), tarea en pasos y qué esperas al final. Esos son los
> "ingredientes" de un buen prompt — mañana los veremos en detalle.

#### 🛠️ La forma a mano (solo si te animas, o si la IA no pudo)

Abre una **terminal dentro de la carpeta del taller** y ejecuta los comandos uno
a uno. (En Antigravity puedes abrir una terminal; en Mac se llama "Terminal", en
Windows "PowerShell".)

**En Mac:**
```text
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
uv pip install -r requirements.txt
```

**En Windows (PowerShell):**
```text
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv venv
uv pip install -r requirements.txt
```

> Si justo después de instalar uv te dice que "no reconoce" el comando, **cierra
> y vuelve a abrir** la terminal (o Antigravity) y sigue desde `uv venv`. uv se
> descarga Python por ti si no lo tienes.

#### ✅ ¿Cómo sé que ha salido bien?

Dentro de `taller-geo-ia` ha aparecido una carpeta nueva **`.venv`**, y uv ha
instalado **Pillow, pandas, folium y pillow-heif** sin errores en rojo.

> 🆘 **¿Te atascas en algún paso de esta página?** Una vez tengas Antigravity
> abierto, **pega en el panel del agente el trozo que no te sale —o esta guía
> entera— y pídele ayuda en español**: *"No consigo hacer esto, ¿me guías paso a
> paso?"*. Para eso está.

---

## 📸 Paso 6 (opcional, para el Día 2) — Trae tus propias fotos

El segundo día harás el mapa **con tus fotos**. Para que funcione, las fotos
tienen que tener **GPS** (dónde se hicieron). Para conseguirlo:

1. **Activa la ubicación de la cámara** en tu móvil:
   - **iPhone:** Ajustes → Privacidad → Servicios de ubicación → Cámara → *Al usar la app*.
   - **Android:** abre la Cámara → Ajustes → activa *Etiquetas de ubicación / Guardar ubicación*.
2. **Haz unas 15 fotos en exterior** (en la calle, el campo...). Dentro de
   edificios el GPS no suele funcionar.
3. **Pásalas al portátil** (cable, Google Fotos, o envíatelas por email) y
   guárdalas en una carpeta fácil de encontrar.
4. **Si tienes iPhone:** tus fotos pueden ser `.HEIC`. Para evitar problemas,
   en *Ajustes → Cámara → Formatos* elige **"Más compatible"** (hace fotos `.JPG`),
   o expórtalas como JPG al pasarlas.

> ¿No traes fotos? No pasa nada: usaremos las fotos de ejemplo que ya vienen en
> el material. Nadie se queda sin hacer su mapa.

---

## 🟢 Estás listo/a si...

- Al abrir Antigravity ves su pantalla principal con el **panel del agente** (la
  zona donde se le escribe), y has iniciado sesión con tu cuenta `@gmail.com`.
- Dentro de la carpeta `taller-geo-ia` ha aparecido una carpeta **`.venv`**
  (el entorno que preparaste en el Paso 5).

Si tienes las dos cosas, **lo tienes todo**. Nos vemos el 29. 🚀
