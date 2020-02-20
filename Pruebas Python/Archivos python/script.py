# preparar funcion para las opciones del script
import os

# Funcion auxiliar que comprueba errores en el archivo css


def cssFile(path_file):
    path_file = open(path_file, 'r')
    for linea in path_file:
        if 'Error' in linea:
            print(linea)
    path_file.close()
    print("Es una archivo")
    return False

# Funcion que comprueba todos los archivos de un directorio


def pruebaCss():

    # variable para la eleccion en el menu
    opcion = None
    # variable para la opcion elegida
    num = 0
    # Textos para el menu
    print("1. Comprobar archivos .css")
    print("2. Salir")
    # bucle
    while(opcion != 2):
        try:
            # variable introducida por consola para ver la opcion
            num = int(input("Elige una opcion: "))
            if num == 2:
                print("Happy Styling!!!")
                break
            else:
                # variable de entrada para ruta
                path_file = str(input("introduce una ruta: "))
                if path_file.endswith(".css"):
                    cssFile(path_file)
                else:
                    # iteracion para entrar desde la ruta hasta el ultimo archivo
                    for subdir, dirs, files in os.walk(path_file):
                        # recorre cada archivo dentro de la ruta
                        for file in files:
                            # union de la ruta para poder leer el archivo
                            filepath = subdir + os.sep + file
                            print(filepath)
                            # comprobacion que es un archivo .css
                            if filepath.endswith(".css"):
                                # uso de la funcion auxiliar para comprobar el error
                                cssFile(filepath)
        # texto para controlar que la opcion introducida debe ser la correcta
        except ValueError:
            print('Error, introduce una opcion correcta')


# lanza el script
pruebaCss()
