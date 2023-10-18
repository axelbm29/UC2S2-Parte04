import gestion_aplicacion
import sys

def menu():
    print("\n" + "*** Datos Persona ****")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")

def agregar():
    print("-- Agregar Datos en un archivo --")
    archivo = input("\n" + "Archivo: ").strip()
    contenido = input("Contenido: ")
    gestion_aplicacion.agregar_personas(archivo, contenido)

def listar():
    print("-- Mostrar nombres de un archivo -- ")
    archivo = input("Archivo: ")
    
    contenido = gestion_aplicacion.listar_personas(archivo)
    
    if contenido:
        lineas = contenido.split('\n')
        for i, linea in enumerate(lineas, start=1):
            if linea.strip():
                print(f"\t{i}. {linea.strip()}")
    else:
        print("El archivo está vacío o no existe.")

def salir():
    print("Gracias por su visita....")
    sys.exit(0)

def error():
    print("Opción incorrecta" + "\n")


max_intentos = 2
min_intentos = 0


while min_intentos <= max_intentos:
    usuario = str(input("Escribir nombre de usuario: "))
    clave = str(input("Escribir clave: "))
    if usuario == gestion_aplicacion.leer_archivo("login.txt") and clave == gestion_aplicacion.leer_archivo("clave.txt"):
        opcion = 1
        while opcion!=5:
            menu()
            opcion = int(input("\n" + "opcion: "))
            if opcion == 1:
                listar()
            elif opcion == 2:
                agregar()
            elif opcion == 3:
                salir()
            else:
                error()
    else:
        print("\n" + "*" * 30)
        print("DATOS INCORRECTOS")
        print("*" * 30 + "\n")
        min_intentos += 1