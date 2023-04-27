nombre = input("Dime tu nombre ")
print("Hola, " + nombre, end=" ")  # da  un espacio y sigue la siguiente linea
print("Hola ", nombre + "\n\n")  # deja dos lineas libres
# tabuala y de dos tabuladores de espacio
print(f"Hola, {nombre}" + "\t\t\texto con espacios de tabulacion")

numero1 = int(input("Dime un numero "))
numero2 = int(input("Dime otro numero"))
resultado = numero1 + numero2
# aqui no suma solo suma una concatenacion de los numeros
print(f"La suma de  {numero1} mas {numero2} es igual a {resultado}")
