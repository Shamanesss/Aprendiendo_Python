# tabla de multiplicar con FOR
tabla = int(input("que tabla quieres ver ?"))
print(f"Tabla del {tabla}")
# repetir mientras sea mayor que 11
for contador in range(1, 11):
    resultado = tabla * contador
    print(f"{tabla} X {contador} = {resultado}")
print("Eso es todo amigos")
