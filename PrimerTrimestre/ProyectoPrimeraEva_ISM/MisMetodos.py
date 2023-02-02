import cx_Oracle
from tabulate import tabulate

#Creamos la conexión
dsn = cx_Oracle.makedsn(host='localhost', port=1521, sid='xe')
conn = cx_Oracle.connect(user="IVANSM", password="IvanSM", dsn=dsn)

#Metodo que muestra el menu Principal
def menuPrincipal():
# Creamos el Menu con un while para que lo vuelva a mostrar despues de la opcion elegida
    salir = False
    opcion = 0
    while not salir:
        print()
        print("   ####### Proyecto Python IvanSM ########")
        print("┌────────────────────────────────────────────┐")
        print("│               Menu Principal               │")
        print("╞════════════════════════════════════════════╡")
        print("│ 01. Crear Tabla Animales.                  │")
        print("│ 02. Insertar datos en la tabla.            │")
        print("│ 03. Modificar datos de la tabla.           │")
        print("│ 04. Borrar datos por clave.                │")
        print("│ 05. Mostrar todo el contenido de la tabla. │")
        print("│ 06. Mostrar datos del registro por clave.  │")
        print("│ 07. Consulta con funcion (avg, max, min).  │")
        print("│ 08. Consulta con agrupacion de resultados  │")
        print("│ 09. Mete en un Array nombre de los perros. │")
        print("│ 10. Mete en un Diccionario las especies.   │")
        print("│  0. Salir del programa.                    │")
        print("└────────────────────────────────────────────┘")

        # Simulamos un switch con if para llamar a los metodos segun la opcion elegida
        opcion = int (input("Introduzca una opcion: "))

        if opcion == 1:
            crearTabla()
        elif opcion == 2: 
            insertar()
        elif opcion == 3: 
            modificar()
        elif opcion == 4:
            borrar()
        elif opcion == 5:    
            mostrarTodo()
        elif opcion == 6: 
            mostrarPorID()
        elif opcion == 7:    
            menuConsultasMinMax() 
        elif opcion == 8:    
            menuConsultasAgrupacion()
        elif opcion == 9:
            arrayNombresPerro()
        elif opcion == 10:
            diccionarioEspecies()
        elif opcion == 0:  
            salir = True
            print("\nHas salido del programa correctamente.")
            #Cerramos la conexion cuando salimos de la aplicacion
            conn.close()
        else:
            print("\nPor favor, introduzca una opcion entre 1 - 8: ")    

#Metodo que muestra el menu de consultas min max
def menuConsultasMinMax():
    salir = False
    opcion = 0
    while not salir:
        print()
        print("   ####### Proyecto Python IvanSM ########")
        print("┌───────────────────────────────────────────────────────────┐")
        print("│                Menu Consultas con funcion                 │")
        print("╞═══════════════════════════════════════════════════════════╡")
        print("│ 1. Consultar la altura del oso mas alto.                  │")
        print("│ 2. Consultar el peso del elefante con menor peso.         │")
        print("│ 0. Volver al menu principal.                              │")
        print("└───────────────────────────────────────────────────────────┘")

        opcion = int (input("Introduzca una opcion: "))

        if opcion == 1:
            consultarOsoMasAlto()
        elif opcion == 2: 
            consultarElefanteMenorPeso()      
        elif opcion == 0:  
           menuPrincipal()
        else:
            print("Por favor, introduzca una opcion entre 1 - 8: ")    
    print("Has salido del programa correctamente.")    

#Metodo que muestra el menu de consultas con agrupacion
def menuConsultasAgrupacion():
    salir = False
    opcion = 0
    while not salir:
        print()
        print("   ####### Proyecto Python IvanSM ########")
        print("┌──────────────────────────────────────────────┐")
        print("│         Menu Consultas con agrupación        │")
        print("╞══════════════════════════════════════════════╡")
        print("│ 1. Consultar numero de animales por sexo.    │")
        print("│ 2. Consultar numero de animales por especie. │")
        print("│ 0. Volver al menu principal.                 │")
        print("└──────────────────────────────────────────────┘")

        opcion = int (input("Introduzca una opcion: "))

        if opcion == 1:
            consultaGroupByCuentaSexo()
        elif opcion == 2: 
            consultaGroupByCuentaEspecie()
        elif opcion == 0:  
           menuPrincipal()
        else:
            print("Por favor, introduzca una opcion entre 1 - 8: ")    
    print("Has salido del programa correctamente.") 

#Metodo que crea una tabla en la base de datos
def crearTabla():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()
            #Creamos el codigo sql
            cur.execute('CREATE TABLE animales(id NUMBER(8), nombre VARCHAR2(10), especie VARCHAR2(10), fecha_nacimiento DATE, sexo CHAR, altura float, peso float, descripcion LONG, PRIMARY KEY (id))')
            print("\nTabla creada correctamente.")
            
    except Exception as e:
            print("Error: ", str(e))

