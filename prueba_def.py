def calcular_costo_envio (peso_paquete, pais_destino, es_cliente_vip):
    cobro_usa = 10
    cobro_espana = 15
    cobro_argentina = 12
    descuento_vip = 20
    

    if pais_destino== "USA":
        
        precio_final = peso_paquete * cobro_usa
    
    elif pais_destino == "ESPAÑA":
        precio_final = peso_paquete * cobro_espana
   
    elif pais_destino== "ARGENTINA":
        precio_final = peso_paquete * cobro_argentina
    
    else:
        return "destino no disponible"
    
    if es_cliente_vip == True:
        total_descuento = descuento_vip / 100
        total_con_descuento = precio_final * total_descuento
        final_vip = precio_final - total_con_descuento
        return f"ustded tiene un descuento del {descuento_vip}% por ser vip,  total a pagar final ${final_vip}"
    
        

    return f"su pauqeter va a {pais_destino}. tarifa normal. total pagar {precio_final}"
    
    

while True:
    try:
        peso_paquete = float(input("ingrese el peso de su paquete: "))
        if peso_paquete <= 0:
            print("EL peso debe ser mayor a 0")
        else:
            break
    except ValueError:
        print("El valor ingresado debe ser numerico.")


pais_destino = input("Ingrese pais de destino: ").upper()


es_vip = input("EL Cliente es bip ?: ").upper()
es_cliente_vip = False
if es_vip == "SI":
    es_cliente_vip = True
    



print(calcular_costo_envio(peso_paquete, pais_destino, es_cliente_vip))

print(f" {peso_paquete} {pais_destino} {es_cliente_vip}")