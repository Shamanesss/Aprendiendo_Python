#nos muestra los numero de 1 al 50
for numero in range(1,51):
    print(numero)
    
#nos muestra los numeros de 1 al 50  solo los impares
def impares():
   for numero in range(1, 50, 2):
       yield(numero) 
    #es un generador que nos devuel el numero dentro del rango estipulado
    
generador = impares()
print(next(generador))
print(next(generador))
print(next(generador))

for numero in generador:
     print(numero)
print(generador)