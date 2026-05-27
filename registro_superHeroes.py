heroe_legendario = 0
heroe_entrenamiento = 0

while True:

    try:
        cantidad_heroes = int(input("ingrese la cantidad de heroes a registrar: "))
        if cantidad_heroes > 0:
            break
        else:
            print("Cantidad inválida. Debe ingresar un entero positivo.")

    except ValueError:
        print("Cantidad inválida. Debe ingresar un entero positivo.")

for i in range(cantidad_heroes):
    while True:
        nombre_heroe = input(f"Ingrese nombre del heroe numero {i + 1}: ")
        if len(nombre_heroe) < 7 or " " in nombre_heroe:
            print("Alias inválido. Intente nuevamente.")
        else:
            break

    while True:
        try:
            nivel_poder = int(input(f"Ingrese nivel de poder del heroe {i+1}: "))

            if nivel_poder >= 90:
               
                heroe_legendario += 1
                break

            elif nivel_poder > 0 and nivel_poder < 90:
                
                heroe_entrenamiento += 1
                break

            else:
                print("Nivel inválido. Debe ingresar un entero positivo.")
        except ValueError:
            print("Nivel inválido. Debe ingresar un entero positivo.")

    
        
print(f"Se registraron {heroe_legendario} Héroe(s) Legendario(s) y {heroe_entrenamiento} Héroe(s) en Entrenamiento.")

            

        

    