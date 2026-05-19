usuario1 = None
usuario2 = None
usuario3 = None

contrasena1 = None
contrasena2 = None
contrasena3 = None

while True:
    try:
        print("1.Iniciar sesión\n2.Registrar Usuario\n3.salir")

        opcion_1 = input("Ingrese una opción: ")

        if opcion_1 == "1":
            if usuario1 == None and usuario2 == None and usuario3 == None:
                print("Primero debe registrarse")
            else:
                print("inicio de sesión")
                usuario = input("Ingrese su usuario: ")
                contrasena = input("ingrese su contraseña: ")
                if (usuario == usuario1 and contrasena == contrasena1) or (usuario == usuario2 and contrasena == contrasena2) or usuario == (usuario3 and contrasena == contrasena3):
                    print("usted a iniciado sesión")
                    while True:
                        print("1.Realizar llamada\n2.Enviar correo\n3.cerrar sesión")

                        opcion_2 = input("Ingrese opción: ")

                        if opcion_2 == "1":
                            while True:
                                numero = input("ingrese el numero al que quiere llamar: ")
                                if len(numero) == 9 and numero[0] == "9":
                                    print(f"numero {numero} es correcto, realizando llamada.")
                                    break
                                else:
                                    print(f"numero {numero} es incorrecto ya que tiene {len(numero)} digitos y deben ser 9, y su numero empieza con {numero[0]} y debe comenzar con 9")
                        
                        elif opcion_2 == "2":
                            while True:
                                correo = input("Ingrese correo de destino: ")
                                for letra in correo:
                                    if letra == "@":
                                        mensaje = input("Escribe tu correo")
                                        print(f"Su correo fue enviado al destino {correo}")
                                        break
                                    else:
                                        print(f"correo ingresado {correo} no tiene @")
                        
                        elif opcion_2 == "3":
                            print("cerrar sesión")
                            break


       
        elif opcion_1 == "2":
            usuario = input("ingrese su nuevo usuario: ")
            contrasena = input("Ingrese su nueva clave: ")
            if usuario1 == None:
                usuario1 = usuario
                contrasena1 = contrasena
                print(f"{usuario} se registro correctamente en usuario 1")

            elif usuario2 == None:
                usuario2 = usuario
                contrasena2 = contrasena
                print(f"{usuario} se registro correctamente en usuario 2")

            elif usuario3 == None:
                usuario3 = usuario
                contrasena3 = contrasena
                print(f"{usuario} se registro correctamente en usuario 3")

        elif opcion_1 == "3":
            print("Saliendo de programa")
            break





    except ValueError:
        print("dato ingresado no es correcto")
