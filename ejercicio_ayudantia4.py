def validar_nombre(nombre):
    return(len(nombre.strip()) > 0)
def validar_stock(stock):
    return(stock >= 0)
def validar_precio(precio):
    return(precio > 0)

def buscar_juego(lista_juegos,juego_buscar):
    for i in range(len(lista_juegos)):
        if lista_juegos[i]['nombre'] == juego_buscar:
            return i
    return -1
def mostrar_menu():
    print("=======MENÚ PRINCIPAL=============")
    print("1- Agregar")
    print("Buscar")
    print("Eliminar")
    print("actualizar")
    print("Mostrar")
    print("salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese la opción: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        print("Opción no valida, Intente nuevamente")

def agregar_juego(lista_juegos):
    while True:
        nombre = input("Ingrese nombre del juego: ")
        if validar_nombre(nombre):
            if buscar_juego(lista_juegos, nombre) != -1:
                print("Juego ya existe en el registro")
                return
            break
        else:
            print("Nombre no valido")
    
    while True:
        try:
            stock = int(input("Ingrese stock: "))
            if validar_stock(stock):
                break
            else:
                print("Stock no es valido")
        except ValueError:
            print("Valor debe ser numerico")

    while True:
        try:
            precio = float(input("Ingrese el precio del juego: "))
            if validar_precio(precio):
                break
            else:
                print("Precio no es valido")
        except ValueError:
            print("Valor debe ser númerico")

    juego = {
        'nombre': nombre,
        'stock': stock,
        'precio': precio,
        'disponible': True 
    }

    
    lista_juegos.append(juego)
    print("Se agrego el juego al registro")


def eliminar_juego(lista_juegos):
    if len(lista_juegos) > 0:
        nombre = input("ingrese el juego que quiere eliminar: ")
        posicion = buscar_juego(lista_juegos, nombre)
        if posicion >= 0:
            lista_juegos.pop(posicion)
            print("Juego eliminado")
        else:
            print("El juego que quiere eliminar no se encuentra")
    else:
        print("Lista vacia no hay juegos que eliminar")

def mostrar_juego(lista_juegos):
    print("=========LISTA DE JUEGOS==========")
    actalizar_estado(lista_juegos)
    for juego in lista_juegos:
        print(f"Nombre: {juego['nombre']}")
        print(f"Stock: {juego['stock']}")
        print(f"Precio: {juego['precio']}")
        if juego['disponible'] == True:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO DISPONIBLE")
        print("**"*40)

def actalizar_estado(lista_juegos):
    for juego in lista_juegos:
        if juego['stock'] > 0:
            juego['disponible'] = True
        else:
            juego['disponible'] = False

def sistema_principal():
    lista_juegos =[]
    while True:

        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_juego(lista_juegos)
        if opcion == 2:
            if len(lista_juegos) > 0:
                juego = input("Ingrese el juego que busca: ")
                posicion = buscar_juego(lista_juegos, juego)
                if posicion != -1:
                    print(f"Su juego se encuentra en la pisición: {posicion}")
                    print(f"Nombre: {lista_juegos[posicion]['nombre']}")
                    print(f"Stock: {lista_juegos[posicion]['stock']}")
                    print(f"Precio: {lista_juegos[posicion]['precio']}")
                else:
                    print("el juego no existe")

        elif opcion == 3:
            eliminar_juego(lista_juegos)

        elif opcion == 4:
            print("Se actualizaron juegos con stock")
            actalizar_estado(lista_juegos)

        elif opcion == 5:
            mostrar_juego(lista_juegos)

        elif opcion == 6:
            print("Saliendo del programa, adios")
            break
                    

if __name__ == "__main__":
    sistema_principal()