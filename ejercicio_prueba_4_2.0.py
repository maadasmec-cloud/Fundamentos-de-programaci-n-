# ==============================
# FUNCIONES DE VALIDACIÓN
# ==============================

def validar_titulo(titulo):
    # No puede estar vacío ni ser solo espacios
    return len(titulo.strip()) > 0


def validar_paginas(paginas):
    # Debe ser entero mayor a 0
    return paginas > 0


def validar_puntuacion(puntuacion):
    # Debe ser decimal entre 0 y 10
    return 0 <= puntuacion <= 10


# ==============================
# FUNCIONES PRINCIPALES
# ==============================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar destacados")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


def opcion_menu():
    # No deja avanzar hasta que el usuario ingrese opción válida
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        else:
            print("Opción inválida, intente nuevamente")


# ==============================
# BÚSQUEDA
# ==============================

def buscar_libro(lista_libros, titulo_buscar):
    # Retorna posición o -1 si no existe
    for i in range(len(lista_libros)):
        if lista_libros[i]["titulo"] == titulo_buscar:
            return i
    return -1


# ==============================
# AGREGAR
# ==============================

def agregar_libro(lista_libros):

    # Validar título
    while True:
        titulo = input("Ingrese título: ").strip()
        if validar_titulo(titulo):
            if buscar_libro(lista_libros, titulo) >= 0:
                print("El libro ya existe")
            else:
                break
        else:
            print("Título inválido")

    # Validar páginas
    while True:
        try:
            paginas = int(input("Ingrese número de páginas: "))
            if validar_paginas(paginas):
                break
            else:
                print("Debe ser mayor a 0")
        except ValueError:
            print("Debe ingresar un número entero")

    # Validar puntuación
    while True:
        try:
            puntuacion = float(input("Ingrese puntuación (0-10): "))
            if validar_puntuacion(puntuacion):
                break
            else:
                print("Debe estar entre 0 y 10")
        except ValueError:
            print("Debe ingresar un número")

    # Crear diccionario EXACTO como pide la pauta
    libro = {
        "titulo": titulo,
        "paginas": paginas,
        "puntuacion": puntuacion,
        "destacado": False
    }

    lista_libros.append(libro)
    print("Libro agregado correctamente")


# ==============================
# ELIMINAR
# ==============================

def eliminar_libro(lista_libros):
    titulo = input("Ingrese título a eliminar: ").strip()

    posicion = buscar_libro(lista_libros, titulo)

    if posicion >= 0:
        lista_libros.pop(posicion)
        print("Libro eliminado")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado")


# ==============================
# ACTUALIZAR DESTACADOS
# ==============================

def actualizar_destacados(lista_libros):
    for libro in lista_libros:
        if libro["puntuacion"] >= 8:
            libro["destacado"] = True
        else:
            libro["destacado"] = False

    print("Destacados actualizados")


# ==============================
# MOSTRAR LIBROS
# ==============================

def mostrar_libros(lista_libros):

    # Primero se actualizan destacados
    actualizar_destacados(lista_libros)

    print("\n=== LISTA DE LIBROS ===")

    for libro in lista_libros:

        print(f"Título: {libro['titulo']}")
        print(f"Páginas: {libro['paginas']}")
        print(f"Puntuación: {libro['puntuacion']}")

        if libro["destacado"]:
            print("Estado: DESTACADO")
        else:
            print("Estado: ESTÁNDAR")

        print("----------------------------------")


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

def sistema_central():

    lista_libros = []  # Lista inicial

    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_libro(lista_libros)

        elif opcion == 2:
            titulo = input("Ingrese título a buscar: ").strip()
            posicion = buscar_libro(lista_libros, titulo)

            if posicion >= 0:
                print("Libro encontrado en posición:", posicion)
                print(lista_libros[posicion])
            else:
                print("Libro no encontrado")

        elif opcion == 3:
            eliminar_libro(lista_libros)

        elif opcion == 4:
            actualizar_destacados(lista_libros)

        elif opcion == 5:
            mostrar_libros(lista_libros)

        elif opcion == 6:
            print("Gracias por usar el sistema de la biblioteca. Vuelva pronto")
            break


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    sistema_central()