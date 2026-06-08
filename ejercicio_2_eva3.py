cupos_disponibles = 30
vehiculos_registrados = 0

print("¡Bienvenido al sistema de gestión de cupos del Estacionamiento Corporativo!")

while True:
    try:

        print("1- Cupos disponibles\n2- Registrar vehículo\n3- Retirar vehículo\n4- Historial de ocupaciones\n5- salir")

        
        opcion_menu = int(input("Ingrese una opción del menú: "))

        


        if opcion_menu == 1:
            print(f"Cupos para registrar vehículos disponibles actualmente: {cupos_disponibles} ")
            
        elif opcion_menu == 2:
            while True:
                if cupos_disponibles == 0:
                    print("Ya no quedan cupos disponibles para registrar vehiculos.")
                    break
                try:
                    registrar_vehiculo = int(input("Ingrese cantidad de cupos a registrar: "))
                    if registrar_vehiculo <= 0:
                        print("Cantidad a registrar no puede ser menor o igual a 0.")
                    elif registrar_vehiculo > cupos_disponibles:
                        print("Cantidad a registrar supera cupos disponibles de estacionamiento.")
                    else:
                        print(f"Se registran {registrar_vehiculo} cupos de estacionamiento.")
                        vehiculos_registrados += registrar_vehiculo
                        cupos_disponibles -= registrar_vehiculo
                        break
                except ValueError:
                    print("Valor ingresado es incorrecto. Debe ingresar un numero entero positivo.")

        elif opcion_menu == 3:


            while True:
                if vehiculos_registrados == 0:
                    print("No se puede retirar vehiculo ya que no se han registrado.")
                    break
                try:
                    retirar_vehiculo = int(input("Ingrese cantidad de vehiculos a retirar: "))
                    if retirar_vehiculo <= 0:
                        print("Cantidad a retirar no puede ser menor o igual a 0")
                    elif retirar_vehiculo > vehiculos_registrados:
                        print("Cantidad ingresada supera la cantidad de vheiculos registrados.")
                    else:
                        print(f"Se registra el retiro de {retirar_vehiculo} vehiculos desde el estacionamiento.")
                        cupos_disponibles += retirar_vehiculo
                        vehiculos_registrados -= retirar_vehiculo
                        break
                except ValueError:
                    print("Valor ingresado es incorrecto. Debe ingresar un numero entero positivo.")

        

        elif opcion_menu == 4:
            print(f"Cantidad de vehiculos registrados durante la sesión: {vehiculos_registrados}")

        elif opcion_menu == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break

        else:
            print("opción no valida.")


    except ValueError:
        print("Opción no valida. Debe ser numerico")



