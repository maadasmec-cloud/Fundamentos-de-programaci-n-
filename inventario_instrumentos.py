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

#===========================
#Funcion vender instrumento
#===========================
"""Esta funcion busca el producto usando la funcion buscar instrumento
luego lo saca o elimina de la lista con .pop()"""

def vender_instrumento(lista_instrumento):
    if tiene_instrumento(lista_instrumento):
        instrumento = input("Ingrese modelo del instrumento a vender: ")
        posicion = buscar_instrumento(lista_instrumento, instrumento)
        if posicion >= 0:

            print("La venta del instrumento se ejecuto exitosamente.")
        else:
            print("EL instrumento no se encuentra disponible.")

        cantidad = int(input("Cuantos comprará: "))
        if lista_instrumento[posicion]['stock'] <= cantidad:
            lista_instrumento.pop(posicion['stock'])
            print("Venta exitosa")
        else:
            print("Stock no disponible para esta compra")
    
    else:
        print("En este momento nos encontramos sin stock de instrumentos.")
        

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





def sistema_principal():
    lista_instrumentos = []

    while True:
        menu_mostrar()
        opcion = opcion_menu()

        if opcion == 1:
            registrar_instrumento(lista_instrumentos)

        elif opcion == 2:
            pass
        
        elif opcion == 3:
            pass

        elif opcion == 4:
            vender_instrumento(lista_instrumentos)
        elif opcion == 5:
            mostrar_instrumentos(lista_instrumentos)
            
            

        elif opcion == 6:
            print("Gracias por usar nuestro servicio. Hasta pronto")
            break
        

    
if __name__ == "__main__":
    sistema_principal()