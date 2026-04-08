# EJERCICIO 4#
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

agente = input("Ingrese nombre del agente: ")
while not agente.isalpha():
    agente = input("Error. Ingrese solo letras: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print("--- ESTADO ---")
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} | Alarma: {alarma}")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opcion: ")
    while not opcion.isdigit() or int(opcion) not in [1,2,3]:
        opcion = input("Error. Ingrese 1, 2 o 3: ")

    opcion = int(opcion)
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1
        if forzar_seguidas == 3:
            alarma = True
            print("La cerradura se trabó! Se activó la alarma.")
            continue
        if energia < 40:
            num = input("Riesgo! Elegí número 1-3: ")
            while not num.isdigit() or int(num) not in [1,2,3]:
                num = input("Error. Ingrese 1,2 o 3: ")
            if int(num) == 3:
                alarma = True
                print("Activaste la alarma!")
        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura!")
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0
        print("Hackeando.")
        for i in range(4):
            print(f"Paso {i+1}")
            codigo_parcial += "A"
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura abierta automaticamente!")
    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        forzar_seguidas = 0
        if alarma:
            energia -= 10
            print("La alarma te drena energía!")
        print("Descansaste.")
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma!")
        break
if cerraduras_abiertas == 3:
    print("VICTORIA.Abriste la boveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA.Te quedaste sin recursos.")