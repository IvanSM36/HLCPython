from unittest import result

def factorial (num):
    if num == 1 or num == 0:
        return 1
        print (result)

    if num > 1:
        result = num * factorial(num -1)
        return result

    else:
        txt = ("Error, el numero debe ser positivo")
        return  txt

num = 9
print ("El factorial de " + str(num) + " es: " + str(factorial(num)))