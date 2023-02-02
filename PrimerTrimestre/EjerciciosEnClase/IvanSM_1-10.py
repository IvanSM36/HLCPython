#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
# año que dura la inversión.

#Pedimos por teclado la cantidad a invertir
cantidadInvertir = float(input("Introduzca la cantidad a invertir: "))
#Pedimos por teclado el interes anual
intereses = float(input("Introdzca el interes anual: "))
#Pedimos por teclado el numero de años
anios = int(input("Introduzca numero de años: "))

for i in range(anios):
    cantidadInvertir *= 1 + intereses / 100 
    print("Dinero invertido tras " + str(i+1) + " años: " + str(cantidadInvertir))