#!/usr/bin/python3
import os
import argparse
import lector
import tfidf
import clean

def carga_textos(folder,termina):
  try:
    lista_textos=[]#lista de contenidos
    lista_archivos=os.listdir(folder)
    lista_txt=[archivo for archivo in lista_archivos if archivo.endswith(termina)]
    #a leer!
    for archivo in lista_txt:
      texto=lector.leer_archivo(os.path.join(folder,archivo))
      texto_limpio=clean.clean_text(texto)
      lista_textos.append(texto_limpio)
  except IOError as e:
    pirnt(e)
    lista_textos=[]
  return lista_textos
  
def obten_set_palabras(lista_textos):
  try:
    set_palabras_unicas=set()
    for texto in lista_textos:
      set_palabras=texto.split(" ")
      set_palabras_unicas=set_palabras_unicas.union(set_palabras)
  except:
    print("error al obttener paabras unicas")
    set_palabras_unicas=set()
  return set_palabras_unicas
  
def obten_lista_palabras(textos):
  lista_palabras=[]
  for texto in textos:
    palabras=texto.split(" ")
    lista_palabras.append(palabras)
  return lista_palabras

def main(folder, termina, numero, output):
    textos=carga_textos(folder,termina)
    
    print(len(textos))
    print(len(textos[0]))
    set_palabras_unicas=obten_set_palabras(textos)
    print(len(set_palabras_unicas))
    lista_palabras_textos=obten_lista_palabras(textos)
    print(len(lista_palabras_textos))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--folder', dest='folder', help="nombre de folder", required=True,)
    parser.add_argument('-t','--termina', dest='termina', help="con que termina el archivo", required=True,default='txt')
    parser.add_argument('-n','--numero', dest='numero', help="numero de palabras a aextraer", required=False,default=10,type=int)
    parser.add_argument('-o','--output', dest='output', help="nombre del archivo de salida", required=False)
    args=parser.parse_args()
    folder=args.folder
    numero=args.numero
    termina=args.termina
    output=args.output
    main(folder,termina,numero,output)