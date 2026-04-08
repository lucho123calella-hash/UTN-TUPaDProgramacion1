# EJERCICIO 3 #
lunes1=""
lunes2=""
lunes3=""
lunes4=""
martes1=""
martes2=""
martes3=""

operador=input("Ingrese su nombre: ")
while not operador.isalpha():
    perador=input("No se permiten numeros. Ingrese su nombre: ")
    print(f"Bienvenido {operador}")

    
while True:
 print("1. Reservar turno")
 print("2. Cancelar turno (por nombre)")
 print("3. Ver agenda del día")
 print("4. Ver resumen general")
 print("5. Cerrar sistema")
 opcion=input("Por favor elija una opcion: ")
 match opcion:
    case "1":
       dia_t=input("Que dia desea reservar el turno 1=Lunes 2=Martes. ")
       match dia_t:
         case "1":
            nombre=input("Ingreses su nombre:")
            if nombre.isalpha():
               if nombre==lunes1 or nombre==lunes2 or nombre==lunes3 or nombre==lunes4:
                  print("Error: el paciente ya tiene turno.")
               elif lunes1=="":
                  lunes1=nombre
                  print("Turno 1 reservado.")
               elif lunes2=="":
                  lunes2=nombre
                  print("Turno 1 reservado.")
               elif lunes3=="":
                  lunes3=nombre
                  print("Turno 1 reservado.")
               elif lunes3=="":
                  lunes3=nombre
                  print("Turno 1 reservado.")
               elif lunes4=="":
                  lunes4=nombre
                  print("Turno 1 reservado.")
               else:
                  print("Lo sentimos. Lunes completo")
            else:
               print("Error: El nombre solo puede contener letras.")
         case "2":
            nombre=input("Ingreses su nombre:")
            if nombre.isalpha():
               if nombre==martes1 or nombre==martes2 or nombre==martes3:
                  print("Error: el paciente ya tiene turno.")
               elif martes1=="":
                  martes1=nombre
                  print("Turno 1 reservado.")
               elif martes2=="":
                  martes2=nombre
                  print("Turno 1 reservado.")
               elif martes3=="":
                  martes3=nombre
                  print("Turno 1 reservado.")
               else:
                  print("Lo sentimos. Martes completo")
            else:
               print("Error: El nombre solo puede contener letras.")
    case "2":
       dia_t=input("Que dia desea cancelar el turno 1-Lunes 2-Martes.")
       nombre=input("Ingrese su nombre: ")
       match dia_t:
          case "1":
             if lunes1==nombre:
                lunes1=""
                print("Su turno fue cancelado.")
             elif lunes2==nombre:
                lunes2=""
                print("Su turno fue cancelado.")
             elif lunes3==nombre:
                lunes3=""
                print("Su turno fue cancelado.")
             elif lunes4==nombre:
                lunes3=""
                print("Su turno fue cancelado.")
             else:
                print("No se encotro el paciente.")
          case "2":
             if martes1==nombre:
                martes1=""
                print("Su turno fue cancelado.")
             elif martes2==nombre:
                martes3=""
                print("Su turno fue cancelado.")
             elif martes3==nombre:
                martes3=""
                print("Su turno fue cancelado.")
             else:
                print("No se encotro el paciente.")
    case "3":
       dia_t=input("Que dia desea ver la agenda? 1-Lunes 2-Martes.")
       match dia_t:
          case "1":
             print(f"Su agenda del dia Lunes es: {lunes1}, {lunes2}, {lunes3}, {lunes4}")
          case "2":
             print(f"Su agenda de dia Martes es: {martes1}, {martes2}, {martes3}")
    case "4":
       print("---- RESUMEN GENERAL----")
       print(f"Dia Lunes: {lunes1}, {lunes2}, {lunes3}, {lunes4}")
       print(f"Dia Martes: {martes1}, {martes2}, {martes3}")
    case "5":
       print("Saliendo...")
       break