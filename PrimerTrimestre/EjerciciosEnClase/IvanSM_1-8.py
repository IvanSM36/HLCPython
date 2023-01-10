#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)

#Introducimos los datos por teclado
edad = int(input("Introduzca tu edad: "))

#Declaramos una variable contador a 0
x = 1

#Creamos un for desde el contador hasta la edad introducida
for x in range(edad):
    x = x + 1 # sumamos 1 el contador 
    print (x)