helicopteros_disponibles = 3
combustible_total = 1000
personas_rescatadas = 0

while True:

    print("1-Ver estado de la base\n2-Iniciar misión de rescate\n3-Finalizar misión\n4-Ver total rescatados\n5-Cerrar sistema")

    try:
        opcion_menu = int(input("Ingrese opción del menú: "))
    except ValueError:
        print("Error. Debe ingresar un numero entero positivo")
        continue

    if opcion_menu == 1:
        print(f"La base actualmente tiene {helicopteros_disponibles} helicopteros disponibles y {combustible_total} litros de combustible")

    elif opcion_menu == 2:
        
            if combustible_total < 200:
                print("No queda combustible suficiente")
                

            elif helicopteros_disponibles <= 0:
                print ("No hay helicopteros disponibles")
                

            else:
                while True:
                        try:
                            personas_rescatar = int(input("Ingrese cuantas personas se rescatan: "))
                            if personas_rescatar > 0 and personas_rescatar <= 4:
                                helicopteros_disponibles -= 1
                                combustible_total -= 200
                                personas_rescatadas += personas_rescatar
                                print(f"Se registra el rescate de {personas_rescatar} personas")
                                break

                            else:
                                print("Cantidad de personas no válida.")
                        

                        except ValueError:
                            print("Error. Debe ingresar un numero entero positivo")

    elif opcion_menu == 3:
        
            if helicopteros_disponibles >= 3:
                print("Error: Todos los helicópteros ya están en la base.")
                

            else:
                while True:
                            try:
                                combustible_vuelta = int(input("Ingrese el combustible que trae de vuelta: "))
                                if combustible_vuelta < 0:
                                    print("Debe ser un numero entero")

                                elif combustible_vuelta > 200:
                                    print("No puede devolver mas de lo que se llevo")

                                else:
                                    print(f"Se registra la devolución de {combustible_vuelta} litros de combustible")
                                    helicopteros_disponibles += 1
                                    combustible_total += combustible_vuelta
                                    break
                            except ValueError:
                                print ("Error. Debe ingresar un numero entero positivo")

    elif opcion_menu == 4:
        print (f"personas total rescatadas:  {personas_rescatadas}")


    elif opcion_menu == 5:
        print("Saliendo del sistema....")
        break

                    




    