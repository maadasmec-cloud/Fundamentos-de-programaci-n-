def calcular_iva(p):
    iva = p * 0.19
    return iva

precio_compra = float(input("Ingrese el valor de la compra: "))

iva = calcular_iva(precio_compra)

print(f"el valor de la compra sin iva: ", precio_compra)

print(f"El valor a pagar con el iva incluido es de: ", precio_compra + iva)