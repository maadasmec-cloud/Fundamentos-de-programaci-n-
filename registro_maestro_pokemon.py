contador_maestro = 0
contador_novato = 0
while True:
    print("1.registro pokemon\n2.Visualización de datos\n3.Salir")
    try:
        menu =  int(input("Ingrese una opción: "))
    except ValueError:
        print("opcion incorrecta, debe ingresar un numero ")
        continue

    if menu == 1:
        while True:
            try:
                cantidad_entrenadores = int(input("Ingrese cantidad de entrenadores a registrar: "))
                if cantidad_entrenadores > 0:
                    break
                else:
                    print("cantidad invalida. Debe ingresar un entero positivo")
            except ValueError:
                print("cantidad invalida. Debe ingresar un numero entero positivo.")
        for i in range(cantidad_entrenadores):
             print(f"registrando entrenador {i + 1} de {cantidad_entrenadores} entrenadores")

             while True:
                  nombre_original = input("nombre del entrenador: ")
                  nombre_con_mayusculas = nombre_original.title()#pone en mayus la primeras letras ej(MarcoAdasme)
                  nombre_entrenador = nombre_con_mayusculas.replace(" ","")#remplaza espacio " " por nada ""
                  if len(nombre_entrenador) < 6:
                       print("Nombre invalida. intente nuevamente")
                  else:
                       break
             while True:
                  try:
                       medallas = int(input("Cantidad de medallas: "))
                       if medallas >= 0:
                            break
                       else:
                            print("Cantidad no valida, debe ser entero positivo")
                  except ValueError:
                       print("Dato ingresado no es valid")

             if medallas > 8:
                  print(f"{nombre_entrenador} es un maestro Pokemon")
                  contador_maestro += 1
             else:
                  print(f"{nombre_entrenador} es un entrenador novato")
                  contador_novato += 1
         
                        
         
        


    elif menu == 2:
         print("Ver datos")
         print(f"el total de maestros pokemon son {contador_maestro}")
         print(f"El total maestros novatos pokemon es {contador_novato}")

    elif menu == 3:
         print("Saliendo del programa...")
         break

    else:
         print("Opcion incorrecta")

                                        
                                     
print("Hasta pronto")

                
               

            