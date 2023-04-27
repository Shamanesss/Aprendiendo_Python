# ejemplo For con lista
nombres = ["Maria", "May", "Jone", "Jessica"]
for nombre in nombres:
    print(f"Hola, {nombre}")

    # ejemplo con una lista de colores queremos con nos busque un color y que nos diga si lo ha encontrado
colores = ["Rojo", "Azul", "Verde", "Morado", "Negro"]
micolor = "Azul"
for color in colores:
    # print(color)
    if color == micolor:
        print(f"El color {color} existe")
        break  # finaliza cuando encuentra el color
    else:
        print(f"El color {color} no esta en la lista")
        
 # en un rago del 1 a mil le pedimos que encuentr un numero y que salga del bucle si lo encuentra       
rango_largo=range(1,1000)
print(rango_largo)
for numero in rango_largo:
    print(numero)
    if numero == 100:
        print(f"Encontrado el numero {numero}")
        break
