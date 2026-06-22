#=================================
# VALIDACIONES
#=================================
def validar_identificador(identificador):
    return(len(identificador.strip()) > 0)
def validar_meses(meses):
    return (meses > 0)
def validar_costo(costo):
    return costo >= 0


#=================================
# BUSQUEDA
#=================================
def buscar_miembro(lista_miembros, miembro_buscar):
    for i in range(len(lista_miembros)):
        if lista_miembros[i]['identificador'] == miembro_buscar:
            return i
    return -1

#=================================
# AGREGAR
#=================================
def agregar_miembro(lista_miembros):
    while True:
        identificador = input("Ingrese el identificador del miembro: ")
        if buscar_miembro(lista_miembros,identificador) == -1:
            if validar_identificador(identificador):
                break
            else:
                print("Nombre no es valido")
        else:
            print("Registro ya existe")

    while True:
        try:
            meses = int(input("Ingrese cantidad de meses contratados: "))
            if validar_meses(meses):
                break
            else:
                print("Cantidad de meses no valido")
        except ValueError:
            print("Cantidad debe ser un valor numerico")

    while True:
        try:
            costo = int(input("Ingrese el costo base por cada mes: "))
            if validar_costo(costo):
                break
            else:
                print("Cantidad debe ser un numero mayor o igual a 0")
        except ValueError:
            print("Valor ingresado debe ser numerico")

    nuevo_miembro ={
        'identificador': identificador,
        'meses':meses,
        'costo_mensual':costo,
        'premium': False
    }

    lista_miembros.append(nuevo_miembro)
    print("Miembro registrado con exito")


#=================================
# ELIMINAR
#=================================

def eliminar_miembro (lista_miembros):
    if len(lista_miembros) > 0:
        identificador = input("Ingrese identificador del miembro que quiere eliminar: ")
        posicion = buscar_miembro(lista_miembros, identificador)
        if posicion >= 0:
            lista_miembros.pop(posicion)
            print("Miembro eliminado correctamente")
        else:
            print("EL miembro que quiere eliminar no existe")

    else:
        print("LIsta vacia, nada que eliminar")

#=================================
# ACTUALIZAR
#=================================
def actualizar_premium(lista_miembros):
    for miembro in lista_miembros:
        if miembro['costo_mensual'] >= 45000:
            miembro['premium'] = True

        else:
            miembro['premium'] = False

#=================================
# MOSTRAR
#=================================
def mostrar_miembros(lista_miembros):
    actualizar_premium(lista_miembros)
    print("=== HISTORIAL DE MIEMBROS ===")
    for miembro in lista_miembros:
        print(f"Identificador: {miembro['identificador']}")
        print(f"Meses contratados: {miembro['meses']}")
        print(f"Costo mensual: {miembro['costo_mensual']}")
        if miembro['premium'] == True:
            print(f"Pase: PREMIUM")
        else:
            print("Pase: ESTANDAR")

#=================================
# MENU Y OPCIONES
#=================================
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ==========")
    print("1- Agregar miembro")
    print("2- Buscar miembro por identificador")
    print("3- Eliminar miembro")
    print("4- Actualizar planes premium")
    print("5- Mostrar historial de miembros")
    print("6- Salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opcion del menu: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        
        print("Opcion no valida. intente nuevamente")

#=================================
# PRINCIPAL
#=================================

def sistema_principal():
    lista_miembros =[]
    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_miembro(lista_miembros)

        elif opcion == 2:
            if len(lista_miembros) > 0:
                miembro = input("Ingrese el el miembro que busca: ")
                posicion = buscar_miembro(lista_miembros,miembro)
                if posicion >= 0:
                    print(f"miembro se encuentra en el indice: {posicion}")
                    print(f"Identificador: {lista_miembros[posicion]['identificador']}")
                    print(f"Meses contratados: {lista_miembros[posicion]['meses']}")
                    print(f"Costo mensual: {lista_miembros[posicion]['costo_mensual']}")
                else:
                    print("Miembro que busca no existe")
            else:
                print("Lista vacia, nada que buscar")

        elif opcion == 3:
            eliminar_miembro(lista_miembros)
        elif opcion == 4:
            actualizar_premium(lista_miembros)
            print("Miembros actualizados")

        elif opcion == 5:
            mostrar_miembros(lista_miembros)

        elif opcion == 6:
            print("Gracias por usar el sistema del gimnasio. Vuelva pronto.")
            break

if __name__ == "__main__":
    sistema_principal()