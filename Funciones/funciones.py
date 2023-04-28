# creacion de la funcion21
def esPar(numero):
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")


# llamada a usuario
numero = int(input("Dime  un numero "))

# llamamos a la funcion
esPar(numero)
esPar(23)
esPar(24)


# este funcion nos devuelve un valor
def esImpar(numero):
    if numero % 2 != 0:
        return True
    else:
        return False


numero = int(input("Dime un numero "))
resultado = esImpar(numero)
# aqui le indicamos que si es resultado es true
if resultado:  # esto es igual a esto if resultado == true
    print(f"el numero {numero} es impar")
else:
    print(f"el numero {numero} es par")
