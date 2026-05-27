productos_aprobados = 0
productos_rechazados = 0
contador = 0

revision_ugente = []

productos = ["APROBADO", "RECHAZADO", "APROBADO", "EN_ESPERA", "APROBADO", "RECHAZADO", "EN_ESPERA", "APROBADO"]

for control in productos:
    contador += 1
    if control == "APROBADO":
        productos_aprobados += 1
    elif control == "RECHAZADO":
        productos_rechazados += 1
        revision_ugente.append(contador)



print(f"Productos aprobados: {productos_aprobados}")

print(f"Productos rechazados: {productos_rechazados}")

print(f"Lugar de los productos rechazados:", *revision_ugente)
        