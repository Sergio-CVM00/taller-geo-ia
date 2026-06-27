# Módulo 2 — El servidor de GEOIA: una API que sirve los lugares
**Día 2 · lo enseña el presentador en directo (y, si quieres, lo sigues tú)**

> **Pieza independiente.** Parte de [`../datos/lugares.json`](../datos/lugares.json)
> y se prueba sola. **No necesitas haber hecho el Módulo 1.**

## Qué es esto (en una frase)

Un **servidor** es como un **camarero**: espera peticiones y responde con lo que le
pides. La **API** es su **menú**: la lista de lo que puedes pedirle. Aquí montarás un
camarero pequeño, hecho con **Python**, que sirve la lista de lugares y deja
**añadir** nuevos.

> Es la **parte que no se ve** de una app, pero es la que hace el trabajo. La probarás
> en una página de pruebas automática (la `/docs`), sin escribir código.

## Antes de empezar

- Tienes Antigravity abierto con la carpeta `taller-geo-ia`.
- Python se prepara solo durante el taller: el agente crea un **entorno** propio (una
  cajita aparte para no tocar el resto de tu ordenador). Los datos están en
  [`../datos/lugares.json`](../datos/lugares.json).

> **Contexto limpio:** ¿vienes de otro módulo? Abre un **chat nuevo** en
> Antigravity para empezar con la cabeza despejada.

## El prompt de partida (cópialo y pégalo)

> **No necesitas entender el prompt** (verás palabras técnicas como `uvicorn` o
> `Path`): cópialo tal cual y pégaselo al agente. Él escribe el código; si algo falla,
> le pegas el error. ¿Te pica la curiosidad por alguna palabra? Mírala en la
> [chuleta](../guia/chuleta-conceptos.md).

```text
Eres un desarrollador backend que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Estoy en "taller-geo-ia". En "datos/lugares.json" hay lugares con los campos: id,
nombre, lat, lon, categoria, descripcion, foto. (CONTEXTO)

Quiero un archivo "mod2-backend/main.py" que: (1) al arrancar, cargue los lugares de
"datos/lugares.json" en una lista en memoria (usa la ruta
Path(__file__).parent.parent / "datos" / "lugares.json"); (2) los devuelva en
GET /lugares; y (3) permita añadir uno nuevo con POST /lugares. (TAREA)

Usa el entorno virtual del proyecto (si no existe, créalo con uv venv). Para instalar
usa siempre "uv pip install fastapi uvicorn" (nunca .venv/bin/pip). Arráncalo con
".venv/bin/uvicorn mod2-backend.main:app --port 8722" desde la carpeta "taller-geo-ia",
en un terminal normal (no en segundo plano), y dime cómo abrir la página de pruebas
/docs. (FORMATO)

Un solo archivo, sin subcarpetas, comentado en español, solo fastapi y uvicorn, paso
a paso enseñándome los comandos. (LÍMITES)
```

## Cómo saber que va bien

1. El agente arranca el servidor y te da una dirección parecida a
   **`http://localhost:8722`** (`localhost` = tu propio ordenador). Pega esa dirección
   en el navegador y **añade `/docs`** al final.
2. Verás un **formulario naranja**: es la página de pruebas de la API, donde pruebas
   todo **sin escribir código**. Aparecen `GET /lugares` y `POST /lugares`.
3. Abre `GET /lugares` → *Try it out* → *Execute*: devuelve los **18 lugares**.
4. Abre `POST /lugares`, rellena un lugar nuevo y ejecútalo; vuelve a `GET /lugares` y
   ahora hay **19**.

> Como guarda los lugares "en memoria", si **paras el servidor se pierden los
> nuevos**. Es normal: darles memoria de verdad es justo lo del Módulo 3.

## Si algo falla

Copia el error entero y pégaselo al agente: pegar el error es darle contexto.
- Si **`/docs` sale en blanco** o sin estilo, es la conexión a internet de esa página de
  pruebas, no tu servidor: recarga, o pídele al agente *"ábreme `GET /lugares` en el
  navegador"* (verás el JSON con los 18 lugares, así sabes que el servidor va bien).
- Si el agente menciona un error de **CORS** (un bloqueo de seguridad rutinario del
  navegador), **no es culpa tuya**: pídele que lo arregle él en la API.

## Ahora tú (retos)

Pídele mejoras **de una en una** (en el mismo chat; si se empieza a liar, abre uno
nuevo). **No necesitas saber cómo se hace: descríbelo en español y deja que el agente
escriba el código.** Todo se prueba en la misma página `/docs`. Sube por la escalera lo
que quieras.

> ¿Te atascas en el **reto A** de algún nivel? Tienes un prompt de ejemplo en
> [`../prompts/retos/`](../prompts/retos/) (`mod2-nivel1-confianza-A.txt` … `mod2-nivel3-atrevete-A.txt`). Míralo
> solo si lo necesitas: lo suyo es **describir tú la mejora en español**.

**Nivel 1 · Para coger confianza**
- **A.** *"Añade GET /lugares/{id} para devolver un solo lugar por su id."*
- **B.** *"Añade un endpoint /salud que responda que el servidor está vivo."*
- **C.** *"Cambia el título y la descripción que aparecen arriba en la página /docs."*

**Nivel 2 · Interacción de verdad**
- **A.** *"Haz que pueda filtrar los lugares por categoría, por ejemplo /lugares?categoria=Olivar."*
- **B.** *"Añade una búsqueda por texto que mire en el nombre y la descripción."*
- **C.** *"Permite borrar un lugar con DELETE /lugares/{id}."*

**Nivel 3 · Atrévete**
- **A.** *"Sirve mi mapa desde aquí: que al abrir http://localhost:8722/ se vea el mapa del Módulo 1."*
- **B.** *"Dame la lista de categorías con cuántos lugares tiene cada una."*
- **C.** **(Si hiciste el Módulo 1)** *"Conecta mi mapa de mod1-frontend para que pida los lugares a esta API en vez de llevarlos dentro del HTML."*

> Los retos **no son obligatorios**: elige los que te apetezcan. Y si uno se resiste,
> ya sabes — **copia el error y pégaselo al agente**.

> ¿Viste que al **parar el servidor se pierden** los lugares nuevos? El **Módulo 3**
> les da **memoria de verdad** para que no se pierdan — y también se construye por
> separado.
