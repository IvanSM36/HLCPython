# Array vegetariano
vegetariana = ["Pimiento", "Tofu"]
# Array no vegetarianos
noVegetariana = ["Peperoni", "Jamon", "Salmon"]

# Menu
print("Menu de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = int(input("Elige el menu: "))


if tipo == 1 :
    for menuVeg in vegetariana:
        print("\t", menuVeg)

elif tipo == 2:
        for menuNoVeg in noVegetariana:
            print("\t", menuNoVeg)
else:
    print("Error, por favor introduzca la opcion 1 o 2")
#Pedimos el ingrediente
ingrediente = input("Elija el ingrediente: ")

if ingrediente == "Pimiento":
    print("La pizza es vegetariana, incluye mozzarella, tomate y ", ingrediente)
elif ingrediente == "Tofu":
    print("La pizza es vegetariana, incluye mozzarella, tomate y ", ingrediente)
elif ingrediente == "Peperoni":
        print("La pizza no es vegetariana, incluye mozzarella, tomate y ", ingrediente)
elif ingrediente == "Jamon":
        print("La pizza no es vegetariana, incluye mozzarella, tomate y ", ingrediente)   
elif ingrediente == "Salmon":
        print("La pizza no es vegetariana, incluye mozzarella, tomate y ", ingrediente)             


