from menu import menu, create, find_password, find_apps, change
#1. add a new password
#2. find password by appname
#3. find all sites by email
#4. change password
#E. exit

contra = input("ingrese la contraseña master para ingresar: ")

if contra == "masterkey":
    print("Contraseña correcta!")
else:  
    print("Contraseña Incorrecta! hasta pronto")
    exit()


choice = menu()
while choice != 'E':
    if choice == '1':
        create()
    if choice == '2':
        find_password()
    if choice == '3':
        find_apps()
    if choice == '4':
        change()
    choice = menu()
exit()