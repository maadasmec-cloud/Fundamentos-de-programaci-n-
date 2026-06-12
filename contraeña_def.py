def comprobar_contraena(passw):
    largo = False
    mayus = False
    numer = False
    if len(passw) > 8:
        largo = True
    for i in range(len(passw)):
        if passw[i].isupper():
            mayus= True
        
        if passw[i].isnumeric():
            numer = True


    if largo and mayus and numer:
        return True
    
    else:
        return False


passw = input("Ingrese contraseña: ")
verificacion = comprobar_contraena(passw)

if verificacion:
    print("Contraseña es segura")
else:
    print("contraeña no sefura")

