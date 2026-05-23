from pathlib import Path

#1- Definir la ruta de la carpeta descarga
ruta_descargas = Path("/home/marco/Descargas")

#2- definir un diccionario con las extensiones que queremos ordenar
#puede agregar más extensiones aquí si quieres (ej: ".xlsx"): "EXcels")
carpetas_destino = {
    ".zip": "Archivos_Zip",
    ".pdf": "Documentos_PDF",
    ".html": "Paginas_Web",
    ".xlsx": "Archivos_excel"
    }


print("---ordenando la carpeta de descargas de fedora ---")

#3. El ciclo principal que recorre la carpeta
for elemento in ruta_descargas.iterdir():
    # Filtro 1: Asegurar que sea un archivo y no una carpeta
    if elemento.is_file():
        extension = elemento.suffix

        #Filtro 2: Verificar si tienes una carpeta asignada para esa extensión
        if extension in carpetas_destino:
            nombre_carpeta = carpetas_destino[extension]
            nueva_carpeta_ruta = ruta_descargas / nombre_carpeta

            # Acción 1: Crear la carpeta de destino si no existe
            nueva_carpeta_ruta.mkdir(exist_ok=True)


            # Acción 2: Definir la ruta final y mover el archivo
            destino_final = nueva_carpeta_ruta / elemento.name
            elemento.rename(destino_final)



            print(f"Movido con exito: {elemento.name} -->  {nombre_carpeta}/")

