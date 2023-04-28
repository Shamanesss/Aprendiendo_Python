def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    opcion = int(input("?__"))
    return opcion


def solicitaDatos():
    num1 = int(input("Dime el primer numero "))
    num2 = int(input("Dime el segundo numero "))
    return num1, num2


def operacion(operador, num1, num2):
    if operador == "suma":
        resultado = num1 + num2
    elif operador == "resta":
        resultado = num1 - num2
    elif operador == "multiplica1":
        resultado = num1 * num2
    elif operador == "divide":
        resultado = num1 / num2
    return resultado


# Siempre se ejecuta hasta que pulsemos el 0 para salir
while True:
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} + {num2}  es = ")
        print(operacion("suma", num1, num2))
    elif opcion == 2:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} - {num2}  es = ")
        print(operacion("resta", num1, num2))
    elif opcion == 3:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} * {num2}  es = ")
        print(operacion("multiplica", num1, num2))
    elif opcion == 4:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} / {num2}  es = ")
        print(operacion("divide", num1, num2))
    elif opcion == 0:
        break
    else:
        print("introduce un numero del 1 al 4")
    print("\n")
print("Bye")
