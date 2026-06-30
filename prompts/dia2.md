# Día 2 — El servidor, la memoria y compartir ⚙️

**Todo lo del Día 2 en un sitio.** Hoy no construyes de golpe: vas **nivel a nivel**,
y **cada prompt suma una sola cosa** sobre el anterior. Son **6 prompts** (3 para el
servidor, 3 para la memoria) y, aparte, el **broche final** para compartir tu app.

> Empieza el Día 2 **descargando la versión nueva** del repositorio y trayendo tu
> trabajo de ayer. Y el hábito de oro: **tarea nueva → chat nuevo**, con la cabeza
> despejada.

**El viaje de hoy, por dentro:** un **servidor** (Módulo 2) es el *camarero* que sirve
los datos; una **base de datos** (Módulo 3) es la *memoria que no se borra*; y al final
**compartes tu app** con un enlace. Necesitas **uv** instalado (ver
[`../INSTRUCCIONES.md`](../INSTRUCCIONES.md)); si no lo tienes, el agente lo prepara.

> **Cómo van los prompts:** el del **Nivel 1** crea el archivo desde cero; los del
> **Nivel 2 y 3** le piden al agente que **modifique el archivo que ya tienes**. Pégalos
> en orden y prueba después de cada uno antes de pasar al siguiente.

---

## Módulo 2 · El servidor 🍽️  *(suele montarlo el presentador; tú lo sigues)*

**Qué es:** un programita en **Python** que **sirve** la lista de lugares. No se ve como
una web; se prueba en una página automática (**`/docs`**), sin escribir código.

**Dónde se crea:** tu archivo va en **`modulo-2-servidor/main.py`**.

### Nivel 1 · Servir los lugares

**La meta:** que el servidor arranque y entregue los 18 lugares en `GET /lugares`.

```text
Eres un desarrollador backend que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Estoy en la carpeta "taller-geo-ia". En "datos/lugares.json" hay 18 lugares con estos
campos: id, nombre, lat, lon, categoria, descripcion, foto. (CONTEXTO)

Quiero un archivo "modulo-2-servidor/main.py" que, al arrancar, cargue los lugares de
"datos/lugares.json" en una lista en memoria (usa la ruta
Path(__file__).parent.parent / "datos" / "lugares.json") y los devuelva en
GET /lugares. (TAREA)

Usa el entorno virtual del proyecto (si no existe, créalo con "uv venv"). Para instalar
usa siempre "uv pip install fastapi uvicorn" (nunca .venv/bin/pip). Arráncalo desde la
carpeta "taller-geo-ia" con este comando, en un terminal normal (no en segundo plano):
".venv/bin/uvicorn main:app --app-dir modulo-2-servidor --port 8722"
(el "--app-dir" es importante porque la carpeta lleva guiones). Al terminar, dime cómo
abrir la página /docs. (FORMATO)

Un solo archivo, sin subcarpetas, comentado en español, solo fastapi y uvicorn, paso a
paso enseñándome los comandos. (LÍMITES)
```

**Cómo saber que va bien:** el agente te da una dirección tipo
**`http://localhost:8722`**; le añades **`/docs`** y ahí aparece **`GET /lugares`**, que
al ejecutarlo devuelve los **18** lugares.

### Nivel 2 · Añadir lugares

**La meta:** poder **añadir** un lugar nuevo con `POST /lugares` (de momento, en memoria).

```text
Sigues siendo mi desarrollador backend; hazlo tú y explícamelo en español. (PAPEL)

En "taller-geo-ia" ya tengo "modulo-2-servidor/main.py" del paso anterior: carga los
lugares de datos/lugares.json en una lista en memoria y los sirve en GET /lugares.
(CONTEXTO)

Añádele al MISMO archivo un POST /lugares que reciba un lugar nuevo en JSON y lo agregue
a esa lista en memoria. No cambies lo que ya funciona. (TAREA)

Vuelve a arrancarlo igual que antes, desde "taller-geo-ia":
".venv/bin/uvicorn main:app --app-dir modulo-2-servidor --port 8722". Al terminar,
recuérdame cómo probar el POST desde /docs. (FORMATO)

Un solo archivo, comentado en español, solo fastapi y uvicorn, paso a paso. (LÍMITES)
```

**Cómo saber que va bien:** en `/docs` aparece **`POST /lugares`**; tras añadir uno y
volver a ejecutar `GET /lugares`, hay **19**. Si **paras** el servidor, los nuevos
**se pierden**: es "en memoria". Eso lo arregla el Módulo 3.

### Nivel 3 · La app entera

**La meta:** servir **tu mapa** del Día 1 en la raíz `/` y que pida los lugares al
servidor (en vez de llevarlos escritos dentro). Por fin: **mapa + servidor, juntos.**

```text
Sigues siendo mi desarrollador backend; hazlo tú y explícamelo en español. (PAPEL)

En "taller-geo-ia" tengo "modulo-2-servidor/main.py" (sirve GET /lugares y POST
/lugares) y, del Día 1, el mapa en "modulo-1-mapa/index.html". (CONTEXTO)

Quiero abrir la app entera en http://localhost:8722/ : (1) que el servidor sirva mi
mapa en la raíz "/"; y (2) que ese mapa, en lugar de llevar los lugares escritos dentro,
los pida al servidor con fetch a GET /lugares. (TAREA)

No dupliques los datos: el mapa debe mostrar lo que diga el servidor. Arráncalo igual
que antes desde "taller-geo-ia":
".venv/bin/uvicorn main:app --app-dir modulo-2-servidor --port 8722". Al terminar, dime
qué dirección abrir en el navegador. (FORMATO)

Comentado en español, paso a paso, sin añadir cosas que no haya pedido. (LÍMITES)
```

