contenedor_pesado = 0
contenedor_ligero = 0
peso_total = 0
peso_maximo = 0


while True:
      try:
            cantidad_contenedores = int(input("ingrese cantidad de contenedores a registrar: "))
            if cantidad_contenedores > 0:
                  break
            else:
                print("Cantidad no valida")
      except ValueError:
            print("Debe ser un numero entero valido")

for i in range(cantidad_contenedores):
      

    while True:
        codigo_contenedor = input("Ingrese codigo del contenedor: ")
        if len(codigo_contenedor) == 5:
                break
        else:
            print("Codigo invalido")

    while True:
       try:
            peso_contenedor = float(input("Ingrese el peso del contenedor: "))
            if peso_contenedor <= 0:
                 print("Numero debe ser mayor a 0")
            elif peso_contenedor >= 50:
                  contenedor_pesado += 1
                  peso_total += peso_contenedor
                  break
            else:
                 contenedor_ligero += 1
                 peso_total += peso_contenedor
                 break
                  

           
                 
                 
          
          
       except ValueError:
             print("Peso inválido. Debe ingresar un valor numérico positivo.")

    if peso_contenedor > peso_maximo:
                  peso_maximo = peso_contenedor
            

print(f"Total contenedores pesados: {contenedor_pesado}")
print(f"Total contenedores ligeros: {contenedor_ligero}")
print(f"el promedio de peso total es: {peso_total / cantidad_contenedores} kg")
print(f"el contenedor mas pesado peso: {peso_maximo} kg")