from database_manager import create_account, find_app, find_accounts, password_change

# Muestra las opciones del menu
def menu():
    print(' ')
    print('-'*30)
    print('-'*12 + ' Menu ' + '-'*12)
    print('-'*30)
    print(' ')
    print('1. Agregar nueva cuenta con contraseña ')
    print('2. Encontrar contraseña por sitio web ')
    print('3. Encontrar todas las cuentas por medio de correo electronico ')
    print('4. cambiar contraseña ')
    print('E. salir')
    print('-'*30)
    print(' ')
    return input('colocar el numero de la opcion: ')

#Crea una nueva cuenta con app name, email, username, password y url
def create():
    app_name = input("Ingrese el nombre de de la aplicacion o sitio web: ")
    email = input("Ingrese el correo utilizado del sitio web: ")
    username = input("Ingrese el username colocado, si no tiene username ingrese N/A: ")
    password = input("Ingrese la contraseña utilizada: ")
    url = input("Ingrese el link del sitio web: ")
    create_account(app_name, email, username, password, url)
    
# Busca la columna por medio del nombre del sitio web
def find_password():
    app_name = input("Ingrese el nombre del sitio web: ")
    find_app(app_name)

# Busca todas las cuentas que usen el correo electronico ingresado
def find_apps():
    email = input("Ingrese el correo electronico: ")
    find_accounts(email)

# Cambia el valor de la contraseña del sitio web ingresado    
def change():
    app_change = input("Ingrese el nombre del sitio web que cambio la contraseña: ")    
    new_password = input("Ingrese la nueva contraseña: ")
    password_change(app_change, new_password)
    

    
