def calcularNota(n1, n2, n3):
    return (n1 *0.3) + (n2 * 0.3)+ (n3 * 0.4)



n1 = float(input("Ingrese la primera nota: "))
n2 = float (input("Ingrese la segunda nota: "))
n3 = float (input("Ingrese la tercera nota: "))




nota_final = calcularNota(n1, n2 , n3)


print(f"La nota final del estudiantes es: " , round (nota_final,2))