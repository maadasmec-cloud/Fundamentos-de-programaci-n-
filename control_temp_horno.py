while True:
    try:
        temperatura_alerta = float(input("Ingrese la temperatura de alerta de su horno: "))
        if temperatura_alerta < 0 or temperatura_alerta > 0:
            break
    except ValueError:
        print("Valor debe ser numerico. intente nuevamente")

temperatura_advertencia = temperatura_alerta - 5


registro_de_temperatura = 0

while True:
    
    try:
        temperatura_actual = float(input("Ingrese temperatura actual de su horno: "))
        if temperatura_actual <= 0:
            print("Temperatura debe ser un numero positivo")

        else:

            if temperatura_actual > temperatura_alerta:
                print(f"Temperatura actual ingresada {temperatura_actual} sobrepasa la temperatura de alerta {temperatura_alerta} PELIGRO!! horno se detiene")
                break
    
            elif temperatura_actual >= temperatura_advertencia:
                print(f"Cuidado su horno alcanzo {temperatura_actual}° es peligroso ALERTA!!")


            else: 
                print(f"Temperatura actual es {temperatura_actual}° es registrada")
            
            

            
            registro_de_temperatura+= 1

    except ValueError:
        print("Valor debe ser numerico. intente nuevamente")

        
        




print(f"EL total de registros fue {registro_de_temperatura}")


