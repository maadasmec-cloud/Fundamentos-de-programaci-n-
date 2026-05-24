raciones_disponibles = 100
raciones_entregadas = 0

while True:

    print("1-Ver raciones disponibles\n2-Distribuir Raciones\n3-Devolver Raciones al deposito\n4-Ver raciones distribuidas\n5-Salir")

    try:
        opcion_menu = int(input("Ingrese una opcion del menú: "))
    except ValueError:
        print("Valor debe ser numérico. Intente nuevamente.")
        continue

    if opcion_menu == 1:
        print(f"Las raciones disponibles en este momento son {raciones_disponibles}")


    elif opcion_menu == 2:
        while True:

            try:
                entrega_raciones = int(input("Ingrese la cantidad de raciones a repartir: "))
                if entrega_raciones > 0 and entrega_raciones <= raciones_disponibles:
                    print(f"Se registra la distribuición de {entrega_raciones} raciones")
                    raciones_disponibles -= entrega_raciones
                    raciones_entregadas += entrega_raciones
                    break
                else:
                    print("Cantidad inválida. No hay suficientes raciones.")

            except ValueError:
                print("Valor debe ser numérico. Intente nuevamente.")

    elif opcion_menu == 3:
        while True:
            try:
                raciones_devolver = int(input("Ingrese cantidad de raciones a devolver: "))

                if raciones_devolver <= raciones_entregadas and raciones_devolver > 0:
                    print(f"Se registra la devolución de {raciones_devolver} raciones")
                    raciones_disponibles += raciones_devolver
                    raciones_entregadas -= raciones_devolver
                    break
                else:
                    print("Cantidad inválida. Supera el límite del refugio.")

            except ValueError:
                print("Valor debe ser numérico. Intente nuevamente.")

    elif opcion_menu == 4:
        print(f"El total de raciones entregadas es de: {raciones_entregadas}")

    elif opcion_menu == 5:
        print("Gracias por utilizar el sistema de control del Refugio 101.")
        break

    else:
        print("Opcion no valida")