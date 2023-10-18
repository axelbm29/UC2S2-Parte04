def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido

max_intentos = 2
min_intentos = 0


while min_intentos < max_intentos:
    usuario = str(input("Escribir nombre de usuario: "))
    clave = str(input("Escribir clave: "))
    if usuario == leer_archivo("login.txt") and clave == leer_archivo("clave.txt"):
        print("Datos Persona")
        print("1. Listar personas")
        print("2. Agregar personas")
        print("3. Salir")
        break
    else:
        print("\n" + "*" * 30)
        print("DATOS INCORRECTOS")
        print("*" * 30 + "\n")
        min_intentos += 1