#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

#Pedimos los datos por teclado
numero = int(input("Introduzca un numero positivo: "))

#Iniciamos un contador a 0
countDown = 0

#Creamos un bucle for que cuente desde 0 hasta el numero introducido,
#Luego el primer -1 indicamos para que cuente el 0
#El segundo -1 es la operacion, estaria restando el numero introducido a -1
for countDown in range(numero, -1, -1):
    print (countDown, end=' ') # con end=' ' muestra el contenido en la misma linea y el espacio dentro separamos
