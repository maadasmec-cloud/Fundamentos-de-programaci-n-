hacker_leyenda = 0
hacker_principiante = 0

while True:
    try:
        cantidad_registros = int(input("Ingrese cantidad de candidatos a registrar: "))
        if cantidad_registros > 0:
            break
        else:
            print("Cantidad inválida. Debe ingresar un entero positivo.")
    except ValueError:
        print("Cantidad inválida. Debe ingresar un entero positivo.")


for i in range(cantidad_registros):
    while True:
        nombre_candidato = input(f"Ingrese el Alias en la red del candidato {i+ 1} de {cantidad_registros}: ")
        if len(nombre_candidato) < 6 or " " in nombre_candidato:
            print("Nombre inválido. Intente nuevamente.")
        else:
            break

    while True:
        try:
            experiencia = int(input(f"Ingrese cantidad de sistemas vulnerados por el candidato {i + 1}: "))
            if experiencia > 0:
                break
            else:
                print("Cantidad inválida. Debe ingresar un entero positivo.")
        except ValueError:
            print("Cantidad inválida. Debe ingresar un entero positivo.")


    if experiencia > 50:
        hacker_leyenda += 1
        print("Candidato registrado como hacker leyenda")

    elif experiencia <= 50:
        hacker_principiante += 1
        print("Candidato registrado como hacker Novato")



print(f"Se registraron {hacker_leyenda} Hackers Leyenda e {hacker_principiante} Hackers Principiantes.")