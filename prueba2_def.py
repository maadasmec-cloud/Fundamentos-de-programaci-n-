def validad_correo (correo):
    if "@" in correo:
        return True
    
    return False


def validad_numero(numero):
    if len(numero) == 9 and numero[0] == "9":
        return True
    return False


def validacion_edad(edad):
    if edad < 18:
        return False
    return True


correo= input("Ingrese correo: ")

if validad_correo(correo) == True:
    print("Correo valido")

else:
    print("Correo no valido")

numero = input("Ingrese numero: ")

if validad_numero(numero) == True:
    print("Numero correcto")
else:
    print("numero no valido")

edad = int(input("Ingrese su edad: "))

if validacion_edad(edad)== True:
    print("usted es mayor de edad")
else:
    print("Usted es menor de edad")


