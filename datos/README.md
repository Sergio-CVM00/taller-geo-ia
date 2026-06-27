# Los datos de partida del mapa

El mapa del taller no empieza vacío: viene **sembrado con 18 lugares reales** — puntos
de trabajo de campo en la **Marina Baja (Alicante)**.

## Archivos

- **`lugares.json`** — los 18 lugares. Es el que usa el **Módulo 1** para pintar los
  marcadores.
- **`lugares.csv`** — los mismos datos en tabla, por si quieres abrirlos en Excel o
  cargarlos en la base de datos del **Módulo 3**.

## Qué guarda cada "lugar"

Cada lugar tiene su **nombre**, sus **coordenadas** (latitud y longitud, que es lo que
lo coloca en el mapa), una **categoría** (qué se ve: bancales, frutales, olivar,
matorral…), una **descripción** corta y la **ruta a su foto**. También un **id** (un
número que lo identifica). **No necesitas entender ni tocar nada de esto**: el agente
los usa tal cual.

> Las coordenadas son reales: los 18 puntos caen en la Marina Baja (alrededor de
> **lat 38.6, lon -0.1**). Si alguno te sale en mitad del mar, algo se ha leído mal —
> díselo al agente.

Origen y licencia de los datos: ver [`../ATRIBUCION-DATOS.md`](../ATRIBUCION-DATOS.md).
