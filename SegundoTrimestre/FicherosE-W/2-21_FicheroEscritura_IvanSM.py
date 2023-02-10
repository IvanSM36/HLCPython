from io import open

#Creo la funcion
def tablaMulti(num):

    #Hago un if para filtrar los numeros para que sean entre el 1 y 10
    if (num <0 & num >10):
        print("Error, introduzca un numero del 1 al 10")
        num = int (input("Introduzca un numero del 1 al 10: "))
    else:
        # Le doy un nombre al fichero y le indico que es de escritura
        tablaMultiplicar = open('Tabla-'+ str(num)+'.txt', 'w')
        # Escribo en el
        tablaMultiplicar.write("Tabla de multiplicar del " + str(num) +'\n')
        tablaMultiplicar.write('--------------------------\n')
        # Escribo el resultado del for para calcular la tabla de multiplicar
        for i in range(1, 11):
            tablaMultiplicar.write(f'{num} x {i} = {num*i}\n')
    # Cerramos
    tablaMultiplicar.close()
#Pedimos un numero por teclado
numero = int (input("Introduzca un numero del 1 al 10: "))

# Llamo a la funcion
tablaMulti(numero)