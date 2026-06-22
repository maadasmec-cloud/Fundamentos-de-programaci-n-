#===========================
#VALIDACIONES
#===========================
def validar_codigo(codigo):
    return(len(codigo.strip()) > 0)

def validar_peso(peso):
    return(peso > 0)

def validar_distancia(distancia):
    return (distancia >= 0)

#===========================
#FUNCIÓN DE BUSQUEDA
#===========================
def buscar_registro(lista_registros, registro_buscar):
    for i in range(len(lista_registros)):
        if lista_registros[i]['codigo'] == registro_buscar:
            return i
    return -1

#===========================
#FUNCIÓN DE AGREGAR REGISTRO
#===========================
def agregar_registro(lista_registros):
    while True:
        codigo = input("Ingrese el codigo a registrar: ")
        if validar_codigo(codigo):
            break
        else:
            print("Codigo invalido. Intente nuevamente")

    while True:
        try:
            peso = int(input("Ingrese el peso del paquete: "))
            if validar_peso(peso):
                break
            else:
                print("Peso no valido. intente nuevamente")
        except ValueError:
            print("Valor ingresado debe ser nuerico")

    while True:
        try:
            disctancia = int(input("Ingrese l distancia a recorrer del envio: "))
            if validar_distancia(disctancia):
                break
            else:
                print("Distancia ingresada no es valida. Intente nuevamente")
        except ValueError:
            print("Valor ingresado debe ser numerico")

    
    nuevo_registro = {
        'codigo':codigo,
        'peso':peso,
        'distancia':disctancia,
        'larga_distancia': False
    }
    lista_registros.append(nuevo_registro)
    print("Registro guardado exitosamente")

#===========================
#FUNCIÓN DE ELIMINAR REGISTRO
#===========================
def eliminar_registro(lista_registro):
    codigo = input("Ingrese el codigo del registro que desea eliminar: ")
    posicion = buscar_registro(lista_registro,codigo)
    if posicion >= 0:
        lista_registro.pop(posicion)
        print("Registro eliminado exitosamente")
    else:
        print("No existe ese registro")

#===========================
#FUNCIÓN DE ACTUALIZAR REGISTRO
#===========================
def actualizar_registro(lista_registros):
    for registro in lista_registros:
        if registro['distancia'] >= 200:
            registro['larga_distancia'] = True
        else:
            registro['larga_distancia'] = False

#===========================
#FUNCIÓN DE MOSTRAR REGISTRO
#===========================
def mostrar_registros(lista_registros):
    actualizar_registro(lista_registros)
    print("=== HISTORIAL DE ENVÍOS ===")
    for registro in lista_registros:
        print(f"Código Seguimiento: {registro['codigo']}")
        print(f"peso (Kg): {registro['peso']}")
        print(f"Distancia (km): {registro['distancia']}")
        if registro['larga_distancia'] == True:
            print("Tipo de Ruta: LARGA DISTANCIA")
        else:
            print("Tipo de Ruta: ESTÁNDAR")
#===========================
#FUNCIÓN DE MENU REGISTRO
#===========================
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ==========")
    print("1. Agregar envío")
    print("2. Buscar envío por código")
    print("3. Eliminar envío")
    print("4. Actualizar envíos de larga distancia")
    print("5. Mostrar historial de envíos")
    print("6. Salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opcion del menu: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        print("Opcion no valida. Intente nuevamente")


#===========================
#FUNCIÓN PRINCIPAL
#===========================

def sistema_principal():
    lista_registros =[]
    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_registro(lista_registros)

        elif opcion == 2:
            registro = input("Ingrese el codigo del registro que busca: ")
            posicion = buscar_registro(lista_registros, registro)
            if posicion >= 0:
                print(f"El registro esta en el indice: {posicion}")
                print(f"Codigo: {lista_registros[posicion]['codigo']}")
                print(f"peso: {lista_registros[posicion]['peso']}")
                print(f"Distancia: {lista_registros[posicion]['distancia']}")
            
        elif opcion == 3:
            eliminar_registro(lista_registros)

        elif opcion == 4:
            actualizar_registro(lista_registros)
            print("registros actualizados")

        elif opcion == 5:
            mostrar_registros(lista_registros)

        elif opcion ==6:
            print("Gracias por usar el sistema de logística. Vuelva pronto.")
            break
    
if __name__ == "__main__":
    sistema_principal()