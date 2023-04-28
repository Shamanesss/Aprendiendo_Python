# funcion simple
def suma(a, b):
    return a + b

# funcion anidada


def calcular(a, b, operacion="sumar"):
    def sumar(a, b):
        return a+b

    def restar(a, b):
        return a-b

    def multiplicar(a, b):
        return a*b

    def dividir(a, b):
        return a/b
    if operacion == "sumar":
        print(f"{a} + {b} = {sumar(a,b)}")
    elif operacion == "restar":
        print(f"{a} - {b} = {restar(a,b)}")
    elif operacion == "multiplicar":
        print(f"{a} * {b} = {multiplicar(a,b)}")
    elif operacion == "dividir":
        print(f"{a} / {b} = {dividir(a,b)}")
    return "Resultado"


print(calcular(3, 5))
print(calcular(3, 5, "multiplicar"))
print(calcular(45, 5, "dividir"))
