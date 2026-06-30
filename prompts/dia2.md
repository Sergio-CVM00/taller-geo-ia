# Día 2 — El servidor, la memoria y compartir ⚙️

**Todo lo del Día 2 en un sitio:** los prompts para el servidor, la memoria y el
enlace para compartir, dónde se crea cada archivo, cómo saber que va bien y los retos.

> Empieza el Día 2 **descargando la versión nueva** del repositorio y trayendo tu
> trabajo de ayer. Y el hábito de oro: **tarea nueva → chat nuevo**, con la cabeza
> despejada.

**El viaje de hoy, por dentro:** un **servidor** (Módulo 2) es el *camarero* que sirve
los datos; una **base de datos** (Módulo 3) es la *memoria que no se borra*; y al final
**compartes tu app** con un enlace. Necesitas **uv** instalado (ver
[`../INSTRUCCIONES.md`](../INSTRUCCIONES.md)); si no lo tienes, el agente lo prepara.

---

## Módulo 2 · El servidor 🍽️  *(suele montarlo el presentador; tú lo sigues)*

**Qué es:** un programita en **Python** que **sirve** la lista de lugares y deja
**añadir** nuevos. No se ve como una web; se prueba en una página automática
(**`/docs`**), sin escribir código.

**Dónde se crea:** tu archivo va en **`modulo-2-servidor/main.py`**.

### El prompt (cópialo y pégalo)

```text
Eres un desarrollador backend que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Estoy en la carpeta "taller-geo-ia". En "datos/lugares.json" hay lugares con estos
campos: id, nombre, lat, lon, categoria, descripcion, foto. (CONTEXTO)

Quiero un archivo "modulo-2-servidor/main.py" que: (1) al arrancar, cargue los lugares
de "datos/lugares.json" en una lista en memoria (usa la ruta
Path(__file__).parent.parent / "datos" / "lugares.json"); (2) los devuelva en
GET /lugares; y (3) permita añadir uno nuevo con POST /lugares. (TAREA)

Usa el entorno virtual del proyecto (si no existe, créalo con "uv venv"). Para instalar
usa siempre "uv pip install fastapi uvicorn" (nunca .venv/bin/pip). Arráncalo desde la
carpeta "taller-geo-ia" con este comando, en un terminal normal (no en segundo plano):
".venv/bin/uvicorn main:app --app-dir modulo-2-servidor --port 8722"
(el "--app-dir" es importante porque la carpeta lleva guiones). Al terminar, dime cómo
abrir la página /docs. (FORMATO)

Un solo archivo, sin subcarpetas, comentado en español, solo fastapi y uvicorn, paso a
paso enseñándome los comandos. (LÍMITES)
```

### Cómo saber que va bien
1. El agente te da una dirección tipo **`http://localhost:8722`**; le añades **`/docs`**.
2. En `/docs` aparecen **`GET /lugares`** (devuelve los **18**) y **`POST /lugares`**
   (tras añadir uno, hay **19**).
3. Si paras el servidor, los nuevos **se pierden**: es "en memoria". Eso lo arregla el
   Módulo 3.

### Los retos
| Nivel | A | B | C |
|---|---|---|---|
| Para coger confianza | Pedir un lugar por su id (`GET /lugares/{id}`) | Un endpoint `/salud` que diga que el servidor está vivo | Cambiar el título y la descripción de `/docs` |
| Interacción de verdad | Filtrar por categoría (`/lugares?categoria=Olivar`) | Búsqueda por texto en nombre y descripción | Borrar un lugar (`DELETE /lugares/{id}`) |
| Atrévete | Servir tu mapa en `http://localhost:8722/` | Lista de categorías con su recuento | Conectar el mapa para que pida los lugares a la API |

---

## Módulo 3 · La memoria 🧠  *(lo construyes tú)*

**Qué es:** una **base de datos** es la **memoria que no se borra**: un archivo donde
los lugares se guardan **de verdad**, así que **apagas y enciendes** el servidor y
**siguen ahí**. Usas **SQLite**, que ya viene con Python (no instalas nada extra).

