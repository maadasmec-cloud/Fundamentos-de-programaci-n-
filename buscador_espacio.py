


while True:
        espacio = False
        palabra = input("palabra: ")


        for i in palabra:
            print(i)
            if i == " ":
                espacio = True
                
                
            
        if espacio == True:
                print("No puede tener espacio")
        else:
            print("palabra ok sin palabras")
            break