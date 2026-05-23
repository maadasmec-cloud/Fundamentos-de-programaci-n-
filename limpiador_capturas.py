from pathlib import Path

ruta_capturas = Path("/home/marco/Imágenes/Capturas de pantalla")

carpeta_destino = {
    ".png": "Capturas_viejas"
}

for elemento in ruta_capturas.iterdir():
    if elemento.is_file():
        extension = elemento.suffix

        if extension in carpeta_destino:
            nombre_carpeta = carpeta_destino [extension]
            nueva_carpeta_ruta = ruta_capturas / nombre_carpeta

            nueva_carpeta_ruta.mkdir(exist_ok = True)

            destino_final = nueva_carpeta_ruta /elemento.name
            elemento.rename(destino_final)


            print(f"Movido correctamente {elemento.name} al directorio {nombre_carpeta}/")
