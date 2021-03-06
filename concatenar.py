#!/usr/bin/python3
import lector
import argparse
import os

def crear_archivo(output, contenidos):
#Se crea un archivo que es definido al ingresar el comando con los parametros y se escriben los textos conectados.
    with open(output,'w') as f:
        for item in contenidos:
            f.write("{}\n".format(item))
            
def conca_archivos(archivos_new, folder):
'''
Se guardan las palabras de los archivos 
y se juntan en una misma lista
'''
    contenidos = []
    for archivo in archivos_new:
        texto = lector.leer_archivo(os.path.join(folder,archivo))
        contenidos.append(texto)
    return contenidos
    
def busqueda_archivos(folder, inicia, termina):
'''
El metodo os.listdir(folder) sirve para ver todos los archivos que se encuentran en el directorio.
Depues se seleccionaran los documentos tomando en cuenta los metodos archivo.starswith y archivo.endswith
'''
    listado_archivos = os.listdir(folder)
    archivos_new = []
    for archivo in listado_archivos:
        if archivo.endswith(termina) and archivo.startswith(inicia):
            archivos_new.append(archivo)
            
    archivos_new.sort()
    return archivos_new

def main(folder, inicia, termina, output):
    archivos = busqueda_archivos(folder, inicia, termina)
    contenidos = conca_archivos(archivos, folder)     
    crear_archivo(output, contenidos)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--folder', dest='folder', help="nombre de folder", required=True,)
    parser.add_argument('-i','--inicia', dest='inicia', help="con que inicia el archivo", required=False, default="")
    parser.add_argument('-t','--termina', dest='termina', help="con que termina el archivo", required=True)
    parser.add_argument('-o','--output', dest='output', help="nombre del archivo de salida", required=True)
    args=parser.parse_args()
    folder=args.folder
    inicia=args.inicia
    termina=args.termina
    output=args.output
    main(folder,inicia,termina,output)