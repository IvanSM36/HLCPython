# Declaramos el array
array = [15, 62, 28, 32, 44, 6]

#Mostramos el contenido del array
for num in array:
    print(num)

######### Borrar el valor menor sin usar la funcion min #########
#Creamos una funcion que compare los numero y sacar el menor
def menor(array):
    n = 0
    if n < num:
        n = num
#Recorremos el array y comprobamos el menor
print ("-----------------------------------")
for num in array:
    menor(num)

print ("El menor es: ", num, " será borrado")
print ("-----------------------------------")

#Borramos el valor menor
array.remove(num)

#Mostramos el contenido del array

print("Contenido del array con el numero minimo anterior borrado")
print("---------------------------------------------------------")
for num in array:
    print(num)

######### Calcula el promedio del array sin usan la función promedio #########
#Creamos una funcion para sacar el promedio del array
def promedio(array):
    for num in array:
        sumaTotal = num + num
        promedio = sumaTotal / 6
    return promedio
print (promedio(array))
