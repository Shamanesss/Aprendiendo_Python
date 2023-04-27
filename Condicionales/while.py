# tabla de multiplicar
tabla = int(input("Que tabla quieres calcular?"))
# creamos la variable contador
contador = 1
print(f"Tabla del {tabla}")
# la repeticion
while (contador < 11):
    resultado = tabla * contador
    # mostramos la tabla
    print(f"{tabla} X {contador} = {resultado}")
    # incrementamos el contador
    contador = contador + 1
print("Fin de la tabla")
