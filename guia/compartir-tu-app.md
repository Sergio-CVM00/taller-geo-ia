# 🌍 Comparte tu app con quien quieras

**Día 2 · el broche final: enseñar lo que has construido**

> Has hecho una app **en tu ordenador**. Ahora viene lo bonito: que **otra persona la
> abra desde su móvil o su portátil**. No necesitas saber nada nuevo: se lo pides al
> agente y él te da un **enlace para compartir**.

## Antes de empezar

- Tienes tu app **funcionando** (si es del Módulo 2 o 3, el servidor está encendido en
  una dirección como `http://localhost:8722`).
- 📶 Necesitas **wifi**.

## ¿Qué vas a compartir?

Hay dos casos, y para los dos el agente se encarga:

- 🗺️ **Solo el mapa (Módulo 1)** — es **un archivo** (`index.html`). Lo más simple de
  todo: **mándaselo** a tu compañero o **ábrelo en el proyector**. Ya está.
- ⚙️💾 **Una app con servidor (Módulos 2 o 3)** — vive en *tu* ordenador
  (`localhost` = tu máquina), así que para que otra persona la abra hace falta un
  **enlace temporal a internet**. Eso es lo que pides con el prompt de abajo.

## El prompt para compartir (cópialo y pégalo)

> 🙌 No hace falta entenderlo (verás palabras como `cloudflared` o `túnel`): pégalo tal
> cual. El agente instala lo que haga falta y te devuelve un enlace.

```text
Eres un desarrollador que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Acabo de construir una app en la carpeta "taller-geo-ia" y la tengo funcionando en mi
ordenador, en una dirección como http://localhost:8722. Quiero enseñársela a un
compañero desde SU móvil u ordenador, durante un rato. (CONTEXTO)

Dame un enlace público y temporal que abra mi app desde internet, y a ser posible sin
que tenga que crearme ninguna cuenta. (TAREA)

Usa una herramienta de "túnel" gratuita: prueba primero "cloudflared" con el comando
"cloudflared tunnel --url http://localhost:8722" (no pide registro). Si no está
disponible, usa "ngrok". Si hace falta instalar algo, instálalo tú y enséñame el
comando. Deja encendido el servidor de mi app y arranca el túnel en OTRO terminal.
(FORMATO)

Al terminar, dame el enlace para copiar y pegar. Recuérdame en una frase que es
temporal: deja de funcionar cuando cierre el túnel o apague el ordenador. Nada de
dominios ni configuraciones permanentes. (LÍMITES)
```

> 💡 Si tu app está en otro puerto (por ejemplo `8731` en el Módulo 3), cámbialo en el
> prompt. ¿No sabes cuál es? **Pregúntaselo al agente**: *"¿en qué dirección está
> corriendo mi app?"*.

## Cómo saber que va bien ✅

1. El agente te da un **enlace** parecido a `https://algo-algo.trycloudflare.com`.
2. Lo abres **tú** primero en el navegador para comprobar que se ve tu app.
3. Se lo **mandas a un compañero** (chat, correo…) y lo abre desde **su** dispositivo:
   ve lo mismo que tú. 🎉

## Recuerda 🔔

- El enlace es **temporal**: cuando cierras el túnel o apagas el ordenador, **deja de
  funcionar**. Es justo lo que quieres para una demo del taller.
- Mientras el túnel esté abierto, cualquiera con el enlace puede entrar. Para cerrarlo,
  dile al agente: *"cierra el túnel"* (o cierra ese terminal).

## Si algo falla 🆘

Copia el error entero y pégaselo al agente.
- Si `cloudflared` no se instala o no arranca, dile: *"prueba con ngrok"*.
- Si el enlace abre pero **no se ve tu app**, casi siempre el **servidor se ha parado**:
  pídele al agente que **vuelva a arrancarlo** y deje el túnel apuntando a su dirección.

> 🎉 Acabas de **publicar algo que has construido tú** hablando en español. El límite
> ya no es saber programar; es lo que te atrevas a imaginar.
> **Imagínalo → pídeselo → inténtalo.**
