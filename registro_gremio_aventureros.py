aventureros_veteranos = 0
aventureros_novatos = 0


while True:

    try:
        cantidad_aventureros = int(input("Ingrese cantidad de aventureros a registrar: "))
        if cantidad_aventureros > 0:
            break
        else:
            print("Cantidad inválida. Debe ingresar un entero positivo.")
    except ValueError:
        print("Cantidad inválida. Debe ingresar un entero positivo.")



for i in range(cantidad_aventureros):
    while True:
        nombre_aventurero = input(f"Ingrese el nombre del aventurero {i+1} del registro: ")
        if len(nombre_aventurero) < 6 or " " in nombre_aventurero:
            print("Nombre inválido. Intente nuevamente.")
        else:
            break


    while True:
        try:
            numero_misiones = int(input("Ingrese número de misiones completadas: "))
            if numero_misiones > 0:
                break
            else:
                print("Cantidad inválida. Debe ingresar un entero positivo.")
        except ValueError:
            print("Cantidad inválida. Debe ingresar un entero positivo.")

    if numero_misiones > 15:
        aventureros_veteranos += 1
        print("Se registra un aventuraro Veterano")

    elif numero_misiones <= 15:
        aventureros_novatos += 1
        print("Se registra un aventurero Novato")



print(f"Se registraron {aventureros_veteranos} Aventureros Veteranos e {aventureros_novatos} Aventureros Novatos.")


            
    