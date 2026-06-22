#============================================
#FUCNIONES PRINCIPALES
#============================================
def menu_mostrar():
    print("=== MENÚ PRINCIPAL ==========")
    print("1- Agregar reserva")
    print("2- Buscar reserva por código")
    print("3- Eliminar reserva")
    print("4- Actualizar temporadas altas")
    print("5- Mostrar historial de reservas")
    print("6- Salir")

def opcion_menu():
    while True:
        opcion = (input("Seleccione una opción del menú: "))
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        print ("Opción no valida. Vuelva a intentarlo")

#============================================
#FUCNIONES DE VALIDACIÓN
#============================================
def validar_codigo(codigo):
    return(len(codigo.strip()) > 0)

def validar_dias(dias):
    return (dias > 0)

def validar_precioNoche(precio_noche):
    return(precio_noche >= 0)

#============================================
#FUCNIÓN DE BUSQUEDA
#============================================
def buscar_reserva (lista_reservas, codigo_buscar):
    for i in range(len(lista_reservas)):
        if lista_reservas[i]['codigo'] == codigo_buscar:
            return i
    return -1

#============================================
#FUCNIÓN DE AGREGAR RESERVA
#============================================
def agregar_reserva(lista_reservas):
    while True:
        codigo = input("Ingrese el codigo de la cabaña: ")
        if validar_codigo(codigo):
            if buscar_reserva(lista_reservas, codigo) != -1:
                print("Este registro ya existe")
                return
            break
        else:
            print("Nombre no es valido. Vuelva a intentarlo")
    
    while True:
        try:
            dias = int(input("Ingrese la cantidad de días que durará la estadia: "))
            if validar_dias(dias):
                break
            else:
                print("Cantidad de dias no es valído. Intente nuevamente")

        except ValueError:
            print("Cantidad de días debe ser valor númerico")

    while True:
        try:
            precio_noche = int(input("INgrese el precio asignado por noche: "))
            if validar_precioNoche(precio_noche):
                break
            else:
                print("Precio ingresado no es valido. Intente nuevamente")

        except ValueError:
            print("Precio ingresado debe der de valor númerico")

    registro ={
        'codigo':codigo,
        'dias':dias,
        'precio_noche':precio_noche,
        'temporada_alta':False
    }

    lista_reservas.append(registro)
    print("Se ingreso el nuevo registro con exito")

#============================================
#FUCNIÓN DE ELIMINAR RESERVA
#============================================
def eliminar_reserva(lista_reservas):
    if lista_con_datos(lista_reservas):
        codigo = input("Ingrese el codigo de la reserva que desea eliminar: ")
        posicion = buscar_reserva(lista_reservas, codigo)
        if posicion >= 0:
            lista_reservas.pop(posicion)
            print("Reserva eliminada correctamente")
        else:
            print("Reserva no existe")

    else:
        print("Lista de registos vacias, nada que eliminar")
    

#============================================
#FUCNIÓN LISTA CON DATOS
#============================================
def lista_con_datos(lista_reservas):
    return (len(lista_reservas) > 0)

#============================================
#FUCNIÓN ACTUALIZAR
#============================================
def actualizar_temporada(lista_reservas):
    for codigo in lista_reservas:
        if codigo['precio_noche'] >= 80000:
            codigo['temporada_alta'] = True

#============================================
#FUCNIÓN MOSTRAR
#============================================

def mostrar_registros (lista_reservas):
    print("=== HISTORIAL DE RESERVAS ===")
    actualizar_temporada(lista_reservas)
    for codigo in lista_reservas:
        print(f"Codgio cabaña: {codigo['codigo']}")
        print(f"Dias de estadia: {codigo['dias']}")
        print(f"Precio por noche: {codigo['precio_noche']}")
        
        if codigo['temporada_alta'] == True:
            print(f"Condición : TEMPORADA ALTA")

        else:
            print(f"Condición : ESTANDAR")






def sistema_central():
    lista_reservas = []
    while True:
        menu_mostrar()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_reserva(lista_reservas)

        elif opcion == 2:
            pass

        elif opcion == 3:
            eliminar_reserva(lista_reservas)

        elif opcion == 4:
            actualizar_temporada(lista_reservas)
            print("Se actualizó registro de temporada")

        elif opcion == 5:
            mostrar_registros(lista_reservas)

        elif opcion == 6:
            print("Gracias por usar el sistema del complejo turístico. Vuelva pronto.")
            break



if __name__ == "__main__":
    sistema_central()