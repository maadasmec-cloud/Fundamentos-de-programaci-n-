def buscar_usuario(lista_sistema, nombre):
    for i in range(len(lista_sistema)):
        if lista_sistema[i]['nombre'] == nombre:
            return i
    
    return -1


def guardar_en_lista(lista_sistema, texto_nombre, telefono):
    ficha = {"nombre": texto_nombre, "telefono": telefono}

    lista_sistema.append(ficha)

def contar_telefono(lista_sistema, telefono_buscar):
    
    contador = 0
    
    for i in range(len(lista_sistema)):
        
        if lista_sistema[i] ['telefono'] == telefono_buscar:
            contador += 1
    return contador

def eliminar_usuario (lista_sistema, nombre):
    posicion = buscar_usuario(lista_sistema, nombre)

    if posicion != -1:
        eliminado = lista_sistema.pop(posicion)
        return True
    return False
    

        

mi_archivador = []


guardar_en_lista(mi_archivador, "marco", "1234")
guardar_en_lista(mi_archivador, "Antonio", "4321")
guardar_en_lista(mi_archivador, "pedro", "1234")
guardar_en_lista(mi_archivador, "susan", "5678")

print(mi_archivador)


telefono = input("Ingrese telefono a buscar: ")

print(f"se encontraron {contar_telefono(mi_archivador, telefono)} telefonos iguales a {telefono}")


usuario_eliminar = input("ingrese el nombre del usuario a eliminar: ")

if eliminar_usuario(mi_archivador, usuario_eliminar) == True:

    print(f"se eliminara el usuario: {usuario_eliminar} ")

else:
    print("Error usuario no encontrado")


print(mi_archivador)






lista = ['marco', 'pedro', 'susan', 'leche']

marco_diccionario = {'nombre': 'marco',
                     'edad': '28',
                     'telefono': '2345'}

susan_diccionario = {'nombre': 'susan',
                     'edad': '40',
                     'telefono': '4444'}


lista_con_diccionario = [{'nombre': 'marco', 'telefono': '1234', 'edad': '28' },
                         {'nombre': 'susan', 'telefono': '76688', 'edad': '24'},
                         {'nombre': 'leche', 'telefono': '00009', 'edad': '12'}]

print("esta es la lista: ", lista)
print("este el diccionario: ",marco_diccionario)
print("diccionario de susan: ",susan_diccionario)
print("esta la lista con diccionario ",lista_con_diccionario)

