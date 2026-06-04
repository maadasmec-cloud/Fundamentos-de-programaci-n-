lista_nombres = []


for i in range(3):
    while True:
        nombre = input(f"Ingrese un nombre {i+1}: ")

        if len(nombre) >= 3:
            lista_nombres.append(nombre)
            break

        else:
            print("nombre no cumple con tres caracteres")

nombre_mayor = max(lista_nombres, key= len)


print (f"El nombre mayor es: {nombre_mayor} y tiene {len(nombre_mayor)} letras.")
