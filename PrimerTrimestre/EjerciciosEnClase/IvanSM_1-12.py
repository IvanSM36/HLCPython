
#Declaramos el diccionario
from multiprocessing.sharedctypes import Value


dicCiudad = dict()
contLetra = 0
i = 0
letra = "a"

#Recorremos un for para pedir 5 ciudades por teclado
for i in range(5):
    ciudad = (input("Introduzca una ciudad: "))
    #Agregamos la ciudad a un diccionario
    dicCiudad[i] = ciudad

#Mostramos el contenido del diccionario
print("Ciudades")
print("--------")
print(dicCiudad)

print()

#Volvemos a recorrer el diccionario para contar las letras
for i in dicCiudad:
    if letra == dicCiudad.values:
        contLetra += 1
    if contLetra == 5:
        print("Ya se ha encontrado las 5 a.")
    else:
        print("No se ha encontrado las 5 a")
