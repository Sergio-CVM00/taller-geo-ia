# Chuleta para llevarte 🧠

Un resumen de todo lo del taller. Guárdalo: es lo que necesitas para seguir
usando la IA en tu trabajo **sin nosotros al lado**.

---

## 1. ¿Qué es esto de la IA? (en una frase)
Programas que han "leído" enormes cantidades de texto y código y, a partir de
ahí, **predicen la mejor respuesta** a lo que les pides. No "piensan" como
nosotros; son muy buenos completando y transformando.

**Los asistentes que oirás nombrar** (todos hacen cosas parecidas):
- **ChatGPT** (OpenAI) · **Gemini** (Google) · **Claude** (Anthropic).
- Existen modelos *abiertos* (Llama, Kimi, GLM…) que se pueden instalar uno
  mismo, pero para tu día a día los de arriba te sobran.
- En este taller usamos **Gemini dentro de Antigravity**.

---

## 2. Prompt engineering — cómo pedir las cosas
Un buen prompt lleva **5 ingredientes**:

| Ingrediente | Ejemplo |
|---|---|
| **Papel** | "Eres un asistente que me ayuda a..." |
| **Contexto** | "Tengo una carpeta con fotos .JPG que tienen GPS..." |
| **Tarea** (en pasos) | "1. Lee... 2. Calcula... 3. Guarda..." |
| **Formato** | "...un CSV con las columnas archivo, latitud, longitud" |
| **Límites** | "Usa solo Pillow y pandas. Si falla, avisa." |

> 🔴 **Flojo:** *"hazme algo con las fotos"*
> 🟢 **Bueno:** los 5 ingredientes juntos.

**Reglas de oro:** sé concreto · da ejemplos · di el formato que quieres ·
pide que te explique antes de actuar · itera con frases pequeñas.

---

## 3. Context engineering — qué "sabe" la IA en cada momento
La IA solo conoce **lo que hay en la conversación** (su "ventana de contexto").
No ve tu pantalla ni se acuerda de otra conversación.

- 🟢 **Contexto limpio:** lo que le das es relevante a la tarea de ahora
  (el error que salió, el archivo correcto, el objetivo claro).
- 🔴 **Contexto sucio:** mezcla de cosas viejas, intentos fallidos y temas
  distintos → la IA se confunde y responde peor.

**Reglas prácticas:**
- ¿Cambias de tarea? → **abre una conversación nueva**.
- ¿Error? → **pega el error entero**; es contexto valiosísimo.
- Dale **el nombre exacto** de archivos y carpetas.
- No le hagas adivinar lo que tú ya sabes.

---

## 4. ¿Qué es un agente (o "harness")?
Un asistente normal solo *habla*. Un **agente** además **actúa en tu ordenador**:
crea y edita archivos, abre la terminal, ejecuta programas, instala librerías.
Antigravity es un agente. Por eso pudo escribir *y ejecutar* tu programa.

> ⚠️ Como actúa de verdad, **revisa lo que hace** antes de aceptar cambios
> grandes. Tú mandas: puedes aceptar o rechazar.

> 💡 **Truco de profesional:** un proyecto puede incluir un archivo `AGENTS.md`
> con reglas que el agente **lee solo** al abrir la carpeta (en qué idioma
> responder, qué entorno usar, qué librerías...). Este taller trae uno: por eso
> el asistente "ya sabe" responder en español y usar el entorno correcto sin que
> se lo recuerdes. Es *ingeniería de contexto* hecha permanente.

---

## 5. 🚀 Qué puedes hacer AHORA en tu trabajo
Lo que hiciste (carpeta → procesar → resultado) se aplica a muchísimo:

- 📂 **Renombrar u organizar** cientos de archivos por fecha, lugar o nombre.
- 🗺️ **Poner en un mapa** cualquier Excel/CSV que tenga coordenadas o direcciones.
- 📄 **Sacar una tabla** de un PDF (informes, boletines) a Excel.
- 🖼️ **Redimensionar o convertir** imágenes en lote (incl. HEIC → JPG).
- 🛰️ **Recortar o renombrar** capas/imágenes para tus análisis.
- 📊 **Limpiar y graficar** una hoja de cálculo desordenada.
- 🌐 **Descargar datos** de una web y guardarlos en una tabla.
- 📝 Convertir formatos: shapefile ↔ GeoJSON ↔ CSV, etc.

---

## 🎯 Tu reto
Elige **una tarea repetitiva y aburrida** que hagas a mano en tus estudios o
trabajo. Esta semana, ábrela en Antigravity y pídesela con los 5 ingredientes.
Aunque no salga a la primera, **lo habrás intentado tú solo/a**. Ese es el
objetivo de todo esto. 💪

---

### Para seguir
- Antigravity: https://antigravity.google
- Gemini: https://gemini.google · ChatGPT: https://chat.openai.com · Claude: https://claude.ai
