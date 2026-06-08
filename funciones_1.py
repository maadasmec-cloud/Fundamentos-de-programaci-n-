def sum(a, b):
    return a + b

def resta(a, b):
    return a-b


while True:
    print("Menú principal matematicas")

    print("1-sumar\n2-restar\n3-salir")
    


    opcion_menu = input("Ingrese una opción: ")

    num1 = float(input("ingrese el primer numero: "))

    num2 = float( input("INgrese el segundo numero: "))

    if opcion_menu == "1":
        print(f"La suma de ambos numero es:", sum(num1, num2))

    elif opcion_menu == "2":
        print(f"la resta de ambos numeros es: ", resta(num1, num2))



    elif opcion_menu == "3":
        break