dias_mayor = 0
suma_temperaturas = 0
cantidad_dias = 0

temperaturas = [28, 31, 25, 33, 22, 30, 26]

for dias in temperaturas:
    suma_temperaturas += dias
    cantidad_dias += 1

    if dias > 28:
        dias_mayor +=1




print(f"Total de dias con temperaturas mayor a 28 fue: {dias_mayor}")
print(f"La suma de todas las temperaturas da: {suma_temperaturas}")
print(f"Cantidad de dias que se tomo la temperatura: {cantidad_dias}")

promedio_temperatura = suma_temperaturas / cantidad_dias

print(f"{promedio_temperatura:.3f}")