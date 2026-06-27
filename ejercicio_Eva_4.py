import json 
#=============================
#FUNCIÓN DE GUARDAR PELICULA
#=============================
def guardar_peliculas_json(lista_peliculas):
    try:
        with open("base_peliculas.json", "w", encoding="utf-8") as archivo:
            #json.dump toma la lista de diccionarios y las escribe en el archivo
            json.dump(lista_peliculas, archivo,  ensure_ascii=False, indent=4)
        print("[SISTEMA] Datos respaldados con éxito en el disco duro.")
    except Exception as e:
        print(f"Errori al guardar los datos: {e}")

#=============================
#FUNCIÓN DE CARGAR PELICULAS
#=============================
def cargar_peliculas_json():
    import os
    #esto valida si el archivo existe en el computador
    if os.path.exists("base_peliculas.json"):
        try:
            with open ("base_peliculas.json", "r", encoding="utf-8") as archivo:
              # json.load toma el archivo de texto y lo transforma de vuelta en una lista de diccionarios
                return json.load(archivo)
        except Exception:
            print("Error al cargar base de datos, se iniciará una lista vacía.")
            return []
    return []

#=============================
#FUNCIONES PRINCIPALES
#=============================
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6- Salir")
    print("=====================================")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opción del menú: ").strip()
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        print("Opción no válida. intente nuevamente")
#=============================
#FUNCIONES DE VALIDACIÓN
#=============================
def validar_titulo(titulo):
    return(len(titulo.strip())> 0)

def validar_duracion(duracion):
    return(duracion > 0)

def validar_calificacion(calificacion):
    return(calificacion >= 0 and calificacion <= 10)

def tiene_peliculas(lista_peliculas):
    return(len(lista_peliculas) > 0)
#Esta función valida si la lista tiene peliculas en su registro.
#=============================
#FUNCIÓN DE BUSQUEDA
#=============================   
def buscar_pelicula(lista_peliculas,pelicula_buscar):
    for i in range (len(lista_peliculas)):
        if lista_peliculas[i]['titulo'].lower() == pelicula_buscar.lower():
            return i
    return -1

#=============================
#FUNCIÓN DE AGREGAR
#=============================
def agregar_pelicula(lista_peliculas):
    while True:
        titulo = input("Ingrese el titulo de la película: ").strip()
        if validar_titulo(titulo):
            if buscar_pelicula(lista_peliculas,titulo) >= 0:
                print("película ya esta registrada.")
                #Aquí se puede aplicar un return para que en el caso el usuario ingrese una pelicula que ya esta en el registro lo devuelva al menú principal.
            else:
                break
        else:
            print("Titulo no válido.")
    while True:
        try:
            duracion = int(input("Ingrese duración de la película en minutos: "))
            if validar_duracion(duracion):
                break
            else:
                print("Duración no es válida. Intente nuevamente.")
        except ValueError:
            print("Dato a ingresar debe ser un valor númerico entero.")

    while True:
        try:
            calificacion = float(input("Ingrese la calificación de la película: "))
            if validar_calificacion(calificacion):
                break
            else:
                print("Calificación no es valida. intente nuevamente.")
        except ValueError:
            print("dato a ingresar debe ser valor númerico(puede ser decimal). ")

    nueva_pelicula = {
        'titulo':titulo,
        'duracion':duracion,
        'calificacion':calificacion,
        'disponible':False
    }

    lista_peliculas.append(nueva_pelicula)
    print("Se registrado la película exitosamente.")


#=============================
#FUNCIÓN DE ACTUALIZAR
#=============================
def actualizar_peliculas(lista_peliculas):
    for pelicula in lista_peliculas:
        if pelicula['calificacion'] >= 7.0:
            pelicula['disponible'] = True
        else:
            pelicula['disponible'] = False
   
#=============================
#FUNCIÓN DE MOSTRAR PELICULAS
#=============================
def mostrar_peliculas(lista_peliculas):
    if tiene_peliculas(lista_peliculas):
        actualizar_peliculas(lista_peliculas)
        print("=== LISTA DE PELICULAS ===")
        for pelicula in lista_peliculas:
            print(f"Titulo: {pelicula['titulo'].title()}")
            print(f"Duración: {pelicula['duracion']}")
            print(f"Calificación: {pelicula['calificacion']}")
            if pelicula['disponible'] == True:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: NO RECOMENDADA")
            print("********************************************")
    else:
        print("Lista vacia. No hay películas que mostrar.")

#=============================
#FUNCIÓN DE ELIMINAR PELICULAS
#=============================
def eliminar_pelicula(lista_peliculas):
    if tiene_peliculas(lista_peliculas):
        pelicula = input("Ingrese el nombre de la película a eliminar: ").strip()
        posicion = buscar_pelicula(lista_peliculas,pelicula)
        if posicion >= 0:
            lista_peliculas.pop(posicion)
            print("Se elimino la película.")
        else:
            print(f"La película {pelicula.title()} no se encuentra registrada.")
    else:
        print("Lista vacia. No hay películas para eliminar.")



def sistema_principal():
    lista_peliculas = cargar_peliculas_json()
    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_pelicula(lista_peliculas)

        elif opcion == 2:
            if tiene_peliculas(lista_peliculas):
                pelicula = input("Ingrese el el titulo de la película que busca: ").strip()
                posicion = buscar_pelicula(lista_peliculas,pelicula)
                if posicion >= 0:
                    print("==== película encontrada ====")
                    print(f"La película esta en la posición: {buscar_pelicula(lista_peliculas, pelicula)+ 1}") 
                    #Se configura con un +1 para que en este caso el usuario vea algo amigable, ya que en la primera pelicula veria el indice que es 0.
                    print(f"Titulo: {lista_peliculas[posicion]['titulo'].title()}")
                    print(f"Duración: {lista_peliculas[posicion]['duracion']}")
                    print(f"Calificación: {lista_peliculas[posicion]['calificacion']}")
                else:
                    print("Película no encontrada.")
            else:
                print("Lista vacia. No hay películas para buscar.")
            
        elif opcion == 3:
            eliminar_pelicula(lista_peliculas)
        
        elif opcion == 4:
            if tiene_peliculas(lista_peliculas):
                actualizar_peliculas(lista_peliculas)
                print("Se actualizo el estado de las películas.")
            else:
                print("Lista vacia. No hay películas para actualizar.")

        elif opcion == 5:
            mostrar_peliculas(lista_peliculas)
        
        elif opcion == 6:
            guardar_peliculas_json(lista_peliculas)
            print("“Gracias por usar el sistema. Vuelva Pronto”")
            break

if __name__ == "__main__":
    sistema_principal()
            