cinta_transportadora = ["S", "M", "L", "S", "L", "M", "M", "S"]

cajas_grandes = 0

cajas_traducidas = []


for caja in cinta_transportadora:

    if caja == "S":
        cajas_traducidas.append("CHICA")

    elif caja == "M":
        cajas_traducidas.append("MEDIANA")

    else:
        cajas_traducidas.append("GRANDE")
        cajas_grandes += 1


print(f"Lista de cajas traducidas: ", *cajas_traducidas)

print(f"Total de cajas grandes: {cajas_grandes}")




