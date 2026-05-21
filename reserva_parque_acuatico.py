cupos_disponibles = 100
reservas = 0
cupos_reservados = 0


while True:

    print("1-Ver cupos disponibles\n2-Reservar cupos\n3-Cancelar reserva\n4-Ver reservas realizadas\n5-Salir")

    try:
        opcion_menu = int(input("ingrese una opcion: "))
    except ValueError:
        print("error. seleccione una opcion correcta")
        continue

    if opcion_menu == 1:
        print(f"cupos disponibles {cupos_disponibles}")

    elif opcion_menu == 2:
        print("Reservar")
        while True:
            try:
                reserva_cupos = int(input("Ingrese cantidad de cupos a reservar: "))
                if reserva_cupos > 0 and  reserva_cupos <= cupos_disponibles:
                    reservas += reserva_cupos
                    cupos_disponibles -= reserva_cupos
                    print(f"se reservaron {reserva_cupos} cupos")
                    break
                elif reserva_cupos > cupos_disponibles:
                    print(f"No hay cupos disponibles para su reserva. cupos disponibles {cupos_disponibles}")
                else:
                    print("numero no valido")

            except ValueError:
                print("Dato ingresado incorrecto, debe ser numero positivo")

    elif opcion_menu == 3:
        print("Cancelar")
        while True:
            try:
                reservas_cancelar = int(input("ingrese el numero de reservas a cancelar: "))
                if reservas_cancelar > 0 and reservas_cancelar <= reservas and (reservas_cancelar + cupos_disponibles) <= 100:
                    print (f"Se cancelan {reservas_cancelar} reservas")
                    cupos_disponibles += reservas_cancelar
                    reservas -= reservas_cancelar
                    break  
                elif reservas_cancelar > reservas:
                    print(f"El numero de cancelación no puede superar las reservas. reservas {reservas}")
                else:
                     print(f"Su numero de reserva no puede ser 0 o menor a 0")
                
            except ValueError:
                print("Debe ser un numero positivo y entero")

        

    
    elif opcion_menu == 4:
        print("Realizadas")
        print(f"el numero de reservas es {reservas}")

    elif opcion_menu == 5:
        print("Gracias por utilizar el sistema Splash World.")
        break

    else:
        print("opcion no valida")

