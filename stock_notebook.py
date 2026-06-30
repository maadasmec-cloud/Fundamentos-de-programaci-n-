productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'], 
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'], 
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    'FS1230HD': ['acer', 15.6, '4GB', 'DD', '500GB', 'Intel', 'integrada']
} 

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1], 
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7], 
    'GF75HD': [749990,2], 
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0]
}

#================================
#FUNCIÓN MOSTRAR STOCK POR MARCA
#================================
"""En esta funcion mostraremos el stock por marca, primero debmos pedir la marca al usuario
(desde la función principal) iniciamos una variable total_stock que ira acumulando la suma
de los stock al ir recorriendo el diccionario de productos, iniciamos un ciclo con la 
variable modelo y otra variable detalles en el diccionario producto usando items. usando items()
le decimos que nos entre primero la llave (modelo) y luego el valor de la llave (detalle),
en una nueva variable llamada marca_producto guardamos lo que nos entrega detalle en el indice 0 
(detalle[0]) ahora comparamos esa variable marca_prducto con marca ingresada por el usuario
usamos lower para que sea aprueba de errores, ahora llamamos otra vez la variable acumuladora
total_stock y sumamos stock[modelo][1], modelo es lo que se guardo en la primera variable del ciclo
o sea la clave, finalizamos con un prin donde mostramos el resultado de la suma de todas las
vueltas y que fueron acumulando en total_stock"""
def stock_marca(marca):
    #Iniciamos una variable acumulador que guarda el total de stock que ira sumando por ciclos
    total_stock = 0 
    #iniciamos un ciclo con los variables, modelo que guarda clave y detalles que guarda el valor
    #usamos items() en el diccionario que vamos a recorrer para que entregue todo completo clave y valor
    for modelo, detalles in productos.items():
        #iniciamos una nueva variable donde se guardara lo de la variable detalle en el indice [0]
        marca_producto = detalles [0]
        #comparamos la variable con el dato ingresado por el usario en lower para evitar error
        if marca_producto.lower() == marca.lower():
            #si es verdadero llamamos la variable total, llamamos el diccionario stock 
            #aqui con la primera variable del ciclo que es modelo nos metemos al diccionario
            # stock en la clave[modelo] y el indice [1] el indice [1] tiene el stock y es lo que suma
            total_stock += stock[modelo][1]
    #mostramos al final del ciclo el total sumado
    print(f"El stock es: {total_stock}")



def principal ():

    marca = input("Ingrese la marca: ")
    stock_marca(marca)


if __name__ == "__main__":
    principal()