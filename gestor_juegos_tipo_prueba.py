#========================
#FUCIONES PRINCIPALES
#========================
#MENÚ
def mostar_menu():
    print("===== MENÚ PRINCIPAL ==========")
    print("1- Agregar videojuego")
    print("2- Buscar videojuego")
    print("3- Eliminar videojuego")
    print("4- Actualizar destacados")
    print("5- Mostrar videojuegos")
    print("6- Salir")

#OPCIÓN EN MENÚ
def opcion_menu():
    while True:
        opcion = input("Seleccione una opción del menú: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
            

        else:
            print("Opción no valida")
        
#========================
#FUCIONES DE VALIDACIÓN
#========================

#VALIDAR TITULO
def validar_titulo(titulo):
    return(len(titulo.strip())> 0)

#VALIDAR PUNTUACIÓN
def validar_puntuacion (puntuacion):
    return(puntuacion >= 0 and puntuacion <= 10)

#VALIDAR HORAS DE JUEGO
def validar_horas(horas):
    return(horas > 0)

#========================
#FUNCIÓN DE AGREGAR
#========================
def agregar_juego (lista_juegos):
    while True:
        titulo = input("Ingrese el titulo del juego: ").strip()
        if validar_titulo (titulo):
            if buscar_juego(lista_juegos, titulo) >= 0:
                print("Juego ya existe")
            else:
                break
        else:
            print("Nombre no puede estar vacio o contener solo espacios")

    while True:
        try:
            puntuacion = int(input("Ingrese la puntuación del videojuego: "))
            if validar_puntuacion(puntuacion):
                break
            else:
                print("Puntuación no es valida")
        except ValueError:
            print("Se debe ingresar solo valor númerico")

    while True:
        try:
            horas = int(input("ingrese cantidad de horas del videojuego: "))
            if validar_horas(horas):
                break
            else:
                print("Cantidad de horas no es valida.")
        except ValueError:
            print("Valor a ingresar debe ser númerico")

    video_juego = {
        'titulo':titulo,
        'horas':horas,
        'puntuacion': puntuacion,
        'destacado': False
    }

    lista_juegos.append(video_juego)
    print("VideoJuego agregado")

            
        
#========================
#FUNCIÓN DE BUSCAR
#========================
def buscar_juego(lista_juegos,titulo_buscar):
    for i in range(len(lista_juegos)):
        if lista_juegos[i]['titulo'] == titulo_buscar:
            return i
    return -1

#========================
#FUNCIÓN DE ELIMINAR
#========================

def eliminar_juego(lista_juegos):
    if len(lista_juegos) > 0:
        titulo = input("Ingrese el titulo que quiere eliminar: ").strip()
        posicion = buscar_juego(lista_juegos, titulo)
        if posicion >= 0:
            lista_juegos.pop(posicion)
            print("Videojuego eliminado exitosamente")

        else:
            print("Videojuego no existe")
    else:
        print("Lista de juegos vacia sin elementos que eliminar")

#===================================================
#FUNCIÓN ACTUALIZAR DESTACADOS
#===================================================

def actualizar_destacados(lista_juegos):
    for titulo in lista_juegos:
        if titulo['puntuacion'] >= 8:
            titulo['destacado'] = True

        else:
            titulo['destacado'] = False

#===================================================
#FUNCIÓN  MOSTRAR JUEGOS
#===================================================

def mostrar_juegos(lista_juegos):
    actualizar_destacados(lista_juegos)
    if len(lista_juegos) > 0:
        print("=== LISTA DE VIDEOJUEGOS ===")

        for titulo in lista_juegos:
            print(f"Titulo: {titulo['titulo']}")
            print(f"Horas: {titulo['horas']}")
            print(f"Puntuacion: {titulo['puntuacion']}")

            if titulo['destacado']:
                print("Estado: DESTACADO")
            else:
                print("Estado: ESTANDAR")

            print("-------------------------------")


            


#===================================================
#FUNCIÓN PRINCIPAL
#==================================================
def sistema_central():

    lista_juegos = []
    while True:
        mostar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_juego(lista_juegos)

        elif opcion == 2:
            if len(lista_juegos) > 0:
        
                titulo = input("Ingrese el videojuego que busca: ").strip()
                posicion = buscar_juego(lista_juegos, titulo)
                if posicion >= 0:
                    print(f"El video juego que usted busca esta en la posición {posicion}")
                    print(f"{lista_juegos[posicion]}")
                else:
                    print("Juego no existe")
            else:
                print("lista se encuentra sin juegos registrados")

        elif opcion == 3:
            eliminar_juego(lista_juegos)

        elif opcion == 4:
            actualizar_destacados(lista_juegos)
            print("Se actualizaron los juegos destacados")
        elif opcion == 5:
            mostrar_juegos(lista_juegos)
        elif opcion == 6:
            print("Gracias por usar nuestro sistema de gestion videojuegos, adios.....")
            break



if __name__ == "__main__":
    sistema_central()