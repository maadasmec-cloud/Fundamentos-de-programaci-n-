try:
    temperatura_alerta = float(input("Ingrese la temperatura de alerta de su horno: "))

    temperatura_advertencia = temperatura_alerta - 5

    
    registro_de_temperatura = 0

    while True:
        
        
        temperatura_actual = float(input("Ingrese temperatura actual de su horno: "))

        if temperatura_actual <= 0:
            print("error de registro, se cierra el programa....")
            break


        elif temperatura_actual > temperatura_advertencia and temperatura_actual < temperatura_alerta:
            print(f"Cuidado su horno alcanzo {temperatura_actual}° es peligroso ALERTA!!")


        elif temperatura_actual > 0 and temperatura_actual < temperatura_alerta:
            print(f"Temperatura actual es {temperatura_actual}° es registrada")
            

        
        else:
            print(f"Su horno alcanzo {temperatura_actual}° Peligro!! horno se detiene")
            break


        registro_de_temperatura+= 1

        
        




    print(f"EL total de registros fue {registro_de_temperatura}")

except ValueError:
    print("Valor debe ser numérico")
