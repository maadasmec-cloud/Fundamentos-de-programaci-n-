def validar_rut(rut):
    if len(rut) >= 8:
        return True
    return False

def crear_registro (lista_usuarios):
    rut = input("ingrese su rut: ")
    if validar_rut(rut) == True:
        nuevo_usuario = {"rut": rut, "autorizado": False
                         }
        lista_usuarios.append(nuevo_usuario)
        return True
    return False
def mostrar_menu ():
    print("1-Registrar usuario\n2- mostrar base de datos\n3.Salir")


def leer_opcion():
    opcion = input("selecciona una opcion: ")
    if opcion in ['1', '2', '3']:
        return int(opcion)
    return 0



def main():

    lista_usuarios = []
    while True:
        mostrar_menu()
        opcion = leer_opcion()


        if opcion == 1:
           exito = crear_registro(lista_usuarios)

           if exito == True:
               print("Usuario registrado")
           else:
               print("Error no se registro")
            

        elif opcion == 2:
            print(lista_usuarios)


        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida")
                




if __name__ == "__main__":
    main()