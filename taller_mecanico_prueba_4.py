#=====================================
#MENÚ PRINCIPAL
#=====================================
def menu_mostrar():
    print("=== MENÚ PRINCIPAL ==========")
    print("1- Agregar orden de raparacíon")
    print("2- Buscar orden por patente")
    print("3- Eliminar orden de reparación")
    print("4- Actualizar servicios mayores")
    print("5- Mostrar historial de órdenes")
    print("6- Salir")

#=====================================
# SELECCIÓN DE OPCIÓN DEL MENÚ
#=====================================
def opcion_menu():
    while True:
        opcion = input("Ingrese una opción del menú: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        print("Opcion no válida. Intente nuevamente")

#=====================================
# FUNCIONES DE VALIDACIÓN
#=====================================
#VALIDAR PATENTE NO VACIO Y SOLO ESPACIOS EN BLANCO
def validar_patente(patente):
    return(len(patente.strip()) > 0)

#VALIDAR QUE SEA NUMERO ENTERO IGUAL O MAYOR A 0
def validar_repuestos(repuestos):
    return(repuestos >= 0)

#VALIDAR QUE SEA NUEMRO ENTERO MAYOR QUE 0
def validar_horas(horas):
    return(horas > 0)

#=====================================
# FUNCIÓN DE BUSCAR
#=====================================
#ESTA FUNCIÓN RECORRE LA LISTA DE REGISTROS Y BUSCA COINCIDENCIAS
def buscar_patente(lista_ordenes,patente_buscar):
    for i in range(len(lista_ordenes)):
        if lista_ordenes[i]['patente'] == patente_buscar:
            return i
    return -1

#=====================================
# FUNCIÓN AGREGAR REGISTRO
#=====================================
#ESTA FUNCIÓN ES PARA AGREGAR NUEVOS REGISTROS
def agregar_orden(lista_ordenes):
    while True:
        patente = input("Ingrese la patente: ").strip()
        #valida patente sin solo espacios o vacio
        if validar_patente(patente):
            break
        else:
            print("Nombre de patente no valído")

    while True:
        try:
            #vlaida si repuesto es numero entero mayor o igual a 0
            repuestos = int(input("Ingrese costo de los repuestos: "))
            if validar_repuestos(repuestos):
                break
            else:
                print("Cantidad ingresada no es valido")
        except ValueError:
            print("Valor solo debe ser númerico")

    while True:
        try:
            #valida que horas sea un numero entero mayor a 0
            horas = int(input("Ingrese cantidad de horas de mano de obra: "))
            if validar_horas(horas):
                break
            else:
                print("Horas ingresadas no son valĺidas")
        except ValueError:
            print("Valor solo debe ser númerico")
# aqui se define el diccionario de como se guardara cada orden
    orden = {
        'patente':patente,
        'repuestos':repuestos,
        'horas': horas,
        'servicio_mayor': False
    }
#aqui se guarda la nueva orden en la lista
    lista_ordenes.append(orden)
    print("Orden registrada exitosamente")
        

#=====================================
# FUNCIÓN ELIMINAR REGISTRO
#=====================================
def eliminar_orden(lista_ordenes):
    if len(lista_ordenes) > 0:
        patente = input("Ingrese patente de la orden que quiere eliminar:  ").strip()
        posicion = buscar_patente(lista_ordenes, patente)
        if posicion >= 0:
            lista_ordenes.pop(posicion)
            print("Orden eliminada")
        else:
            print("Orden con esa patente no encontrada")
    else:
        print("lista de ordenes vacia, nada que eliminar")

#=====================================
# FUNCIÓN ACTUALIZAR SERVICIOS MAYORES
#=====================================
def actualizar_servicios(lista_ordenes):
    for orden in lista_ordenes:
        if orden['horas'] >= 10:
            orden['servicio_mayor'] = True
        else:
            orden['servicio_mayor'] = False

#=====================================
# FUNCIÓN MOSTRAR HISTORIAL DE ORDENES
#=====================================
def mostrar_historial(lista_ordenes):
    actualizar_servicios(lista_ordenes)
    print("=== HISTORIAL DE ÓRDENES ===")
    for orden in lista_ordenes:
        print(f"Patente: {orden['patente']}")
        print(f"Costo Repuestos: {orden['repuestos']}")
        print(f"Horas de mano de obra: {orden['horas']}")
        if orden['servicio_mayor'] == True:
            print("Tipo de servicio: MAYOR")
        else:
            print("Tipo de servicio: ESTANDAR")
    
        
def sistema_central ():
    lista_ordenes = []

    while True:


        menu_mostrar()
        
        opcion = opcion_menu()

        if opcion == 1:
            agregar_orden(lista_ordenes)

        elif opcion == 2:
            if len(lista_ordenes) > 0:
                
                patente = input("Ingrese la patente de la orden que busca: ").strip()
                posicion = buscar_patente(lista_ordenes,patente)
                if posicion >= 0:
                    print(f"la posición de su busqueda esta en el indice {posicion}")
                    print(f"Patente: {lista_ordenes[posicion]['patente']}")
                    print(f"Costo de repuestos: {lista_ordenes[posicion]['repuestos']}")
                    print(f"Horas de mano de obra: {lista_ordenes[posicion]['horas']}")
                else:
                    print("La orden con esa patente no se encuentra registrada")
                
            else:
                print("LIsta de ordenes vacia, nada que buscar")

        elif opcion == 3:
            eliminar_orden(lista_ordenes)

        elif opcion == 4:
            if len (lista_ordenes) > 0:
                actualizar_servicios(lista_ordenes)
                print("Servicios mayores actualizados")
            else:
                print("Lista vacia, nada que actualizar")

        elif opcion == 5:
            if len(lista_ordenes) > 0:
              mostrar_historial(lista_ordenes)
            else:
                print("Lista vacia, no existen ordenes para mostrar")
            


        elif opcion == 6:
            print("Gracias por usar el sistema del taller mecánico. Vuelva pronto.")
            break


if __name__ == "__main__":
    sistema_central()