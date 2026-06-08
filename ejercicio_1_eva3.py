productos_premium = 0
productos_estandar = 0


while True:
    try:
        cantidad_registros = int(input("Ingrese la cantidad de productos que registrará: "))
        if cantidad_registros > 0:
            break
        else:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

for i in range(cantidad_registros):
    while True:
        codigo_sku = input("Ingrese el código SKU del producto: ")
        if len(codigo_sku) < 6 or " " in codigo_sku:
            print("Código incorrecto. Debe tener al menos 6 caracteres y no incluir espacios.")
        
        else:
            break

    while True:
        try:
            valor_unitario_producto = int(input("Ingrese el valor unitario del producto: "))
            if valor_unitario_producto > 0:
                break
            else:
                print("¡Error de valoración! Ingresa un número entero positivo para el valor unitario.")
        except ValueError:
            print("¡Error de valoración! Ingresa un número entero positivo para el valor unitario.")


    if valor_unitario_producto > 75000:
        productos_premium += 1

    else:
        productos_estandar += 1


print(f"¡El almacén cuenta con {productos_premium} productos Premium y {productos_estandar} productos Estándar! ¡Distribución lista!")




    



