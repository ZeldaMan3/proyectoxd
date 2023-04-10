import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Exilenova123",
  database="mydatabase"
)

mycursor = mydb.cursor()

def Ver():
  mycursor.execute("SELECT * FROM customers")
  for x in mycursor:
    print(x)

def Crear():
 val = (input("Nombre: "), input("Direccion:"))
 sql = ("INSERT INTO customers (name, address) VALUES (%s, %s)")
 mycursor.execute(sql,val)
 mydb.commit()
 print(mycursor.rowcount, "Valor agregado.")

def Modificar():
  name = input("Ingresa el nombre del sujeto: ")
  update = input("Ingresa la direccion nueva: ")
  sql = "UPDATE customers SET address=%s WHERE name  = %s"
  mycursor.execute(sql, (update, name))
  mydb.commit()
  print("1 Valor modificado, ID:", mycursor.lastrowid)

def Eliminar():
  name = input("Ingresa el nombre del sujeto: ")
  sql = "DELETE FROM customers WHERE name  = %s"
  mycursor.execute(sql, (name,))
  mydb.commit()
  print("1 Valor eliminado, ID:", mycursor.lastrowid)


"""mycursor.execute("SELECT * FROM customers")

for x in mycursor:
  print(x)
"""
def CRUD():

 print("Por favor ingresa 1 de las 4 opciones: 1 Crear usuario, 2 Modificar usuario, 3 Eliminar Usuario, 4 Ver usuario, 5 para salir" )
 condition = int(input())

 if condition == 1:
   print("Crear Usuario")
   Crear()
   CRUD()
 elif condition == 2:
   print("Modificar Usuario")
   Modificar()
   CRUD()


 elif condition == 3:
   print("Eliminar Usuario")
   Eliminar()
   CRUD()


 elif condition == 4:
   print("Ver Usuario")
   Ver()
   CRUD()

 elif condition == 5:
   print("Adios!")

CRUD()

