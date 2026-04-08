# EJERCICIO 2#
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 3
acceso = False

while intentos > 0:
    print(f"Te queda {intentos} intentos")
    usuario=input("Ingrese su usuario: ")
    clave=input("Ingese su clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido")
        acceso=True
        break
    else:
        print("Credenciales invalidas.")
        intentos-=1
if not acceso:
    print("Cuenta bloqueada.")

while acceso:
    print("Bienvenido al sistema.")
    print("Eliga una opcion: ")
    print("1_Estado")
    print("2_Cambiar clave")
    print("3_Mensaje")
    print("4_Salir")
    opcion=(input("Elija la opcion que desee: "))
    match opcion:
        case "1":
            print("inscripto")
        case "2":
            n_clave=input("Ingrese su nueva clave: ")
            if len(n_clave) < 6:
                print("Error: la clave debe tener al menos 6 caracteres.")
                continue
            else:
                confirmacion=input("Confirme la nueva clave:")
                if n_clave==confirmacion:
                    print("Se ha actualizado su contraseña")
                else:
                    print("Las claves no coinciden")
        case "3":
            print("Banana")
        case "4":
            print("Saliendo...")
            break
        case _:
            print("Error. Elija una opcion correcta")




