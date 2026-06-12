def buscar_invitado(lista_invitados, ticket_buscar):
    for i in range (len(lista_invitados)):
        

        if lista_invitados[i]['ticket'] == ticket_buscar:
            return i
    return -1

def eliminar_invitado (lista_invitados):
    print("\n--- ELIMINAR INVITADO ---")
    ticket = input("Ingrese el ticker del invitado a eliminar: ")
    posicion = buscar_invitado(lista_invitados, ticket)

    if posicion != -1:
        eliminado = lista_invitados.pop(posicion)
        print(f"El invitado {eliminado['nombre']} con ticket {ticket} fue eliminado")
        return True
    else:
        print("Error: EL ticket no eciste en el sistema")
        return False
    
def mostrar_menu ():
    print("1. registrar invitado\n2-eliminar invitado\n3- ver lista de invitados\n4-Salir")

def leer_opcion():
    opcion = input("Ingrese una opcion del menu: ")
    if opcion in ['1', '2', '3', '4']:
        return int(opcion)
    return 0


def registrar_invitado (lista_invitados, ticket, nombre):
    
    posicion = buscar_invitado(lista_invitados, ticket)

    if posicion >= 0:
        return False
    
    nuevo = {"nombre": nombre, "ticket": ticket, "ingresado":False}
    lista_invitados.append(nuevo)
    return True





def main():

 lista = [
    {"nombre": "Marco", "ticket": "VIP-100"},  # <-- Posición 0
    {"nombre": "Antonia", "ticket": "VIP-200"}, # <-- Posición 1
    {"nombre": "Carlos", "ticket": "VIP-300"}  # <-- Posición 2
    ]

 while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        tkt = input("ingrese ticket: ")
        nombre = input("Ingrese nombre: ")

        if registrar_invitado(lista, tkt, nombre) == True:
            print("Registrado")
        else:
            print("Error de registro")

    elif opcion == 2:
        
        eliminar_invitado(lista)
        

    elif opcion == 3:
        print(f"{lista}")

    elif opcion == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida.")




if __name__ == "__main__":
    main()