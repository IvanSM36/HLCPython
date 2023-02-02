# Creo la clase Cuenta
class Cuenta():
    # Atributos
    titular = ""
    cantidad = 0

    # Constructor
    def __init__(titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    # Metodo que muestra los datos del usurio
    def datosUsuario():
        print("Titular: ", titular, "Cantidad: ", cantidad)

# Creo la clase Caja Ahorro
class CajaAhorro(Cuenta):
    
    # Metodo que muestra informacion de la caja ahorro
    def datosCajaAhorro():
        print("Datos caja ahorro")

# Creo la clase PlazoFijo
class PlazoFijo(Cuenta):    
    # Atributos
    plazo = 0
    interes = 0

    # Constructor
    def __init__(self, plazo, interes):
        self.plazo = plazo
        self.interes = interes

    # Metodo que calcula el importe del interes
    def calcularImporteInteres(cantidad, interes):
        return cantidad*interes/100
    
    # Metodo para mostra la informacion de esta clase
    def mostrarInformacion(totalInteres):
        print("Titular: ", Cuenta.titular, "Plazo: ", PlazoFijo.plazo, "Interes: ", PlazoFijo.interes, "Total de interes: ",  totalInteres)


# Creo el objeto Cuenta
usuario01=Cuenta()  

# Meto datos al objeto   
usuario01.titular="Ivan"
usuario01.cantidad = 2000

# Llamo al metodo datosUsuario de la clase Cuenta
usuario01.datosUsuario()