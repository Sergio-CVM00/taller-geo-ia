# 🌍 Comparte tu app con quien quieras

**Día 2 · el broche final: enseñar lo que has construido**

> Has hecho una app **en tu ordenador**. Ahora viene lo bonito: que **otra persona la
> abra desde su móvil o su portátil**. No necesitas saber nada nuevo: se lo pides al
> agente y él te guía para conseguir un **enlace para compartir**.
>
> 🎈 **Sin presión:** en el taller lo verás primero **en directo**. Si te animas, lo
> haces tú con el prompt de abajo; y si no te da tiempo, **te llevas esta guía** y lo
> haces en casa con calma. Lo importante es **ver que se puede compartir**.

## Antes de empezar

- Tienes tu app **funcionando** (si es del Módulo 2 o 3, el servidor está encendido en
  una dirección como `http://localhost:8722` —o `http://localhost:8731` en el Módulo 3—).
- 📶 Necesitas **wifi**.

## ¿Qué vas a compartir?

- 🗺️ **Solo el mapa (Módulo 1)** — es **un archivo** (`index.html`). Lo más simple:
  **mándaselo** a tu compañero o **ábrelo en el proyector**. Ya está.
- ⚙️💾 **Una app con servidor (Módulos 2 o 3)** — vive en *tu* ordenador
  (`localhost` = tu máquina), así que para que otra persona la abra hace falta un
  **enlace temporal a internet**. Lo consigues con **ngrok** (el prompt de abajo).

## El prompt para compartir (cópialo y pégalo)

> 🙌 No hace falta entenderlo. Pégalo tal cual: el agente instala **ngrok**, lo pone en
> marcha y te da un enlace. **La primera vez** te pedirá crear una **cuenta gratuita de
> ngrok** y pegar un "token" (es normal, solo pasa una vez) — el agente te guía paso a
> paso. Para esa cuenta usa tu **correo personal o tu cuenta de GitHub** (la `@us.es` no
> funciona).

```text
Eres un desarrollador que me ayuda paso a paso. No sé programar; hazlo tú y
explícamelo en español. (PAPEL)

Acabo de construir una app en la carpeta "taller-geo-ia" y la tengo funcionando en mi
ordenador, en una dirección como http://localhost:8722. Quiero enseñársela a un
compañero desde SU móvil u ordenador, durante un rato. (CONTEXTO)

Dame un enlace público y temporal que abra mi app desde internet, usando ngrok. (TAREA)

Instala y configura ngrok tú mismo, enseñándome cada comando. Si ngrok necesita una
cuenta gratuita o un token de autenticación, guíame para conseguirlo paso a paso. Deja
encendido el servidor de mi app y arranca ngrok en OTRO terminal, apuntando al puerto
de mi app. (FORMATO)

Al terminar, dame el enlace para copiar y pegar. Recuérdame en una frase que es
temporal: deja de funcionar cuando lo cierre o apague el ordenador. (LÍMITES)
```

> 💡 Si tu app está en otro puerto (por ejemplo `8731` en el Módulo 3), cámbialo en el
> prompt. ¿No sabes cuál es? **Pregúntaselo al agente**: *"¿en qué dirección está
> corriendo mi app?"*.

## Cómo saber que va bien ✅

1. El agente te da un **enlace** parecido a `https://algo-algo.ngrok-free.app`.
2. Lo abres **tú** primero en el navegador para comprobar que se ve tu app.
3. Se lo **mandas a un compañero** y lo abre desde **su** dispositivo: ve lo mismo. 🎉

> ℹ️ **La primera vez**, ngrok enseña una **página azul de aviso en inglés** (*"You are
> about to visit…"*). Es normal: solo hay que pulsar **"Visit Site"** y ya se ve tu app.
> Avisa a tu compañero para que no piense que está roto.

## Recuerda 🔔

- El enlace es **temporal**: cuando cierras ngrok o apagas el ordenador, **deja de
  funcionar**. Es justo lo que quieres para una demo del taller.
- Para cerrarlo, dile al agente *"cierra ngrok"* (o cierra ese terminal).

## Si algo falla 🆘

Copia el error entero y pégaselo al agente.
- Si ngrok pide un **token** y no sabes de dónde sacarlo, dile: *"guíame para crear la
  cuenta de ngrok y conseguir el token"*.
- Si el enlace abre una **página de error de ngrok** (pone `ERR_NGROK_8012` o
  *connection refused*), casi siempre es el **puerto equivocado**: dile al agente
  *"apunta ngrok al puerto correcto de mi app"* (el Módulo 3 suele ser el **8731**).
- Si el enlace abre pero **no se ve tu app**, casi siempre el **servidor se ha parado**:
  pídele al agente que lo **vuelva a arrancar**.

> 🎉 Acabas de **publicar algo que has construido tú** hablando en español. El límite
> ya no es saber programar; es lo que te atrevas a imaginar.
> **Imagínalo → pídeselo → inténtalo.**
