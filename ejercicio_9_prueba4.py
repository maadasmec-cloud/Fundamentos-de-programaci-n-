#==============================
#FUNCIONES PRINCIPALES DE MENU
#=============================
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ==========")
    print("1. Agregar pasaje")
    print("2. Buscar pasaje por código de vuelo")
    print("3. Eliminar pasaje")
    print("4. Actualizar vuelos internacionales")
    print("5. Mostrar historial de pasajes")
    print("6. Salir")
def opcion_menu():
    while True:
        opcion = input("Ingrese una opcion del menu: ")
        if opcion in ['1','2','3','4','5','6']:
            return int (opcion)
        print("Opcion no valida. intente nuevamente")

#==============================
#FUNCIONES  DE VALIDACIÓN
#==============================
def validar_codigo(codigo):
    return(len(codigo.strip()) > 0)
def validar_asientos(asientos):
    return (asientos > 0)
def validar_precio_asiento(precio_asiento):
    return(precio_asiento >= 0)
def validar_lista_con_registros(lista_con_registro):
    return(len(lista_con_registro) > 0)

#==============================
#FUNCIONES DE BUSQUEDA
#==============================
def buscar_registro(lista_registros,registro_buscar):
    for i in range(len(lista_registros)):
        if lista_registros[i]['codigo'] == registro_buscar:
            return i
    return -1

#==============================
#FUNCIONES DE ELIMINAR
#==============================
def eliminar_registro(lista_registros):
    if validar_lista_con_registros(lista_registros):
        codigo = input("Ingrese el codigo del registro que quiere eliminar: ").strip()
        posicion = buscar_registro(lista_registros,codigo)
        if posicion >= 0:
            lista_registros.pop(posicion)
            print("Registro eliminado exitosamente")
        else:
            print("Registro con ese codigo no encontrado")
    else:
        print("Lista vacia, nada que eliminar")

#==============================
#FUNCIONES DE AGREGAR
#==============================
def agregar_registro(lista_registros):
    while True:
        codigo = input("Ingrese el codigo: ").strip()
        if validar_codigo(codigo):
            posicion = buscar_registro(lista_registros, codigo)
            if posicion >= 0:
                print("Registro ya existe")
                
            else:
                break
        else:
            print("Codigo no valido")
    while True:
        try:
            asientos = int(input("Ingrese la cantidad de asientos comprados: "))
            if validar_asientos(asientos):
                break
            else:
                print("Cantidad ingresada no es valida")
        except ValueError:
            print("Valor a ingresar debe ser numerico")

    while True:
        try:
            precio_asiento = int(input("Ingrese el costo base por cada asiento: "))
            if validar_precio_asiento(precio_asiento):
                break
            else:
                print("Precio ingresado no es valido")
        except ValueError:
            print("Valor a ingresar debe ser numerico")

    registro = {
        'codigo': codigo,
        'asientos': asientos,
        'precio_asiento': precio_asiento,
        'internacional': False
        }
    lista_registros.append(registro)
#==============================
#FUNCION DE ACTUALIZAR
#==============================
def actualizar_registros(lista_registros):
    if validar_lista_con_registros(lista_registros):
        for registro in lista_registros:
            if registro['precio_asiento'] >= 150000:
                registro['internacional'] = True
            else:
                registro['internacional'] = False
    else:
        print("Lista vacia. Nada que actualizar")

#==============================
#FUNCION DE MOSTAR
#==============================
def mostrar_registros(lista_registros):
    if validar_lista_con_registros(lista_registros):
        actualizar_registros(lista_registros)
        print("=== HISTORIAL DE PASAJES ===")
        for registro in lista_registros:
            print(f"Codigo Vuelo: {registro['codigo']}")
            print(f"Asientos: {registro['asientos']}")
            print(f"Precio por asiento: {registro['precio_asiento']}")
            if registro['internacional'] == True:
                print("Destino: INTERNACIONAL")
            else:
                print("Destino: NACIONAL")
            print("**" *30)

#==============================
#FUNCION PRINCIPAL
#==============================

def sistema_principal():
    lista_registros = []
    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_registro(lista_registros)

        elif opcion == 2:
            if validar_lista_con_registros(lista_registros):
                codigo = input("Ingrese el codigo del registro que busca: ").strip()
                posicion = buscar_registro(lista_registros,codigo)
                if posicion >= 0:
                    print(f"Su registro esta en el indice: {posicion}")
                    print("========REGISTRO ENCONTRADO=========")
                    print(f"Codigo: {lista_registros[posicion]['codigo']}")
                    print(f"Asientos: {lista_registros[posicion]['asientos']}")
                    print(f"Precio por asiento: {lista_registros[posicion]['precio_asiento']}")
                else:
                    print("Registro que busca no existe.")

            else:
                print("Lista vacia. Nada que buscar")

        elif opcion == 3:
            eliminar_registro(lista_registros)

        elif opcion == 4:
            if validar_lista_con_registros(lista_registros):
                actualizar_registros(lista_registros)
                print("Registros actualizados")
            else:
                print("No hay registros que actualizar")

        elif opcion == 5:
            if validar_lista_con_registros(lista_registros):
               mostrar_registros(lista_registros)
            else:
                print("No hay registro para mostar")
        elif opcion == 6:
            print("Gracias por usar el sistema de la aerolínea. Vuelva pronto.")
            break

if __name__ == "__main__":
    sistema_principal()
