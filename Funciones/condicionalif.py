numero1 = int(input("dime el primer numero "))
numero2 = int(input("dime el segundo numero "))

if (numero1 > numero2):
    print(f"El numero  {numero1} es mayor que el numero {numero2}")
elif (numero1 < numero2):
    print(f"El numero  {numero1} es mayor que el numero {numero2}")
else:
    print("los dos numero son iguales")
print("Hemos terminado de comparar")


# pregunte la edad
edad = int(input("Dime tu edad para saber el precio del billete "))
if edad < 5:
    precio = 0
elif edad < 15 and edad > 18:
    precio = 5
elif edad < 59:
    precio = 15
else:
    precio = 25
print("El precio del billete es: "+str(precio))
