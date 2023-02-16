import pickle

############################ Clase Persona ############################

# Creo la clase Persona
class Persona():
     # Constructor     
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad 

    # Metodo
    def datosPersona(self):
        print("Nombre:",self.nombre, "\nApellidos:",self.apellidos, "\nEdad:",self.edad)

######################################################################

############################ Creo el fichero ############################

# Creamos varios objetos Personas
p1 = Persona("Roberto", "Romero", 26)
p2 = Persona("Armando", "Almando", 29)
p3 = Persona("Clotilde", "Clitoria", 25)

# Creo una lista de los objetos creados
personas = [p1, p2, p3]

# Creamos un fichero de escritura con el contenido de la lista pero en binario
fichero= open("listaPersonas", "wb")

#Volcamos la informacion de la lista persona al fichero
pickle.dump(personas,fichero)

# Cerramos la conexion del fichero
fichero.close()

# Borramos el fichero en memoria
del(fichero)

######################################################################

############################ Leo el fichero ############################

# Abrimos el fichero
abrirFichero = open("listaPersonas", "rb")

#Variable para cargar la informacion del fichero
listaPersonas = pickle.load(abrirFichero)

#Cerramos la conexion
abrirFichero.close

#Recorremos con un for la informacion de la variable listaPersonas
print("\nLista de personas")
print("-----------------")
print()
for p in listaPersonas:
    print(p.datosPersona())
    print()

######################################################################
