# damos valor a una variable
precio = 224
cantidad = 3
Nombre = "Pepito"

# Calculamos total
total = precio * cantidad
# no se puede sumar un string y un numero asique hay que convertirlo en string
print("El precio total es de " + str(total))

# borrar variable
del precio
# print(precio)  # da error porque la hemos borrado

# asignamos  otros valores a cantidad y creamos precio
precio = 43
cantidad = 5
total = precio * cantidad

print("El precio total es de " + str(total))

# un constante para que no cambie se pone en mayusculas
PASSWORD = "1234"

# asignar varios valores a la vez
a, b, c, d = 1, 4, "nombre", True
print(a)
print(b)
print(c)
print(d)

# asignar mismo valor a varias variables
j = k = l = 17
print(j)
print(k)
print(l)
