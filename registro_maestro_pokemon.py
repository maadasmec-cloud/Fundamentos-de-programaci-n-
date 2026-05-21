contador_maestro = 0
contador_novato = 0
while True:
    print("1.registro pokemon\n2.Visualización de datos\n3.Salir")

    menu =  int(input("Ingrese una opción: "))

    if menu == 1:
        while True:
                
                    cantidad_entrenadores = int(input("Cantidad de entrenadores a registrar: "))
                    if cantidad_entrenadores > 0 :
                        for i in range (cantidad_entrenadores):
                            print(f"entrenador pokemon numero {i+1} registrado")
                            while True:
                                 nombre_entrenador = input("Ingrese el nombre del entrenador: ")
                                 if len(nombre_entrenador) < 6:
                                      print("Debe tener 6 letras minimo")
                                 elif nombre_entrenador.strip() .isspace():
                                      print("No debe tener espacios")

                                 else:
                                      while True:
                                       
                                            cantidad_medallas = int(input("ingrese su cantidad de medallas: "))
                                            if cantidad_entrenadores >= 8:
                                                
                                            
                                            

                                        

                
               

            