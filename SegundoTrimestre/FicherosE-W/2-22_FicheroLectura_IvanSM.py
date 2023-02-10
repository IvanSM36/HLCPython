from io import open

# Creo la funcion
def tablaMulti(num):

    # Hago un if para filtrar los numeros para que sean entre el 1 y 10
    if (num <0 & num >10):
        print("Error, introduzca un numero del 1 al 10")
        num = int (input("Introduzca un numero del 1 al 10: "))
    else:

        try:
            # Le doy un nombre al fichero y le indico que es de lectura
            tablaMultiplicar = open('Tabla-'+str(num)+'.txt', 'r')
            resultado = tablaMultiplicar.read()       

            print(resultado)
            # Cerramos
            tablaMultiplicar.close
        except FileNotFoundError:
            print("El fichero no existe.")

# Pedimos un numero por teclado
numero = int (input("Introduzca un numero del 1 al 10: "))

print()

# Llamo a la funcion
tablaMulti(numero)