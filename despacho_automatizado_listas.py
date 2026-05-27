pedidos_entrantes = [12, 15, 8, 20, 5, 14]
estados_pedidos = []
pedidos_rechazados = 0

stock_disponible = 50

for pedidos in pedidos_entrantes:

    if pedidos <= stock_disponible:
        stock_disponible -= pedidos
        estados_pedidos.append("APROBADO")

    else:
        estados_pedidos.append("RECHAZADO")
        pedidos_rechazados += 1



print(f"EL estado de los pedidos es: ", *estados_pedidos)

print(f"El stock disponible al final del dia es: {stock_disponible}")

print(f"pedidos rechazados: {pedidos_rechazados}")