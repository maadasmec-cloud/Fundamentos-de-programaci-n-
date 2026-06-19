#================================
#funciones principales
#================================
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar destacado")
    print("5. Mostrar libros")
    print("6. Salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opción del menú: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        else:
             print("Opcion no valida")

#================================
#funciones de validación
#================================

def validar_titulo(titulo):
    return (len(titulo.strip()) > 0)

def cantidad_paginas(paginas):
    return paginas > 0

def validar_puntuacion (puntuacion):
    return puntuacion >= 0 and puntuacion <= 10

#================================
#función buscar
#================================

def buscar_libro(lista_libros, libro_buscar):
    for i in range (len(lista_libros)):
        if lista_libros[i]['titulo'] == libro_buscar:
            return i
    return -1

#================================
#función agregar libro
#================================

def agregar_libro(lista_libros):
    while True:
        titulo = input("Ingrese el titulo del libro: ").strip()
        if validar_titulo(titulo):
            if buscar_libro(lista_libros, titulo) >= 0:
                            print ("Libro ya existe")
            else:
                 break
        else:
             print("Titulo no valido")


    while True:
        try:
              paginas = int(input("Ingrese cantidad de paginas del libro: "))
              if cantidad_paginas(paginas):
                   break
              else:
                   print("Cantidad no valida de paginas")
        except ValueError:
             print("Valor debe ser númerico")


    while True:
        try:
             puntuacion = float(input("Ingrese la puntuación del libro: "))
             if validar_puntuacion(puntuacion):
                  break
             else:
                  print("Puntuación incorrecta")

        except ValueError:
             print("Valor debe ser numerico")


    libro_nuevo = {
        'titulo':titulo,
        'paginas': paginas,
        'puntuacion':puntuacion,
        'destacado': False
                   }
    lista_libros.append(libro_nuevo)
    print("Nuevo libro agregado")

#================================
#función eliminar libro
#================================
def eliminar_libro (lista_libros):
    if len(lista_libros) > 0:
        titulo = input("Ingrese el titulo del libro que desea eliminar: ").strip()
        posicion = buscar_libro(lista_libros, titulo)
        if posicion >= 0:
            lista_libros.pop(posicion)
            print("Libro eliminado")
        else:
            print("EL libro no se encuentra registrado")
    else:
         print("No hay libros registrados para eliminar")

#================================
#función actualizar destacados
#================================
def actualizar_destacados (lista_libros):
    for libro in lista_libros:
        if libro['puntuacion'] >= 8:
            libro['destacado'] = True
        else:
            libro['destacado'] = False
    

#================================
#función mostrar libros
#================================

def mostrar_libros (lista_libros):
     
        actualizar_destacados(lista_libros)
        print("Lista de libros")
        for libro in lista_libros:
            print(f"Titulo: {libro['titulo']}")
            print(f"Paginas: {libro['paginas']}")
            print(f"puntuación: {libro['puntuacion']}")

            if libro['destacado']:
                print("Estado: DESTACADOS")
            else:
                 print("Estado: ESTANDAR")

            print("-------------------------------")
               
    


def systema_central():
     lista_libros = []
     
     while True:
            mostrar_menu()
            opcion = opcion_menu()

            if opcion == 1:
                agregar_libro(lista_libros)

            elif opcion == 2:
                if len(lista_libros) > 0:
                    titulo = input("Ingrese el titulo a buscar: ")
                    posicion = buscar_libro(lista_libros, titulo)
                    if posicion >= 0:
                        print(f"El libro {titulo} se encuenta en la ubicacion {posicion + 1} ")
                        print(lista_libros[posicion])
                    else:
                        print("El libro no se encontro")
                else:
                     print("NO existen libros en el registro para buscar")
                     

            elif opcion == 3:
                eliminar_libro(lista_libros)

            elif opcion == 4:
                actualizar_destacados(lista_libros)
                print("Se actualizaron destacados")
            
            elif opcion == 5:
                mostrar_libros(lista_libros)

               

        

            elif opcion == 6:
                print("Gracias por usar nuestro programa... adios")
                break

            elif opcion == 0:
                 print("Opción no valida")

         
              

     


if __name__ =="__main__":
     systema_central()
            