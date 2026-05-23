contador_piloto_novato = 0
contador_piloto_elite = 0

while True:

    print("1-Registrar piloto\n2-Ver datos de registro\n3-salir.")

    try:
        opcion_menu = int(input("ingrese una opción del menú: "))
    except ValueError:
        print("Error. seleccione una opción correcta.")
        continue

    if opcion_menu == 1:
        while True:
            try:
                numero_registros = int(input("Ingrese cantidad de registros: "))
                if numero_registros > 0:
                    break
                else:
                    print("Cantidad debe ser mayor a 0")
            except ValueError:
                print ("Error. ingrese una cantidad valida")
        for i in range(numero_registros):
            print(f"registro del piloto numero {i+1} de un total de {numero_registros}")
            while True:
                    nombre_cadete = input("Ingrese el nombre del cadete: ")
                   

                    if len(nombre_cadete) < 6 or " " in nombre_cadete:
                        print("Nombre no valido. Debe contener 6 letras como minimo")

                    else:
                        break

            while True:
                try:
                    horas_vuelo = int(input("Ingrese horas de vuelo del piloto: "))
                    if horas_vuelo < 0:
                        print("Error. no puede ser menos de 0")
                    elif horas_vuelo > 500:
                        print("Piloto Élite")
                        contador_piloto_elite += 1
                        break

                    elif horas_vuelo <= 500:
                        print("Piloto Novato")
                        contador_piloto_novato += 1
                        break
                except ValueError:
                    print("Error. Dato ingresado no valido")

    elif opcion_menu == 2:
        print(f"Cantidad de pilotos novatos {contador_piloto_novato}")
        print(f"Cantidad de pilotos Élites {contador_piloto_elite}")

    elif opcion_menu == 3:
        print("saliendo del programa...")
        break

    else:
        print("Opción ingresada no valida")