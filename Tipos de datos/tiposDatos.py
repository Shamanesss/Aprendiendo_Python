print('Bienvenido a  mi primer programa')
print('Tipo Entero')
print(type(23))
print('Tipo decimal')
print(type(12.32))
print('Tipo Cadena')
print(type('Saludo'))
print('Tipo booleano')
print(type(False))

# Ejemplos con cadenas
print("Hola, "+" amigos!!")
print("Saludos"*4)  # muestra 4 veces el string indicado
# concatena dos String
variable = "cadena en variable"
variable = "Sumo esto a  " + variable
print(variable)
# inprime solo la posiciones que le digamos
variable = "Murcilago"
# nos muestra la i que es el tercer espacio
print(variable[3])  # c
print(variable[7])  # G
print(variable[-1])  # o empieza por el final
# cila empieza en la 3 e imprime hasta 6 pero hay que decirle donde acaba en la 7
print(variable[3:7])
print(len(variable))  # no dice cuantos caracteres tiene
print("Esto es un cadena en mayusculas".upper())  # pone todo en mayusculas
print("Esto es un cadena en minuscualas".lower())  # pone la todo en minusculas
print("pepito".capitalize())  # pone la primera letra en mayuscuala
cadena = "    Esto es una cadena de muchos espacios     "
print(cadena)
print(cadena.strip())  # quita los espacios de delante y de detras
cadena = "Hola esto es un texto sin reemplazar"
print(cadena)
print(cadena.replace("Hola", "Adios"))
