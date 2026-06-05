pesos_paquetes = [12, 45, 60, 23, 85, 38, 41, 9, 50]

carga_pesada = []

for paquete in pesos_paquetes:
    if paquete > 40:
        print(f"Paquete que pesa {paquete} es movido a carga pesada...")
        carga_pesada.append(paquete)



peso_mayor = max(carga_pesada)

carga_pesada.remove(peso_mayor)


carga_pesada.append(peso_mayor - 10)

carga_pesada.sort(reverse=True)


print("Reporte de carga.")

for peso in carga_pesada:

    print(f"Paquete: {peso} KG")