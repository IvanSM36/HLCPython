# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su 
# frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva
# una tupla con la palabra más repetida y su frecuencia.
 

#Hacemos un split con la frase
frase = 'El perro de San Roque no tiene rabo porque Ramón Ramírez se lo ha cortado El perro de Ramón Ramírez no tiene rabo porque se lo han robado probre perro'
palabras = frase.split(' ')

#Declaramos el diccionario
dictPalabras = dict()

#Agregamaos las palabras a la clave del diccionario
#El Valor del diccionario será un contador de palabras repetidas 
valor = 1
#Recorremos con un for el string palabras para pasar cada palabra a key
for key in palabras:  
    #Si la key esta en el diccionario, se sumara 1 el valor 
    if key in dictPalabras:
        dictPalabras [key] += valor
    #Si no añadira la key contara el valor como 1
    else:
        dictPalabras[key] = 1

#Imprimimos el diccionario
print(dictPalabras)

#Recorremos el diccionario para mostrar el valor mas alto 

#dictPalabras.get()
#max(dictPalabras, palabraMasRepe = dictPalabras.get)