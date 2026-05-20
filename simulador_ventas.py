total_venta = 0
total_con_descuento = 0
while True:
        nombre_producto_vendido = input("ingrese el nombre del producto vendido: ")
        if nombre_producto_vendido == "salir":
                print("Usted esta saliendo del programa...")
                break
        while True:
            try:                                    
                precio_producto_vemdido = int(input(f"ingrese el precio de {nombre_producto_vendido}: "))
                if precio_producto_vemdido <= 0:
                    print(f"el precio de {nombre_producto_vendido} debe ser mayor a 0")
                else:
                    print("precio registrado")
                    total_venta += precio_producto_vemdido
                    break
            except ValueError:
               print("valor incorrecto, intente nuevamente")
if total_venta > 20000:
        print("usted tiene un 10% de descuento")
        total_con_descuento = total_venta *0.90
        print(f"Su total a pagar es ${round(total_con_descuento)}")
else:
        print(f"su total a pagar es ${round(total_venta)}")