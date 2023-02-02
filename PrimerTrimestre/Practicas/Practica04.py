## Ejercicio Fimonacci
from unittest import result

def fibonacci(numero):
    if(numero>1):
        return fibonacci(numero-1) + fibonacci(numero-2)
    elif numero==1:
        return 1
    elif numero==0: 
        return 0
    else:
        resultado=("Debes introducir un numero")
        return resultado

print(fibonacci(7))