# diccionario para almacenar los datos de usuario
database = {}
# funcion para registrar el usuario nuevo y contraseña en el diccionario
def datos_usuarios():
    nombre_de_usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    database[nombre_de_usuario] = contraseña
#funcion para mostrar el usuario y contraseña
def mostrar_los_datos():
    for dato in database.keys():
        print("Usuario: "+ dato + " Contraseña: " + database[dato])
#funcion para que el usuario inicie sesion
def login():
    usuario_input = input("Ingrese el nombre de usuario: ")
    if(database.get(usuario_input) == None):
        while database.get(usuario_input) == None:
            usuario_input = input("Ups, usuario Incorrecto. Por favor, ingrese nuevamente: ")
        print("Genial, usuario correcto")
    contraseña_input = input("Ingrese la contraseña: ")
    while contraseña_input != database[usuario_input]:
            contraseña_input = input("Ups, contraseña incorrecta. Por favor, ingrese otra contraseña: ")
    print("Contraseña correcta")
    print("Inicio de sesion exitosa")

print("Ingreso de usuario")
datos_usuarios()
print("Los datos de los usuarios son: ")
mostrar_los_datos()
print("Inicio de sesion")
login()

with open("test.txt", "w") as testtxt:
    for dato in database.keys():
        testtxt.write(dato + "\n")
    for dato in database.values():
        testtxt.write(dato + "\n")
testtxt.close
