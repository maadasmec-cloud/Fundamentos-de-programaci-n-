def menu_mostrar():
    print("=====MENU PRINCIPAL=====")
    print("1- Registrar instrumentos")
    print("2- Consultar instrumento")
    print("3- Ingresar embarque")
    print("4- Vender Instrumento")
    print("5- Mostrar inventario total")
    print("6- Salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opción del menú: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        print("Opcion no valida. Intente nuevamente.")

#=====================================================
#Función de buscar instrumento por modelo
#=====================================================
"""Esta funcion servirá para buscar el instrumento por su tipo ej: guitarra, bajo o bateria"""
def buscar_instrumento(Lista_instrumentos, modelo_buscar):
    for i in range(len(Lista_instrumentos)):
        if Lista_instrumentos[i]['modelo'].lower() == modelo_buscar.lower():
            return i
    return -1

#============================================
#FUnciones de validacion.
#============================================
"""estas funciones validarán que el modelo no sea solo espacios o este vacio
lo mismo para tipo, tambien que la lista tenga algo antes de hacer y buscar,
que stock no sea un numero negativo o precio"""

def validar_nombre(nombre):
    return (len(nombre.strip())> 0)
#esta funcion servirá tanto para tipo como modelo

def validar_stock(stock):
    return(stock >= 0)

def validar_precio(precio):
    return(precio >= 0)

def tiene_instrumento(lista_instrumento):
    return(len(lista_instrumento) > 0)

def validar_cantidad (cantidad):
    return(cantidad > 0)

#===========================
#Funcion vender instrumento
#===========================
"""Aqui debo ejecutar de distinta manera que eliminar por que no quiero eliminar sino descontar,
lo que podria hacer es buscar el diccionario del instrumento que quiere comprar el cliente,
luego en ese diccionario buscar la clave stock y restarle la cantidad que quiere comprar el 
cliente, esto haria que el instrumento siga en el registro pero sin stock si llega su 
stock a 0."""
def vender_instrumento(lista_instrumento):
    if tiene_instrumento(lista_instrumento):
       instrumento = input("Ingrese el modelo del instrumento: ")
       posicion = buscar_instrumento(lista_instrumento,instrumento)
       if posicion >= 0:
           while True:
                try:
               
                    cantidad = int(input("Ingrese la cantidad a vender: "))
                    if validar_cantidad(cantidad):
                            if lista_instrumento[posicion]['stock'] >= cantidad:
                                lista_instrumento[posicion]['stock'] -= cantidad
                                print("Instrumento vendido exitosamente")
                                break
                            else:
                                print("No hay stock para ejecutar la venta")
                    else:
                        print("Cantidad no es valida.")
                except ValueError:
                    print("Cantidad debe ser un valor numerico mayor a 0")
       else:
           print("Producto no registrado")
    else:
        print("Aun no hay registros de instrumentos. Nada que vender.")
#==============================
#Funcion de registrar instrumento
#==============================

def registrar_instrumento(lista_instrumentos):
    while True:
        tipo = input("Ingrese el tipo de instrumento: ")
        if validar_nombre(tipo):
            break
        else:
            print("Tipo de instrumento no es valido. Intente nuevamente.")
    
    while True:
        modelo = input(f"Ingrese el modelo de su instrumento {tipo}: ")
        if validar_nombre(modelo):
            if buscar_instrumento(lista_instrumentos,modelo) >= 0:
                print("Instrumento ya se encuentra registrado")
            else:
                break
        else:
            print("Modelo ingresado no es valido. Intente nuevamente.")

    while True:
        try:
            stock = int(input("Ingrese el stock que ingresará: "))
            if validar_stock (stock):
                break
            else:
                print("Cantidad no es valida. Intente nuevamente.")
        except ValueError:
            print("Dato ingresado no es valido. Debe ser un numero entero intente nuevamente.")

    while True:
        try:
            precio = int(input("Ingrese precio del producto: "))
            if validar_precio(precio):
                break
            else:
                print("Precio no es valido. Intente nuevamente")
        except ValueError:
            print("Dato ingresado debe ser un numero entero. Intente nuevamente.")

    nuevo_instrumento = {
        'tipo': tipo,
        'modelo':modelo,
        'stock':stock,
        'precio':precio,
    }


    lista_instrumentos.append(nuevo_instrumento)
    print("Se agrego el instrumento exitosamente.")


#============================
#Mostrar instrumentos
#============================

def mostrar_instrumentos(lista_instrumentos):
    if tiene_instrumento(lista_instrumentos):
        print("=========LISTA DE INSTRUMENTOS==========")
        for instrumento in lista_instrumentos:
            print(f"Tipo: {instrumento['tipo']}")
            print(f"Modelo: {instrumento['modelo']}")
            print(f"Stock: {instrumento['stock']}")
            print(f"Precio: {instrumento['precio']}")
            print("-------------------------------")

#============================
#Función ingresar embarque
#============================
"""Primero validamos que la lista tenga registros, si tiene pedimos el modelo
que trae el embarque, usamos la función buscar instrumento para guardarlo en la 
variable posicion con el argumento de lista de instrumento y el de instrumento
que nos dio el usario, si la posicion es mayor o igual a 0 quiere decir que 
existe ese modelo y por lo tanto podemos agregarlo, usamos el metodo simple de sumar
en la lista de instrumentos en el indice que nos dio posicion usando la funcion
buscar y asi tenemos acceso al diccionario y luego a la clave 'stock' le sumamos la
cantidad ingresada por el usuario que debe ser mayor a 0"""

def ingresa_embarque(lista_instrumentos):
    if tiene_instrumento(lista_instrumentos):
        instrumento = input("Ingrese el modelo que trae el embarque: ")
        posicion = buscar_instrumento(lista_instrumentos, instrumento)
        if posicion >= 0:
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad: "))
                    if validar_cantidad(cantidad):
                
                        lista_instrumentos[posicion]['stock'] += cantidad
                        print("Se ingreso el embarque")
                        break
                    else:
                        print("Cantidad debe ser mayor a 0")
                except ValueError:
                    print("Valor debe ser un numero entero.")
        else:
            print("No tenemos registro de ese modelo. Debe ingresarlo en la opción 1.")
    else:
        print("Aun no tenemos registros. Ingrese instrumentos en la opción 1.")


def sistema_principal():
    lista_instrumentos = [{'tipo':'bajo','modelo':'jazz','stock':10,'precio':20000}]

    while True:
        menu_mostrar()
        opcion = opcion_menu()

        if opcion == 1:
            registrar_instrumento(lista_instrumentos)

        elif opcion == 2:
            """En esta función lo primero que hacemos es validar si tenemos instrumentos
            registrados, si es asi entramos en la función, le pedimos al cliente el
            tipo de instrumento que busca( guitarra, bajo, piano, etc.) ponemos una bandera
            "encontrado" en False, recorremos la lista de instrumentos con la variable
            instrumento, y si instrumento (variable del ciclo) en la clave 'tipo' es 
            igual a la ingresada al usuario imprimimos todos los instrumentos de ese tipo
            con print(f"Modelo: {instrumento['modelo']} | Precio: {instrumento['precio']} | Stock: {instrumento['stock']}")
            y la bandera encontrado pasa a True, de lo contrario si la bandera nunca cambio
            al final del ciclo y queda en false en la siguiente condicional mostrara el mensaje
            que de esos instrumentos no tenemos."""
            if tiene_instrumento(lista_instrumentos):
                tipo_cliente = input("Que tipo de instrumento busca: ")
                encontrado = False
                for instrumento in lista_instrumentos:
                    if instrumento['tipo'].lower() == tipo_cliente.lower():
                        print(f"Modelo: {instrumento['modelo']} | Precio: {instrumento['precio']} | Stock: {instrumento['stock']}")
                        encontrado = True
                if not encontrado:
                    print("No tenemos instrumentos registrados en esa categoria")

        
        elif opcion == 3:
            ingresa_embarque(lista_instrumentos)

        elif opcion == 4:
            vender_instrumento(lista_instrumentos)
        elif opcion == 5:
            mostrar_instrumentos(lista_instrumentos)
            
            

        elif opcion == 6:
            print("Gracias por usar nuestro servicio. Hasta pronto")
            break
        

    
if __name__ == "__main__":
    sistema_principal()