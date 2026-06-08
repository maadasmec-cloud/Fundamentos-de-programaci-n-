temperaturas_racks = [28, 36, 42, 31, 39, 29, 45, 33, 37]
alertas = []

for temperatura in temperaturas_racks:
    if temperatura > 35:
        print(f"Temperatura {temperatura} registrada en alertas")
        alertas.append(temperatura)


temp_alta = max(alertas)

alertas.remove(temp_alta)

alertas.sort(reverse=True)

print("--"*50)
print("Reportes de alerta")

for temp in alertas:
    print(f"Temperatura: {temp} grados celcius")