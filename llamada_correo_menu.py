usuario1 = None
usuario2 = None
usuario3 = None

contrasena1 = None
contrasena2 = None
contrasena3 = None
arroba = False

try:

    while True:
             print("Menu llamadas y correo.")

             print("1.Iniciar sesión\n2.Registrar usuario\n3.Salir.")

             opcion1 = int(input("ingrese una opción del menu: "))

             if opcion1 == 1:
                   if usuario1 == None and usuario2 == None and usuario3 == None:
                         print("Primero necesita registrarse...")
                   else:
                         print("Inicio de sesión")
                         
                         user = input("Ingrese su usuario: ")
                         contrasena = input("Ingrese su contraseña: ")
                         if (user != usuario1 and contrasena != contrasena1) and (user != usuario3 and contrasena != contrasena3) and (user != usuario3 and contrasena != contrasena3):
                                print("usuario o contraseña incorreta")
                            




                         elif (user == usuario1 and contrasena == contrasena1) or (user == usuario2 and contrasena == contrasena2) or (user == usuario3 and contrasena == contrasena3):
                           print(f"{user} Bienvenido")
                           while True:
                                        print("1.Realizar llamada\n2.Enviar correo electronico\n3.Cerrar sesión")

                                        opcion2 = input("Ingrese una opcion del menu: ")

                                        if opcion2 == "1":
                                                while True:
                                                    print("realizar llamada")
                                                    numero = input("Ingrese el numero telefonico que llamara: ")

                                                    if len(numero) == 9 and numero[0] == "9":
                                                        print(f"realizando llamada al numero {numero}")
                                                        break

                                                    else:
                                                        print(f"numero {numero} es incorrecto, debe tener 9 digitos y comenzar en 9 su numero comienza con {numero[0]} y tiene {len(numero)} digitos")
                                        elif opcion2 == "2":
                                                while True:
                                                    print("Enviar correo electronico")
                                                    correo = input("Ingrese el destino de su correo: ")
                                                    if "@" in correo:
                                                          print("Correo correcto")
                                                          mensaje = input("Escriba el mensaje: ")
                                                          print(f"El correo: {mensaje} fue enviado a: {correo}")
                                                          break
                                                    else:
                                                      print(f"El correo {correo} no es valido")
                                        

                                        elif opcion2 == "3":
                                                print("Cerrar sesión")
                                                break
                         else:
                            print("Usuario o contraseña incorrecta")
                                          
             elif opcion1 == 2:
                   print("registro de usuario nuevo")

                   user = input("Ingrese su nuevo usuario: ")
                   contrasena = input("ingrese su nueva contraseña: ")

                   if usuario1 == None and contrasena1 == None:
                         usuario1 = user
                         contrasena1 = contrasena
                         print(f"{user} Usted sera registrado como el usuario 1")

                   elif usuario2 == None and contrasena2 == None:
                         usuario2 = user
                         contrasena2 = contrasena
                         print(f"{user} Usted sera registrado como el usuario 2")

                   elif usuario3 == None and contrasena3 == None:
                         usuario3 = user
                         contrasena3 = contrasena
                         print(f"{user} Usted sera registrado como el usuario 3")
                   else:
                         print("No se pueden registrar mas usuarios")

             elif opcion1 == 3:
                  print("Saliendo del programa....")
                  break

             else:
                  print(f"Opcion {opcion1} no es valida")
                               

                               


   
    

except ValueError:
    print("valor ingresado no valido.")