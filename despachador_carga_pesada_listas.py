pesos_paquetes = [45, 120, 80, 95, 110, 30, 105, 70]

cargas_aceptadas = []
cargas_retenidas = []

peso_aceptado = 0


for carga in pesos_paquetes:
    if carga > 100:
        cargas_retenidas.append(carga)

    else:
        cargas_aceptadas.append(carga)
        peso_aceptado += carga


print(f"Cargas retenidas: ",*cargas_retenidas)

print(f"Cargas aceptadas: ",*cargas_aceptadas)

print(f"Kilos totales que llevará el camión: {peso_aceptado}")