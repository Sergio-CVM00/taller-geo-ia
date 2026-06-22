#!/usr/bin/env python3
"""
preparar_datos.py
-----------------
Descarga un subconjunto pequeno del dataset publico de fotos de campo
geoetiquetadas (Marina Baja, Alicante) desde Zenodo, las reduce de tamano
y verifica que cada foto conserva sus coordenadas GPS en el EXIF.

Resultado: la carpeta `fotos_ejemplo/` con ~18 fotos ligeras y geolocalizadas,
lista para el taller (esta es la "via garantizada" para todos los alumnos).

Fuente de datos (licencia CC-BY-4.0):
  Zaragozi, B. (2020). A geotagged image dataset with compass directions for
  studying the drivers of farmland abandonment. Zenodo.
  https://doi.org/10.5281/zenodo.3733436

Uso:
  python scripts/preparar_datos.py
"""
import os
import sys
import urllib.request
from PIL import Image

# --- Configuracion -------------------------------------------------------
RECORD = "3733436"
BASE_URL = f"https://zenodo.org/api/records/{RECORD}/files/{{name}}/content"
N_OBJETIVO = 18          # cuantas fotos validas queremos
LADO_MAX = 1024          # px del lado mayor tras reducir
CALIDAD = 80             # calidad JPEG de salida

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
DESTINO = os.path.join(RAIZ, "fotos_ejemplo")
CACHE = os.path.join(RAIZ, ".cache_descargas")

# Nombres confirmados via API de Zenodo. Si alguno no trae GPS, se omite.
CANDIDATOS = [
    "DSC02592.JPG", "DSC02778.JPG", "DSC02591.JPG", "DSC02590.JPG",
    "DSC02589.JPG", "DSC02588.JPG", "DSC02256.JPG", "DSC02257.JPG",
    "DSC02777.JPG", "DSC02776.JPG", "DSC02258.JPG", "DSC02669.JPG",
    "DSC02775.JPG", "DSC01684.JPG", "DSC02664.JPG", "DSC01923.JPG",
    "DSC01924.JPG", "DSC01925.JPG", "DSC01926.JPG", "DSC01927.JPG",
]


def _a_decimal(valor, ref):
    """Convierte coordenada EXIF (grados, min, seg) + referencia a decimal."""
    g, m, s = [float(x) for x in valor]
    dec = g + m / 60.0 + s / 3600.0
    if ref in ("S", "W"):
        dec = -dec
    return round(dec, 6)


def leer_gps(ruta):
    """Devuelve (lat, lon) en decimal o None si la foto no tiene GPS."""
    try:
        with Image.open(ruta) as img:
            exif = img.getexif()
            gps = exif.get_ifd(0x8825)  # IFD de GPS
            if not gps:
                return None
            lat = _a_decimal(gps[2], gps[1])
            lon = _a_decimal(gps[4], gps[3])
            return (lat, lon)
    except Exception:
        return None


def descargar(nombre):
    os.makedirs(CACHE, exist_ok=True)
    destino = os.path.join(CACHE, nombre)
    if os.path.exists(destino) and os.path.getsize(destino) > 0:
        return destino
    url = BASE_URL.format(name=nombre)
    urllib.request.urlretrieve(url, destino)
    return destino


def reducir_y_guardar(origen, nombre):
    salida = os.path.join(DESTINO, nombre)
    with Image.open(origen) as img:
        exif_bytes = img.info.get("exif")
        img.thumbnail((LADO_MAX, LADO_MAX))
        img.save(salida, "JPEG", quality=CALIDAD, exif=exif_bytes)
    return salida


def main():
    os.makedirs(DESTINO, exist_ok=True)
    validas = []
    print(f"Preparando hasta {N_OBJETIVO} fotos en {DESTINO}\n")
    for nombre in CANDIDATOS:
        if len(validas) >= N_OBJETIVO:
            break
        try:
            origen = descargar(nombre)
        except Exception as e:
            print(f"  [omitida] {nombre}: error de descarga ({e})")
            continue
        salida = reducir_y_guardar(origen, nombre)
        gps = leer_gps(salida)
        if gps is None:
            os.remove(salida)
            print(f"  [omitida] {nombre}: sin GPS en EXIF")
            continue
        kb = os.path.getsize(salida) // 1024
        validas.append((nombre, gps[0], gps[1], kb))
        print(f"  [OK] {nombre}  lat={gps[0]:.5f}  lon={gps[1]:.5f}  ({kb} KB)")

    print(f"\nListo: {len(validas)} fotos geolocalizadas en fotos_ejemplo/")
    if len(validas) < N_OBJETIVO:
        print("Aviso: menos de las deseadas; anade mas nombres a CANDIDATOS.")
    return 0 if validas else 1


if __name__ == "__main__":
    sys.exit(main())
