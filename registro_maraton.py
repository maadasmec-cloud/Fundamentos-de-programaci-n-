kilometros_registrados = []
for i in range (5):
    while True:
        try:
            kilometros_corridos = float(input(f"Ingrese los kilometros corridos del corredor {i + 1}: "))
            if kilometros_corridos > 0:
                kilometros_registrados.append(kilometros_corridos)
                break
            else:
                print("Numero no puede menor o igual que 0")
        except ValueError:
            print("Debe ingresar un valor numerico")
    if kilometros_corridos < 5 :
        print("Nivel principiante")
    elif kilometros_corridos <= 10:
        print("Nivel Intermedio") 
    else:
        print("Nivel avanzado")
promedio_kilometros = sum(kilometros_registrados) / len(kilometros_registrados)
print(f"El promedio de kilometros es: {promedio_kilometros} ")
print(f"Se guardaron los siguientes registros: ", *kilometros_registrados)