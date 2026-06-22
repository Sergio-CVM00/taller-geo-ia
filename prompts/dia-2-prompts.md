# Día 2 — De la tabla a un mapa interactivo 🗺️

**Objetivo de hoy:** convertir `fotos_mapa.csv` en un **mapa interactivo**
(`mapa.html`) donde cada foto aparece en el sitio donde se hizo. Y al final,
hacerlo **con tus propias fotos**.

> ¿No viniste ayer o no tienes el CSV? Pega el `PROMPT 1` del Día 1 primero.

---

## PROMPT 1 — Crear el mapa

```text
Tengo un archivo "fotos_mapa.csv" con estas columnas: archivo, latitud,
longitud, fecha. Las fotos están en la carpeta "fotos_ejemplo".

Crea un archivo "mapa.py" que:
1. Lea el archivo "fotos_mapa.csv".
2. Cree un mapa interactivo y ponga un marcador en cada par de coordenadas.
3. Al pulsar un marcador, que muestre una ventana con la foto correspondiente
   (en pequeño) y debajo su nombre y su fecha.
4. Guarde el mapa como "mapa.html" y ábrelo en el navegador al terminar.

Usa la librería folium e instálala si hace falta. El mapa debe centrarse
automáticamente en la zona de las fotos.
```

> 💡 **Por qué funciona:** reutilizamos el patrón de ayer (tarea numerada +
> formato + librería). Y le damos **el dato clave del contexto**: que el CSV y
> la carpeta de fotos existen y cómo se llaman. La IA no ve tu pantalla; lo que
> no le cuentas, no lo sabe.

---

## PROMPT 2 — Si quieres ajustarlo

```text
Ejecuta mapa.py. Si funciona, ponle un título arriba al mapa que diga
"Mis fotos de campo" y haz los marcadores de color verde.
```

> 💡 Pequeños ajustes en lenguaje natural = iterar. No hace falta saber folium.

---

## 🛠️ Si algo falla
Igual que ayer: **pega el error tal cual** y pide que lo explique y lo arregle.

---

## ✅ Comprobación
Se abre `mapa.html` en el navegador, ves los marcadores sobre Alicante y, al
pulsar uno, **aparece la foto**. 🎉

---

## 🌟 LO IMPORTANTE — hazlo con TUS fotos

Aquí es donde esto se vuelve **tuyo**.

1. **Empieza una conversación nueva** con el agente (chat limpio).
   > 💡 Esto es **ingeniería de contexto**: arrancar sin el "ruido" de lo
   > anterior para que la IA no se confunda. Ventana de contexto limpia.

2. Mete tus fotos en una carpeta (por ejemplo `mis_fotos`) dentro del proyecto y
   usa este prompt:

```text
Tengo mis propias fotos en la carpeta "mis_fotos". Quiero repetir todo el
proceso con ellas: primero leer sus coordenadas GPS y su fecha a un CSV, y
después generar un mapa interactivo "mi_mapa.html" con cada foto en su sitio.
Reutiliza el enfoque de leer_fotos.py y mapa.py pero apuntando a "mis_fotos".
```

3. **Si tus fotos son de iPhone (.HEIC)** y da error, pega esto:

```text
Mis fotos están en formato .HEIC y dan error al leerlas. Añade soporte para
HEIC usando la librería pillow-heif (instálala) y vuelve a intentarlo.
```

> 💡 Si una foto tuya no aparece en el mapa, casi siempre es porque **no tenía
> GPS** (se hizo en interior o con la ubicación desactivada). Es normal.

---

## 🚀 ¿Y ahora qué? — lo que ya puedes hacer

Acabas de crear una herramienta real hablando en español. Lo mismo sirve para
**muchas tareas de tu trabajo**. Mira la pared de ideas en
[`../guia/que-puedes-construir.html`](../guia/que-puedes-construir.html) (y la
lista de [`../guia/chuleta-conceptos.md`](../guia/chuleta-conceptos.md)) y
**elige una tarea aburrida que hagas a mano**. Pruébala esta semana. Ese es el
reto. 💪

> 🌟 **El límite ya no es saber programar; es lo que te atrevas a imaginar.**
> Imagínalo → pídeselo (con los 5 ingredientes) → inténtalo, aunque no salga a
> la primera.
