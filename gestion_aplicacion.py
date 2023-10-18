def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido

def listar_personas(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido

def agregar_personas(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()