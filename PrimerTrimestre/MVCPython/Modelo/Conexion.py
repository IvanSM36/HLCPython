import cx_Oracle
from tabulate import tabulate

#Creamos la conexión
dsn = cx_Oracle.makedsn(host='localhost', port=1521, sid='xe')
conn = cx_Oracle.connect(user="JAVAP", password="JAVAP", dsn=dsn)

#Declaramos un cursor para recorrer los resultados
c = conn.cursor()

#Ejecutamos la sentencia correspondiente
#c.execute('''INSERT INTO
#                persona values('101','Ravi', 20)''')
 
# Sentencia select para consultar la base de datos 
c.execute('select * from animales')
#for reg in c.fetchmany():
#    print(reg)
#for reg in conn.fetchone():
#   print(reg)
# Para usar tabulate hay que instalarlo con install tabulate desde la terminal de Python
# Tablefmt: diseño de la tabla con bordes
# stralign: centra el texto

# Mostramos los datos
#print()
#for registro in c:
print(tabulate(c, headers=["ID", "Nombre", "Especie", "Raza", "Edad", "FechaNacimiento"], tablefmt='fancy_grid', stralign='center'))
#print()

#Cerramos la conexión
#conn.commit()
conn.close()