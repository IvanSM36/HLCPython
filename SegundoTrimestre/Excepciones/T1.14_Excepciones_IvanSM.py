colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 

try:
    colores['blanco']
except KeyError:
    print("La clave 'blanco' no está en el diccionario.")