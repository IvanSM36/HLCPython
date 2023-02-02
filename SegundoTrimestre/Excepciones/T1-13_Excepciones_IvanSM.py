# Funcion que agrega un elemento a la lista.
def agregarAnimal(animales, animal):
    try:
        if animal in animales: # Comprueba si existe el elemento en la lista
            raise ValueError("Error, no se puede agregar el animal") # Si existe lanza el error
        else: # Si no existe agrega el elemento e imprime que lo ha agregado
            animales.append(animal)
            print("Se ha agregado correctamente.")
    except ValueError as errorGeneral:
        print(errorGeneral)

# Creo una lista
animales = ["Perro", "Oso", "Toro"]

# Llamo la funcion para agregar un elemento nuevo
agregarAnimal(animales, "Toro")
    
print(animales)