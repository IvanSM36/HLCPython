# Creo la clase Cuenta
class Cuenta():
    
    # Constructor     
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    # Metodo que muestra los datos del usurio
    def datosUsuario(self):
        print("Datos de la cuenta:")
        print("-------------------")
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)
        print()

# Creo la clase Caja Ahorro
class CajaAhorro(Cuenta):   
    def __init__(self, titular, cantidad):
        Cuenta.__init__(self, titular, cantidad)
       

    # Metodo que muestra informacion de la caja ahorro
    def datosCajaAhorro(self):
        print("Datos de caja de Ahorro:")
        self.datosUsuario()
        print()

# Creo la clase PlazoFijo
class PlazoFijo(Cuenta):    

    # Constructor
    def __init__(self, titular, cantidad, plazo, interes):
        Cuenta.__init__(self, titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    # Metodo que calcula el importe del interes
    def calcularImporteInteres(self):
        return self.cantidad * self.interes / 100
    
    # Metodo para mostra la informacion de esta clase
    def mostrarInformacion(self):
        print("Cuenta de Plazo Fijo:")
        print("---------------------")
        print("Titular:", self.titular, "Plazo:", self.plazo, "Interes:", self.interes, "Total de interes:",  self.calcularImporteInteres())
        print()

# Creo el objeto Cuenta
user01=Cuenta("Ivan", 2000)  
# Creo el objeto CajaAhorra
caja = CajaAhorro("Caja", 2000)
# Creo el objeto CajaAhorra
plazo = PlazoFijo("PlazoFijo", 2000, 12, 2.5)

# Llamo al metodo datosUsuario de la clase Cuenta
user01.datosUsuario()

# Llamo al metodo Heredado de cuenta
caja.datosUsuario()
# Llamo al metodo de la propia clase
caja.datosCajaAhorro()

# Llamo al metodo heredado de cuenta
plazo.datosUsuario()
# Llamo al metodo de la propia clase
plazo.mostrarInformacion()