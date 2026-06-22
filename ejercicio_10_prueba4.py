def mostrar_menu():
    print("=== MENÚ PRINCIPAL ==========")
    print("1- Agregar reserva")
    print("2- Buscar reserva por código de cancha")
    print("3- Eliminar reserva")
    print("4- Actualizar horarios estelares")
    print("5- Mostrar historial de reservas")
    print("6- Salir")

def opcion_menu():
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion in ['1','2','3','4','5','6']:
            return int(opcion)
        print("Opción no válida. Intente nuevamente.")

def buscar_reserva(lista_reservas,reserva_buscar):
    for i in range(len(lista_reservas)):
        if lista_reservas[i]['codigo'].lower() == reserva_buscar.lower():
            return i
        
    return -1

def validar_codigo(codigo):
    return(len(codigo.strip()) > 0)
def validar_horas (horas):
    return (horas > 0)
def validar_valor_hora(valor_hora):
    return(valor_hora >= 0)
def validar_lista_con_reservas(lista_reservas):
    return(len(lista_reservas) > 0)
def agregar_reserva(lista_reservas):
    while True:
        codigo = input("Ingresa el codigo de la reserva: ")
        if validar_codigo(codigo):
            if buscar_reserva(lista_reservas, codigo) >= 0:
                print("Ya existe una reserva con ese codigo")
            else:
                break
        else:
            print("Codigo no valido")

    while True:
        try:
            horas = int(input("Ingrese cantidad de horas de la reserva: "))
            if validar_horas(horas):
                break
            else:
                print("Cantidad de horas ingresadas no validas")
        except ValueError:
            print("Cantidad debe ser en valor numerico")

    while True:
        try:
            valor_hora = int(input("Ingrese el costo base asigando por cada hora: "))
            if validar_valor_hora(valor_hora):
                break
            else:
                print("valor por hora ingresado no es valido")
        except ValueError:
            print("El valor ingresado debe ser nuerico")

    nuevo_registro = {
        'codigo': codigo.strip().title(),
        'horas': horas,
        'valor_hora': valor_hora,
        'horario_estelar': False
    }

    lista_reservas.append(nuevo_registro)
    print("Nuevo registro guardado exitosamente")

def eliminar_registro(lista_reservas):
    if validar_lista_con_reservas(lista_reservas):
        codigo = input("Ingresa codigo se reserva a eliminar: ")
        posicion = buscar_reserva(lista_reservas, codigo)
        if posicion >= 0:
            lista_reservas.pop(posicion)
            print("Se elimino el registro exitosamente")
        else:
            print("El registro con ese codigo no existe")
    else:
        print("Lista vacia. Nada que eliminar.")

def actualizar_reservas(lista_reservas):
        for reserva in lista_reservas:
            if reserva['valor_hora'] >= 25000:
                reserva['horario_estelar'] = True
            else:
                reserva['horario_estelar'] = False
   
def mostrar_reservas(lista_reservas):
    if validar_lista_con_reservas(lista_reservas):
        actualizar_reservas(lista_reservas)
        print("=== HISTORIAL DE RESERVAS ===")
        for reserva in lista_reservas:
            print(f"Codigo Cancha: {reserva['codigo']}")
            print(f"Horas: {reserva['horas']}")
            print(f"Valor por hora: {reserva['valor_hora']}")
            if reserva['horario_estelar'] == True:
                print("Horario: ESTELAR")
            else:
                print(f"Horario: ESTÁNDAR")
            print("========================")
    else:
        print("Lista vacia nada que mostrar")

def sistema_principal():
    lista_reservas = []
    while True:
        mostrar_menu()
        opcion = opcion_menu()

        if opcion == 1:
            agregar_reserva(lista_reservas)
        elif opcion == 2:
            if validar_lista_con_reservas(lista_reservas):
                codigo = input("Ingrese el codigo de la reserva que busca: ")
                posicion = buscar_reserva(lista_reservas, codigo)
                if posicion >= 0:
                    print(f" La reserva esta en en el indice: {posicion}")
                    print(f"Codgio cancha: {lista_reservas[posicion]['codigo']}")
                    print(f"Horas: {lista_reservas[posicion]['horas']}")
                    print(f"Valor por hora: {lista_reservas[posicion]['valor_hora']}")
                else:
                    print("Reserva no encontrada.")
            else:
                print("Lista vacia. Nada que buscar.")
        elif opcion == 3:
            eliminar_registro(lista_reservas)

        elif opcion == 4:
            if validar_lista_con_reservas(lista_reservas):
                actualizar_reservas(lista_reservas)
                print("Reservas actualizadas.")
            else:
                print("Lista vacia, Nada que actualizar.")

        elif opcion == 5:
            mostrar_reservas(lista_reservas)

        elif opcion == 6:
            print("Gracias por usar el sistema del club deportivo. Vuelva pronto.")
            break



if __name__ == "__main__":
    sistema_principal()