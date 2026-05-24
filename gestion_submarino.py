tanques_disponibles = 100
tanques_entregados = 0

while True:

    print("1-Ver tanques disponibles\n2-Equipar tanques a los buzos\n3-Retornar tanques a la bodega\n4-Ver tanques usados\n5-Salir")


    try:
        opcion_menu = int(input("Ingrese una opción del menú: "))
    except ValueError:
        print("Valor debe ser numérico. Intente nuevamente.")


    if opcion_menu == 1:
        print(f"Tanques disponibles {tanques_disponibles}")


    elif opcion_menu == 2:
        while True:
            try:
                entrega_tanques = int(input("Ingrese cantidad de tanques a entregar: "))

                if entrega_tanques <= 0:
                    print("Cantidad debe ser mayor a 0.")
                elif entrega_tanques > tanques_disponibles:
                    print("Cantidad no valida. No hay suficientes tanques")

                else:
                    print(f"Se registra la entrega de {entrega_tanques} Tanques de oxigeno")
                    tanques_disponibles -= entrega_tanques
                    tanques_entregados += entrega_tanques
                    break
            except ValueError:
                print("Valor debe ser numérico. Intente nuevamente.")

    elif opcion_menu == 3:
        while True:
            try:
                retorno_tanques = int(input("Ingrese la cantidad de tanques a devolver: "))
                if retorno_tanques > 0 and retorno_tanques <= tanques_entregados:
                    print(f"Se registra la devolución de {retorno_tanques} tanques de oxigeno")
                    tanques_disponibles += retorno_tanques
                    tanques_entregados -= retorno_tanques
                    break

                else:
                    print("Cantidad inválida. Supera los tanques en uso..")

            except ValueError:
                print("Valor debe ser numérico. Intente nuevamente.")

    elif opcion_menu == 4:
        print(f"Tanques entregados o en uso: {tanques_entregados}")


    elif opcion_menu == 5:
        print("Gracias por utilizar el sistema de control del Nautilus.")
        break


