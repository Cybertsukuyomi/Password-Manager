import pymysql
import pandas as pd
from tabulate import tabulate


# Funcion que conecta a la base de datos en MySQL
def connect():
    try:
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "password",
            db = "password_manager"
        )
        print("coneccion establecida")
        return connection
    except(Exception, pymysql.Error) as error:
        print(error)

# Funcion que agrega toda la nueva informacion a la base de datos
def create_account(app_name, email, username, password, url):
    try:
        connection = connect()
        cursor = connection.cursor()
        add_account = "INSERT INTO manager (app_name, email, username, password, url ) VALUES (%s, %s, %s, %s, %s) "
        cursor.execute(add_account, (app_name, email, username, password, url))
        connection.commit()
        print("la cuenta a sido agregada")
    except(Exception, pymysql.Error) as error:
        print(error)

# Funcion que busca la contraseña por medio del sitio web
def find_app(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        find_data = "SELECT * FROM manager WHERE app_name = %s"
        cursor.execute(find_data, app_name)
        connection.commit()
        result = cursor.fetchone()
        print("la contraseña es: " + result[3])
    except (Exception, pymysql.Error) as error:
        print(error)

# Funcion que busca todas las cuentas por medio del correo electronico
def find_accounts(email):
    try:
        connection = connect()
        cursor = connection.cursor()
        accounts_data = "SELECT * FROM manager WHERE email = %s"
        cursor.execute(accounts_data, email)
        connection.commit()
        #Obtener todos los resultados
        result = cursor.fetchall()
        print(" \n" + "RESULTADO" + " \n")
        #Crear un dataframe con el resultado y colocar headers            
        df = pd.DataFrame(result, columns =['sitio web', 'Email', 'Nombre de Usuario', 'Contraseña', 'URL'])
        #desactivar el index y mostrar formato psql
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

    except (Exception, pymysql.Error) as error:
        print(error)

# Funcion que cambia la contraseña de una cuenta existente
def password_change(app_change, new_password):
    try:
        connection = connect()
        cursor = connection.cursor()
        update_password = "UPDATE manager SET password = %s WHERE app_name = %s"
        change = (new_password, app_change)
        cursor.execute(update_password, change)
        connection.commit()
        print("El cambio ha sido realizado")
    except (Exception, pymysql.Error) as error:
        print(error)