# Módulo 3 — La memoria de GEOIA: que los lugares no se pierdan 💾
**Día 2 · lo construyes con Antigravity, sin escribir código**

> 🧩 **Pieza independiente.** Construye su propio servidor con memoria partiendo de
> [`../datos/lugares.json`](../datos/lugares.json). **No necesitas haber hecho el
> Módulo 2.**

## Qué es esto (en una frase)

Una **base de datos** es la **memoria que no se borra**: un archivo donde los lugares
se guardan **de verdad**, así que aunque apagues y vuelvas a encender el servidor,
**siguen ahí**. Usarás SQLite, que ya viene con Python: no instalas nada nuevo para
ella.

> Este es el momento bonito del taller: creas un lugar, **apagas y enciendes**, y
> sigue ahí. 🎉

## Antes de empezar

- Tienes Antigravity abierto con la carpeta `taller-geo-ia`.
- Los datos de partida están en [`../datos/lugares.json`](../datos/lugares.json).

> 💡 **Contexto limpio:** ¿vienes de otro módulo? **Chat nuevo** en Antigravity.

## El prompt de partida (cópialo y pégalo)

> 🙌 **No necesitas entender el prompt** (verás palabras técnicas como `SQLite`,
> `uvicorn` o `Path`): cópialo tal cual y pégaselo al agente. Él escribe el código; si
> algo falla, le pegas el error. ¿Te pica la curiosidad por alguna palabra? Mírala en
> la [chuleta](../guia/chuleta-conceptos.md).

```text
Eres un desarrollador que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Estoy en "taller-geo-ia". En "datos/lugares.json" hay lugares con los campos: id,
nombre, lat, lon, categoria, descripcion, foto. (CONTEXTO)

Quiero un archivo "mod3-base-de-datos/main.py" que:
(1) al arrancar, cree una base de datos SQLite "lugares.db" en la misma carpeta que
main.py (usa Path(__file__).parent / "lugares.db");
(2) si la tabla "lugares" no existe, la cree y la cargue con los 18 registros de
datos/lugares.json (Path(__file__).parent.parent / "datos" / "lugares.json"); si la
tabla ya tiene datos, NO inserte nada (para no duplicar al reiniciar);
(3) GET /lugares devuelva todos los registros;
(4) POST /lugares reciba un lugar en JSON (acéptalo con await request.json(), sin
clase Pydantic) y lo guarde. (TAREA)

Usa el entorno virtual (si no existe, créalo con uv venv). Para instalar usa
"uv pip install fastapi uvicorn". Arráncalo con
".venv/bin/uvicorn mod3-base-de-datos.main:app --port 8731" desde "taller-geo-ia",
en un terminal normal. Usa sqlite3, que ya viene con Python: no instales nada más
para la base de datos. (FORMATO)

Un solo main.py, sin subcarpetas, comentado en español, paso a paso. (LÍMITES)
```

## Cómo saber que va bien ✅

1. Aparece un archivo **`lugares.db`** en la carpeta del módulo.
2. En la página de pruebas **`/docs`** (la dirección será algo como
   `http://localhost:8731/docs`), `GET /lugares` devuelve los **18 lugares**.
3. **El momento clave:** en `/docs`, abre **`POST /lugares`** → *Try it out*, pega
   este ejemplo y dale a *Execute*:
   ```json
   { "id": 19, "nombre": "Mi lugar de prueba", "lat": 38.65, "lon": -0.10, "categoria": "Prueba", "descripcion": "Este lo he añadido yo", "foto": "" }
   ```
   > 💬 La caja de *Try it out* puede salir **vacía**: es normal. Pega el ejemplo tal
   > cual (con todas sus llaves y comas) dentro. Si sale un **error en rojo**, borra lo
   > que haya, vuelve a pegar el ejemplo limpio y dale a *Execute* otra vez.

   Luego **dile al agente: "para el servidor y vuelve a arrancarlo"**. Pide otra vez
   `GET /lugares`: tu lugar **sigue ahí**. 🎉

## Si algo falla 🆘

Pega el error entero al agente. Si dice que la tabla "no existe", pídele que la
**cree al arrancar si todavía no existe**. Si al reiniciar **se duplican** los
lugares, dile que **solo siembre los datos si la tabla está vacía**.
- Si al reiniciar el servidor **no arranca** y el error menciona `UNIQUE constraint
  failed`, dile: *"siembra los 18 lugares SOLO si la tabla está vacía, no cada vez"*.
- Si al reiniciar tu lugar **desapareció** y vuelven a salir solo 18, dile: *"no borres
  ni recrees la tabla al arrancar; solo siémbrala si está vacía"*.

## Ahora tú (reto) 🚀

- *"Añade poder borrar un lugar."* Luego pruébalo: **dile al agente "borra el lugar
  con id 19"** (el que creaste) y comprueba que desaparece de la lista.
- *"Déjame editar un lugar."*
- **(Si hiciste los Módulos 1 y 2)** *"Conecta el mapa y el servidor con esta base de
  datos."*
- 🌍 **Compártela:** consigue un **enlace temporal** para que otra persona abra tu app
  desde su móvil u ordenador. Lo tienes paso a paso en
  [`../guia/compartir-tu-app.md`](../guia/compartir-tu-app.md).

> 🎉 Has construido una app web completa **hablando en español**. El límite ya no es
> saber programar: es lo que te atrevas a imaginar.
> **Imagínalo → pídeselo → inténtalo.**
