#Pedimos los datos por teclado
edad = int(input("Introduzca tu edad: "))
ingresos = float(input("Introduzca tus ingresos mensuales: "))

#Si es mayor de 16 y tiene un ingreso mayor o igua a 1000 tiene que cotizar si no no
if edad > 16 and ingresos >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")

    