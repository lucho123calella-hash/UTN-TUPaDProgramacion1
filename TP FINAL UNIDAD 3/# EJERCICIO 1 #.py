# EJERCICIO 1 #
total= 0
t_desc= 0
t_sin_desc= 0
ahorro= 0 

cliente= input("Ingrese su nombre: ")
while not cliente.isalpha():
    cliente=input("Por favor ingrese el nombre sin numeros: ")
productos=(input("ingrese la cantidad de productos a comprar: "))
while not productos.isdigit():
    productos=(input("ingrese la cantidad de productos a comprar: "))
for i in range(int(productos)):
    precio=(input(f"Ingrese el valor del producto {i+1}: "))
    while not precio.isdigit():
     precio=(input(f"Ingrese el valor del producto {i+1}:"))
    precio= float(precio)
    total += precio
    tiene_desc =input("Usted tiene un descuento s/n: ").lower()
    while tiene_desc != "s" and tiene_desc != "n":
     tiene_desc =input("Usted tiene un descuento s/n: ").lower()
    if tiene_desc =="s":
     print("Se realizo un 10% de desceunto")
     t_desc=total*0.10
     t_sin_desc=total*0.90
     ahorro=t_desc

    elif tiene_desc == "n":
     t_desc=0
     t_sin_desc=total
     ahorro=0
     print("No se realiza descuento")
ahorro = total - t_desc
print(f"Hola, el total es: {total}")
print(f"El total con descuentos es {t_desc:.2f}")
print(f"El total de tu ahorro es: {ahorro:.2f}")

          