#Metodo que inserta datos en la base de datos
def insertar():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()
                
            #Pedimos los datos por teclado
            id = int(input("Introduzca id: "))             
            nombre = str(input("Introduzca nombre: "))
            especie = str(input("Introduzca especie: "))
            fechaNacimiento = str(input("Introduzca la fecha de nacimiento: "))
            sexo = (input("Introduzca si es macho o hembra (M/H): ")[0])#[0] Recoge solo la primera letra
            altura = float(input("Introduzca altura: "))
            peso = float(input("Introduzca peso: "))
            descripcion = str(input("Introduzca una descripcion: "))
                
            #Creamos el codigo sql
            sqli = "INSERT INTO animales(id, nombre, especie, fecha_nacimiento, sexo, altura, peso, descripcion) VALUES (:id, :nombre, :especie, :fechaNacimiento, :sexo, :altura, :peso, :descripcion)"
               
            #Ejecutamos el codigo SQL
            cur.execute(sqli, (id, nombre, especie, fechaNacimiento, sexo, altura, peso, descripcion))
                
            print("\nSe ha agregado los datos correctamente.")
               
            #Realiza el cambio en la base de datos
            conn.commit()
            
    except Exception as e:
            print("Error: ", str(e))

# Metodo que modifica datos de un animal selecionado por ID de la base de datos
def modificar():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()

            #Pedimos los datos por teclado
            id = int(input("Introduzca id del animal a modificar: "))             
            nombre = str(input("Introduzca nuevo nombre: "))
            especie = str(input("Introduzca nueva especie: "))
            fechaNacimiento = str(input("Introduzca la nueva fecha de nacimiento: "))
            sexo = (input("Introduzca si es macho o hembra (M/H): ")[0])# [0] Recoge solo la primera Letra
            altura = float(input("Introduzca la nueva altura: "))
            peso = float(input("Introduzca el nuevo peso: "))
            descripcion = str(input("Introduzca una nueva descripcion: "))
           
            #Creamos el codigo sql
            sqlu = 'UPDATE animales SET nombre = :nombre, especie = :especie, fecha_nacimiento = :fechaNacimiento, sexo = :sexo, altura = :altura, peso= :peso, descripcion = :descripcion WHERE id = :id'

            #Ejecutamos el codigo sql    
            cur.execute(sqlu, (nombre, especie, fechaNacimiento, sexo, altura, peso, descripcion, id))

            print("\nSe ha actualizado los datos correctamente.")

            #Realiza el cambio en la base de datos
            conn.commit()

    except Exception as e:
            print("Error: ", str(e))

#Metodo que borra un animal introduciendo el ID del animal.
def borrar():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()

            #Pedimos los datos por teclado
            id = int(input("Introduzca el ID del animal que quieres borrar: "))            

            #Creamos el codigo sql
            sqld = 'DELETE FROM animales WHERE id = :id'

            #Ejecutamos el codigo sql    
            cur.execute(sqld, str(id))
            print("\nSe ha Borrado los datos correctamente.")

            #Realiza el cambio en la base de datos
            conn.commit()
            
    except Exception as e:
            print("Error: ", str(e))  

#Metodo que muestra todos los datos de la tabla animales
def mostrarTodo():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()
            #Creamos el codigo sql
            cur.execute('SELECT * FROM animales ORDER BY id')

            #No me hace falta usar el cur.fetchone(): ya que el tabulate lo hace.
                
            ### Mostramos los datos ###
            # Para usar tabulate hay que instalarlo con install tabulate desde la terminal de Python
            # Tablefmt: diseño de la tabla con bordes
            # stralign: centra el texto
            print()         
            print(tabulate(cur, headers=["ID", "Nombre", "Especie", "FechaNacimiento", "Sexo", "Altura", "Peso", "Descripcion"], tablefmt='fancy_grid', stralign='center'))
            print()
            
    except Exception as e:
            print("Error: ", str(e))

# Metodo que muestra los datos de un animal introduciendo su ID   
def mostrarPorID():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()

            id = int(input("Introduzca el ID del animal que quieres mostrar: "))            

            #Creamos el codigo sql
            sqlr2 = 'SELECT * FROM animales WHERE id = :id'
            cur.execute(sqlr2, str(id))
                
            ### Mostramos los datos ###
            # Para usar tabulate hay que instalarlo con install tabulate desde la terminal de Python
            # Tablefmt: diseño de la tabla con bordes
            # stralign: centra el texto
            print()
            print(tabulate(cur, headers=["ID", "Nombre", "Especie", "FechaNacimiento", "Sexo", "Altura", "Peso", "Descripcion"], tablefmt='fancy_grid', stralign='center'))
            print()
            
    except Exception as e:
            print("Error: ", str(e)) 

