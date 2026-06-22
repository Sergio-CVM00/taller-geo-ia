# Reglas del proyecto para el asistente de IA

> **Para quién es esto:** reglas para el asistente de IA que usa una persona
> **mientras hace el taller** (p. ej. Google Antigravity, que lee este archivo
> al empezar cada sesión). Si eres un agente ayudando a **desarrollar** los
> materiales del taller, mira `../CLAUDE.md` en su lugar.

## Con quién hablas

- La persona usuaria es **alumnado de Geografía que no sabe programar**.
  Trátala como principiante absoluto/a.
- **Responde siempre en español (de España)**, claro y sencillo. Si usas un
  término técnico, explícalo en una frase.

## Antes de actuar

- Antes de escribir o ejecutar código, **di en una frase qué vas a hacer**.
- **Enseña los comandos** que ejecutas: la persona aprende mirándote.
- Ve **paso a paso**; no encadenes muchas acciones sin parar a enseñar el
  resultado.
- Tú propones; **ella acepta o rechaza** los cambios. No des nada por hecho.

## Entorno de Python — IMPORTANTE

- Este proyecto tiene un entorno virtual **`.venv`** (creado con **uv**) en la
  raíz de la carpeta. **Usa siempre ese `.venv`, nunca el Python global** del
  sistema.
- Para **ejecutar** los scripts, llama al intérprete de `.venv` (actívalo o
  invócalo directamente): en Mac/Linux `.venv/bin/python`, en Windows
  `.venv\Scripts\python.exe`.
- Si falta una librería, instálala **dentro de `.venv`** con `uv pip install …`,
  no a nivel global. Las del proyecto ya están en `requirements.txt`:
  **Pillow, pandas, folium, pillow-heif**.
- Si no existe `.venv`, créalo con `uv venv` e instala `requirements.txt` antes
  de ejecutar nada.

## Cómo escribir el código

- Python **sencillo y comentado en español**. Que se entienda importa más que
  que sea "elegante".
- Usa **solo** las librerías del proyecto (arriba). No añadas dependencias ni
  estructura extra que no se haya pedido.
- Respeta los nombres de archivo: `leer_fotos.py`, `fotos_mapa.csv`, `mapa.py`,
  `mapa.html` (salvo que te pidan otra cosa).

## Cuando algo falla

- Los errores son normales. **Explica el error en una frase** y arréglalo.
- Si te pegan un mensaje de error, úsalo tal cual: es contexto valioso.

## El proyecto en una línea

Leer fotos con GPS de `fotos_ejemplo/` → `leer_fotos.py` crea `fotos_mapa.csv`
→ `mapa.py` genera un mapa interactivo `mapa.html`. (Día 2: repetir el proceso
con las fotos propias de la persona, en una carpeta `mis_fotos/`.)