**Dónde se crea:** tu archivo va en **`modulo-3-memoria/main.py`** (y una base de datos
`lugares.db` en la misma carpeta).

### El prompt (cópialo y pégalo)

```text
Eres un desarrollador que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Estoy en la carpeta "taller-geo-ia". En "datos/lugares.json" hay lugares con estos
campos: id, nombre, lat, lon, categoria, descripcion, foto. (CONTEXTO)

Quiero un archivo "modulo-3-memoria/main.py" que:
(1) al arrancar, cree una base de datos SQLite "lugares.db" en la misma carpeta que
main.py (usa Path(__file__).parent / "lugares.db");
(2) si la tabla "lugares" no existe, la cree y la cargue con los 18 registros de
datos/lugares.json; si la tabla ya tiene datos, NO inserte nada (para no duplicar);
(3) GET /lugares devuelva todos los registros;
(4) POST /lugares reciba un lugar en JSON (con await request.json(), sin Pydantic) y
lo guarde. (TAREA)

Usa el entorno virtual (si no existe, créalo con "uv venv"). Instala con
"uv pip install fastapi uvicorn". Arráncalo desde la carpeta "taller-geo-ia" con:
".venv/bin/uvicorn main:app --app-dir modulo-3-memoria --port 8731"
(el "--app-dir" es importante porque la carpeta lleva guiones). Usa sqlite3, que ya
viene con Python: no instales nada más para la base de datos. (FORMATO)

Un solo main.py, sin subcarpetas, comentado en español, paso a paso. (LÍMITES)
```

### Cómo saber que va bien
1. Aparece el archivo **`lugares.db`** y en `/docs` el **`GET /lugares`** da los **18**.
2. **El momento clave:** haces un **`POST`** con un lugar nuevo, **paras y arrancas** el
   servidor, vuelves a pedir `GET /lugares`… y **tu lugar sigue ahí**. 🎉

### Los retos *(el último es el broche final del taller)*
| Nivel | A | B | C |
|---|---|---|---|
| Para coger confianza | Borrar un lugar | Editar un lugar | Ver un lugar por su id |
| Interacción de verdad | Filtrar por categoría (`/lugares?categoria=Olivar`) | Búsqueda por texto | Ordenar los lugares por nombre |
| Atrévete | Servir tu mapa leyendo de la base de datos (**¡la app entera!**) | Guardar la fecha en que añadiste cada lugar | **Compartir tu app con un enlace (ngrok)** ↓ |

---

## Broche final · Comparte tu app (ngrok) 🌍  *(dirigido por el agente)*

**La idea:** un **enlace temporal** para que otra persona abra tu app desde **su
móvil**. El agente se encarga de todo; tú solo: **inicia sesión → pega el token →
pruébalo**. Es un enlace **temporal**: deja de funcionar cuando lo cierras.

### El prompt (cópialo y pégalo)

```text
Eres un desarrollador que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Tengo mi app funcionando en mi ordenador (algo como http://localhost) y quiero
enseñársela a otra persona desde su móvil, un rato. (CONTEXTO)

Dame un enlace público y temporal con ngrok. Encárgate tú de todo: instálalo,
ayúdame a iniciar sesión y a pegar el token la primera vez (usa mi correo personal
o GitHub; la cuenta @us.es no funciona) y arráncalo contra el puerto de mi app. (TAREA)

Hazlo paso a paso, enseñándome cada comando. Deja mi app encendida y arranca ngrok
en otro terminal. (FORMATO)

Al final dame el enlace para copiar y recuérdame en una frase que es temporal:
deja de funcionar cuando lo cierre. (LÍMITES)
```

---

## El cierre

Habrás construido una **app web completa hablando en español**: mapa, servidor y
memoria, y la habrás **compartido** con alguien.

> El límite ya no es saber programar; es lo que te atrevas a imaginar.
> **Imagínalo → pídeselo → inténtalo.**
