def validar_precio(precio):
    if precio > 0:
        return True
    return False

def agregar_producto(lista_productos):
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
           precio = int(input(f"Ingrese el precio de {nombre}: "))
           if precio > 0:
               break
        except ValueError:
            print("Valor debe ser numerico")

    if validar_precio (precio) == True:
        producto_nuevo = {"nombre": nombre, "precio": precio, "Disponible": True
        }
        lista_productos.append(producto_nuevo)
        return True
    return False

def mostrar_menu ():
    print("1- agregar producto\n2- ver inventario \n3.Salir")


def leer_opcion():
    opcion = input("selecciona una opcion: ")
    if opcion in ['1', '2', '3']:
        return int(opcion)
    return 0



def main():

    lista_productos = []
    while True:
        mostrar_menu()
        opcion = leer_opcion()


        if opcion == 1:
           exito = agregar_producto(lista_productos)

           if exito == True:
               print("Producto registrado")
           else:
               print("Error no se registro producto")
            

        elif opcion == 2:
            print(lista_productos)


        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida")
                




if __name__ == "__main__":
    main()