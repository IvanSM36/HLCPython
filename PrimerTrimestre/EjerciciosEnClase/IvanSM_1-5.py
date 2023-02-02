#Pedimos los datos por teclado
a = int(input("Introduce un numero: "))
b = int(input("Introduce otro numero: "))

#Hacemos el calculo
resultado = a / b

#Si el divisor no es cero imprime el resultado
if(b!=0):
    print(resultado)
#Si el divisor es cero da error
else:
    print("error")

