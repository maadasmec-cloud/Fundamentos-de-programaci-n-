def mostrar_menu():
    print("1-largo del nombre \n2-comer\n3-correr\n4-salir")



def leer_opcion():
    opcion = input("selecciona una opcion del menú: ")
    if opcion in ['1','2','3','4']:
        return int(opcion)
    return 0

def largo_palabra(palabra):
    return len(palabra)


def main():

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:

            palabra = input("Ingrese palabra a medir: ")

            print(f"el largo de tu palabra es: {largo_palabra(palabra)} letras")
            

        elif opcion == 2:
            print("Comes un bocado")

        elif opcion == 3:
            print("Sales a correr")

        elif opcion == 4:
            print("Saliendo del programa....")
            break

        else:
            print("opcion no valida. intente nuevamente")


if __name__ == "__main__":
    main()