inventario_actual = [25, 4, 18, 9, 34, 2, 50, 12, 7]

criticos = []

for producto in inventario_actual:
    if producto < 10:
        print (f"Producto {producto} fue movido a lista criticos..")
        criticos.append(producto)
        
   

menor = min(criticos)
criticos.remove(menor)
criticos.append(menor + 15)

criticos.sort(reverse=True)



print(criticos)




