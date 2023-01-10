def diHola():
  print("Hola!") # 

diHola()  # llamada a la función, 'Hola!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
  print("Hola " + name + "!")

holaConNombre("Ivan")  # llamada a la función, 'Hola Ivan!' se muestra en la consola

##############################
# función con múltiples parámetros con una sentencia de retorno
def multiplica(num, num2):
 return num * num2

print (multiplica(3, 5)) # muestra 15 en la consola
