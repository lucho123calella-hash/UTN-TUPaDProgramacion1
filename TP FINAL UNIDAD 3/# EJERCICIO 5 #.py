
gladiador = input("Ingrese el nombre de su gladiador: ")
while not gladiador.isalpha():
    gladiador=input("Error solo se permiten letra.Ingrese el nombre de su galdiador: ")
print(f"Bienvenido {gladiador}")
hp_gladiador= 100
hp_enemigo= 100
pocion= 3
atq_pesado= 15
atq_enemigo= 12
turno_gladiador: True
turno_enemigo:False
print("---Comienza el combate-----")
while hp_gladiador > 0 and hp_enemigo > 0:
 print (f"La vida actual de {gladiador} es de {hp_gladiador} y la de tu enemigo es de {hp_enemigo}")
 print("1_Ataque pesado.")
 print("2_Ataque de rafaga.")
 print("3_Beber una pocion.")
 opcion=int(input("Elija una opcion: "))
 while opcion not in [1, 2, 3]:
    opcion=int(input("Error. Elija una opcion correcta: "))
 match opcion:
    case 1:
        hp_enemigo-=atq_pesado
        print("Has acertado un ataque pesado. El enemigo recibio un daño de 15 puntos")
    case 2:
        hp_enemigo-=atq_enemigo
        for i in range(3):
         hp_enemigo -= 5
         print("Golpe acertado -5 de vida.")
    case 3:
        if pocion == 0:
           hp_gladiador-=atq_enemigo
           print("No te quedan pociones. Pierdes el turno y el enemigo ataca.")
        else:
         hp_gladiador+=15
         pocion-=1
         print(f"Se ha restaurda 15 de vida, se descarta una pocion. Te queda {pocion} pociones.")
    case _:
        print("Error. Elija una opcion correcta")
 if hp_enemigo <= 0:
   print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
   
 elif hp_gladiador <= 0:
   print("DERROTA. Has caído en combate")
 if hp_enemigo > 0:
        hp_gladiador -= 12
        print("El enemigo te atacó por 12")