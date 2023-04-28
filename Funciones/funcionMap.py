# creamos un lista
import functools
lista = [25, 3, 2, 35, 1, 5, 68, 86, 988, 94]

# creamos un funcion anonima lambda para ejecutar el cuadro de los valores de la lista
# nos devuelve el cuadrado de cada uno de los valores de la lista
print(list(map((lambda valor: valor*valor), lista)))

# funcion filter donde solo hemos sacado los numeros pares
print(list(filter((lambda valor: valor % 2 == 0), lista)))

# funcion reduce nos devuelve un valor
# muestra la suma de todas lo numeros de la lista
print(str(functools.reduce((lambda x, resultado: x+resultado), lista)))