**Cómo saber que va bien:** abres **`http://localhost:8722/`** (la raíz, sin `/docs`) y
ves **tu mapa** con los 18 marcadores… **servidos por el servidor**. Si añades un lugar
con `POST` y recargas, aparece en el mapa.

---

## Módulo 3 · La memoria 🧠  *(lo construyes tú)*

**Qué es:** una **base de datos** es la **memoria que no se borra**: un archivo donde
los lugares se guardan **de verdad**, así que **apagas y enciendes** el servidor y
**siguen ahí**. Usas **SQLite**, que ya viene con Python (no instalas nada extra).

**Dónde se crea:** tu archivo va en **`modulo-3-memoria/main.py`** (y una base de datos
`lugares.db` en la misma carpeta).

### Nivel 1 · Guardar de verdad

**La meta:** que al arrancar cree una base de datos SQLite, la siembre con los 18
lugares y `GET /lugares` los lea **de la base de datos**.

```text
Eres un desarrollador que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Estoy en "taller-geo-ia". En "datos/lugares.json" hay 18 lugares con estos campos:
id, nombre, lat, lon, categoria, descripcion, foto. (CONTEXTO)

Quiero un archivo "modulo-3-memoria/main.py" que: (1) al arrancar, cree una base de
datos SQLite "lugares.db" en la misma carpeta que main.py (usa
Path(__file__).parent / "lugares.db"); (2) si la tabla "lugares" no existe, la cree y
la cargue con los 18 registros de datos/lugares.json; si la tabla YA tiene datos, NO
inserte nada (para no duplicar); y (3) GET /lugares devuelva todos los registros
leyéndolos de la base de datos. (TAREA)

Usa el entorno virtual (si no existe, créalo con "uv venv"). Instala con
"uv pip install fastapi uvicorn". Usa sqlite3, que ya viene con Python: no instales
nada más para la base de datos. Arráncalo desde "taller-geo-ia" con:
".venv/bin/uvicorn main:app --app-dir modulo-3-memoria --port 8731"
(el "--app-dir" es importante porque la carpeta lleva guiones). (FORMATO)

Un solo main.py, sin subcarpetas, comentado en español, paso a paso. (LÍMITES)
```

**Cómo saber que va bien:** aparece el archivo **`lugares.db`** en `modulo-3-memoria/`
y en `/docs` el **`GET /lugares`** devuelve los **18**, esta vez leídos de la base de datos.

### Nivel 2 · Persistir lo nuevo

**La meta:** que `POST /lugares` **guarde en la base de datos**. Aquí llega el momento mágico.

```text
Sigues siendo mi desarrollador; hazlo tú y explícamelo en español. (PAPEL)

En "taller-geo-ia" ya tengo "modulo-3-memoria/main.py" del paso anterior: crea la base
de datos SQLite "lugares.db", la siembra con los 18 lugares y los sirve en GET /lugares
leyéndolos de ahí. (CONTEXTO)

Añádele al MISMO archivo un POST /lugares que reciba un lugar nuevo en JSON (con
await request.json(), sin Pydantic) y lo GUARDE en la base de datos. No cambies lo que
ya funciona. (TAREA)

Arráncalo igual que antes desde "taller-geo-ia":
".venv/bin/uvicorn main:app --app-dir modulo-3-memoria --port 8731". Al terminar,
recuérdame cómo probar el POST desde /docs. (FORMATO)

Un solo main.py, comentado en español, sqlite3 (nada extra para la base de datos),
paso a paso. (LÍMITES)
```

**Cómo saber que va bien — el momento clave:** haces un **`POST`** con un lugar nuevo,
**paras y arrancas** el servidor, vuelves a pedir `GET /lugares`… y **tu lugar sigue
ahí**. 🎉

### Nivel 3 · La app entera con memoria

**La meta:** servir **tu mapa** en la raíz `/` leyendo de la base de datos. La app
completa: lo que añades **se queda** y se ve en el mapa.

```text
Sigues siendo mi desarrollador; hazlo tú y explícamelo en español. (PAPEL)

En "taller-geo-ia" tengo "modulo-3-memoria/main.py" (GET /lugares y POST /lugares contra
SQLite) y, del Día 1, el mapa en "modulo-1-mapa/index.html". (CONTEXTO)

Quiero abrir la app entera en http://localhost:8731/ : (1) que el servidor sirva mi
mapa en la raíz "/"; y (2) que ese mapa pida los lugares con fetch a GET /lugares (que
ahora salen de la base de datos). (TAREA)

No dupliques los datos: el mapa muestra lo que hay en la base de datos. Arráncalo igual
que antes desde "taller-geo-ia":
".venv/bin/uvicorn main:app --app-dir modulo-3-memoria --port 8731". Al terminar, dime
qué dirección abrir. (FORMATO)

Comentado en español, paso a paso, sin añadir cosas que no haya pedido. (LÍMITES)
```

**Cómo saber que va bien:** abres **`http://localhost:8731/`** y ves tu mapa con los
lugares de la base de datos. Añades uno, **reinicias** el servidor, recargas… y **sigue
en el mapa**. Esa es la app entera: mapa + servidor + memoria.

---

## Broche final · Comparte tu app (ngrok) 🌍  *(dirigido por el agente)*

**La idea:** un **enlace temporal** para que otra persona abra tu app desde **su
móvil**. El agente se encarga de todo; tú solo: **inicia sesión → pega el token →
pruébalo**. Es un enlace **temporal**: deja de funcionar cuando lo cierras.

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
