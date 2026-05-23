plataformas_disponibles = 100
reservas_realizadas = 0

while True:

    print("1-Ver plataformas disponibles\n2-Reseervar plataformas\n3-Cancelar reserva\n4.Ver reservas realizadas\n5-Salir")

    try:
        opcion_menu = int(input("Ingrese una opción del menu: "))
    except ValueError:
        print("Error. opcion no valida")
        continue

    if opcion_menu == 1:
        print(f"El total de plataformas disponibles es: {plataformas_disponibles}")

    elif opcion_menu == 2:
        while True:
            try:
                cantidad_reservas = int(input("Ingrese cantidad a reservar: "))
                if cantidad_reservas > 0 and cantidad_reservas <= plataformas_disponibles:
                    print(f"Reserva de {cantidad_reservas} reservas fue realizada")
                    reservas_realizadas += cantidad_reservas
                    plataformas_disponibles -= cantidad_reservas
                    break
                else:
                    print("Error. cantidad no es correcta.")

            except ValueError:
                print("Error. valor incorrecto")

    elif opcion_menu == 3:
        while True:
                try:
                    cancelar_cantidad = int(input("Ingrese cantidad de reservas que quiere cancelar: "))
                    if cancelar_cantidad > 0 and cancelar_cantidad <= reservas_realizadas:
                        print(f"se registran {cancelar_cantidad} reservas a cancelar")
                        reservas_realizadas -= cancelar_cantidad
                        plataformas_disponibles += cancelar_cantidad
                        break
                    else:
                        print("Cantidad incorrecta")
                except ValueError:
                    print("Error. valor incorrecto")

    elif opcion_menu == 4:
        print(f"cantidad de reservas realizadas es: {reservas_realizadas}")

    elif opcion_menu == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida")

