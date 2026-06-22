# Día 1 — De una carpeta de fotos a una tabla 📋

**Objetivo de hoy:** que la IA escriba un programa que lea las fotos de
`fotos_ejemplo/` y cree una tabla (`fotos_mapa.csv`) con el nombre, las
coordenadas GPS y la fecha de cada foto.

## Cómo usar esta guía
- Cada bloque **`PROMPT`** es texto para **copiar y pegar** en el panel del
  agente de Antigravity.
- Debajo de cada prompt hay una nota **💡 Por qué funciona** — léela: ahí está
  la verdadera lección (cómo se le habla a la IA).
- Ve **uno a uno**. No tengas prisa. Cada vez que tengas un resultado, levanta
  la vista y seguimos todos juntos.

---

## 🔴 vs 🟢 Primero, mira la diferencia

Antes de empezar, observa estos dos prompts para la *misma* tarea:

> 🔴 **Prompt flojo:** `hazme algo para las fotos`

> 🟢 **Prompt bueno:** el `PROMPT 1` de abajo.

El flojo obliga a la IA a adivinar y gasta intentos (y tu cuota). El bueno le da
**papel, datos, tarea, formato y límites**. Regla de oro de hoy:
**piensa antes de pulsar enviar; un buen prompt vale por diez malos.**

---

## PROMPT 1 — Crear el programa

```text
Eres un asistente que me ayuda a crear un script de Python sencillo y comentado.
No sé programar, así que explícalo de forma clara.

Tengo una carpeta llamada "fotos_ejemplo" con fotos .JPG tomadas en trabajo de
campo. Cada foto guarda sus coordenadas GPS en los metadatos EXIF.

Crea un archivo "leer_fotos.py" que haga lo siguiente:
1. Recorra todas las fotos .JPG de la carpeta "fotos_ejemplo".
2. De cada foto, lea: el nombre del archivo, la latitud y la longitud en grados
   decimales, y la fecha en que se tomó.
3. Guarde esos datos en un archivo "fotos_mapa.csv" con estas columnas exactas:
   archivo, latitud, longitud, fecha
4. Si una foto no tiene GPS, que la omita y avise por pantalla.

Usa solo las librerías Pillow y pandas, e instálalas si hace falta.
Antes de escribir el código, dime en una frase qué va a hacer el programa.
```

> 💡 **Por qué funciona (esto es "prompt engineering"):**
> - **Papel:** *"Eres un asistente... explícalo de forma clara."*
> - **Contexto:** le decimos qué hay en la carpeta y que el GPS está en el EXIF.
> - **Tarea numerada:** pasos concretos, no una idea vaga.
> - **Formato exacto:** las columnas que queremos, con sus nombres.
> - **Límites:** qué librerías usar y qué hacer con los errores.
> - **Comprobación:** le pedimos que explique antes de programar, para detectar
>   malentendidos *antes* de gastar otro intento.

---

## PROMPT 2 — Ejecutarlo

Cuando el agente haya escrito el archivo, pídele que lo pruebe:

```text
Ejecuta el programa y enséñame las primeras filas del archivo fotos_mapa.csv
que ha creado.
```

> 💡 Antigravity puede **ejecutar el programa él mismo** (abre la terminal por
> ti). Eso es lo que hace especial a un *agente*: no solo escribe, también actúa.

---

## 🛠️ Si algo falla (te va a pasar, y está bien)

No reescribas el prompt entero. **Copia el mensaje de error tal cual** y pégalo:

```text
Ha dado este error. Explícame en una frase qué significa y arréglalo:

[pega aquí el error completo]
```

> 💡 Pegar el error es darle **contexto** a la IA. Sin el error, adivina; con el
> error, lo arregla. Mañana llamaremos a esto "ingeniería de contexto".

---

## ✅ Comprobación del Día 1

Abre `fotos_mapa.csv` (Antigravity puede mostrártelo). Debes ver **una fila por
foto** con columnas `archivo, latitud, longitud, fecha`, y las coordenadas
rondando **38.6, -0.1** (Alicante). Si lo ves: **¡has hecho software hablando en
español!**

---

## ✍️ AHORA TÚ (sin prompt escrito — invéntalo)

Pídele al agente, **con tus palabras**, que **añada una columna nueva** a la
tabla: por ejemplo *la hora* a la que se hizo la foto, o *cuántas fotos hay en
total* al final. Piensa en la regla de oro: papel, tarea, formato.

> Esto es lo que de verdad te llevas: no el programa, sino **saber pedirlo**.

---

### Cierre
Guarda tu trabajo. Mañana convertimos esta tabla en un **mapa interactivo** y
luego lo harás **con tus propias fotos**. 👋