#Metodo que consulta el oso mmas alto
def consultarOsoMasAlto():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()

            #Ejecutamos el codigo sql 
            cur.execute("SELECT MAX(altura) FROM animales WHERE especie = 'Oso'")
                
            ### Mostramos los datos ###
            # Para usar tabulate hay que instalarlo con install tabulate desde la terminal de Python
            # Tablefmt: diseño de la tabla con bordes
            # stralign: centra el texto
            print()
            print(tabulate(cur, headers=["El oso mas alto mide"], tablefmt='fancy_grid', stralign='center'))
            print()
             
    except Exception as e:
            print("Error: ", str(e))

# Metodo que consulta el elefante que pesa menos
def consultarElefanteMenorPeso():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()
            sql = "SELECT MIN(peso) FROM animales WHERE especie = 'Elefante'"
            #Ejecutamos el codigo sql 
            cur.execute(sql)
                
            ### Mostramos los datos ###
            # Para usar tabulate hay que instalarlo con install tabulate desde la terminal de Python
            # Tablefmt: diseño de la tabla con bordes
            # stralign: centra el texto
            print()
            print(tabulate(cur, headers=["El Elefante con menor peso pesa"], tablefmt='fancy_grid', stralign='center'))
            print()
            
    except Exception as e:
            print("Error: ", str(e))

# Metodo que realiza una consulta que cuenta las especies y agrupa las especies
def consultaGroupByCuentaSexo():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as conn:
            print("Se ha iniciado sesion en la base de datos.")
            # Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()
            sql = "SELECT especie, count(*) FROM animales GROUP BY especie"
            # Ejecutamos el codigo sql 
            cur.execute(sql)
                
            ### Mostramos los datos ###
            # Para usar tabulate hay que instalarlo con install tabulate desde la terminal de Python
            # Tablefmt: diseño de la tabla con bordes
            # stralign: centra el texto
            print()
            print(tabulate(cur, headers=["Especie", "Numero de animales" ], tablefmt='fancy_grid', stralign='center'))
            print()
            
    except Exception as e:
            print("Error: ", str(e)) 

# Metodo que consulta que agrupa por el sexo las especies de los animales
def consultaGroupByCuentaEspecie():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as co:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()
            sql = "SELECT especie, count(*) FROM animales  GROUP BY especie ORDER BY especie"
            #Ejecutamos el codigo sql 
            cur.execute(sql)
                
            ### Mostramos los datos ###
            # Para usar tabulate hay que instalarlo con install tabulate desde la terminal de Python
            # Tablefmt: diseño de la tabla con bordes
            # stralign: centra el texto
            print()
            print(tabulate(cur, headers=["Especie", "Numero de animales" ], tablefmt='fancy_grid', stralign='center'))
            print()
            
    except Exception as e:
            print("Error: ", str(e)) 

# Metodo que contiene los nombres de todos los perros
def arrayNombresPerro():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as co:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos el diccionario
            nombrePerro = []
           
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()
            #Creamos el codigo sql
            cur.execute("SELECT nombre FROM animales WHERE especie = 'Perro' ORDER BY nombre")
            
            cont= 0
            for perros in cur: #Recorrermos los datos del sql para recogerlos               
                for perro in perros:                
                    nombrePerro.append(perro)  #Guardamos los datos en el diccionario
                    cont += 1
                             
            ### Mostramos los datos ###
            print()         
            print("Nombre de los perros que hay:")
            print()
            print(nombrePerro)
            print()
            
    except Exception as e:
            print("Error: ", str(e))    

# Metodo crea un diccionario con las especies que existe
def diccionarioEspecies():
    try :
        with cx_Oracle.connect('JAVAP/JAVAP')as co:
            print("Se ha iniciado sesion en la base de datos.")
            #Declaramos el diccionario
            dicEspecies = dict()
           
            #Declaramos un cursor para recorrer los resultados
            cur = conn.cursor()
            #Creamos el codigo sql
            cur.execute('SELECT especie FROM animales GROUP BY especie ORDER BY especie')
        
            key= 1
            for especies in cur: #Recorrermos los datos del sql para recogerlos               
                for especie in especies:                
                    dicEspecies[key] = especie  #Guardamos los datos en el diccionario
                    key += 1

            ### Mostramos los datos ###        
            print()         
            print("\tContenido del Diccionario")  
            print("\tKey: 'Valor'") 
            print("\t-------------------------")      
            
            print(dicEspecies)
            print()
            
    except Exception as e:
            print("Error: ", str(e))
