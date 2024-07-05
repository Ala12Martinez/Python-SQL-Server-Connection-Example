import pyodbc

# Configura tus datos de conexión
server = 'ALANMARTINEZ12'  # Nombre del servidor
database = 'prueba12'  # Nombre de la base de datos

# Establece la conexión usando autenticación de Windows
try:
    connection = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    )
    print("Conexión exitosa")
    
    # Ejecuta una consulta de ejemplo
    cursor = connection.cursor()
    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

except pyodbc.Error as e:
    print("Error en la conexión: ", e)

finally:
    # Cierra la conexión
    try:
        connection.close()
        print("Conexión cerrada")
    except NameError:
        print("La conexión no fue establecida, por lo tanto, no necesita ser cerrada.")
