#!/usr/bin/python3
import argparse

def leer_archivo (archivo):
    #archivo = "/tmp/episodio4.txt" 
  try:
  
    with open(archivo,"r") as fh:
    
      texto =fh.read()
    
      lista=texto.splitlines()
    
      texto_limpio=" ".join(lista)
      
  except:
    
    texto_limpio=""
  
  return texto_limpio
    
    #fc = open(archivo,"r") # r = reading: lectura 

    #texto = fc.read() 

    #lineas = texto.splitlines() 

    #texto_limpio = " ".join(lineas) 
  
    #return texto_limpio
    
def leer_stopwords(archivo):
     try:
             with open(archivo,"r") as fh:
                     lista=fh.readlines()
             lista_palabras=[palabra.strip("\n") for palabra in lista
     except:
             lista_palabras=[]
     return set(lista_palabras)

    
def contar_palabras(texto):
    palabras = texto.split(" ") 

    dp = dict() 

    for palabra in palabras: 

      p = palabra.strip(",.") 

      if p in dp: 

         dp[p]+= 1 

      else: 

         dp[p] = 1 
    if "" in dp:
    
      del (dp[""])
    return dp
    

    
def imprime_diccionario(dp, minimo):
     lista=[(k,v) for k,v in dp.items() if v>=minimo]
     lista_ordenada=sorted(lista, key=lambda x:x[1], reverse=True)
     #print(lista_ordenada)
     for tupla in lista_ordenada:
             print(tupla[0],"= ",tupla[1])
     return


def main(archivo, minimo):
    ###main() recibe nombre de archivo
    ###lo abre y cuenta las palabras repetidas
    ###
    texto=leer_archivo(archivo)
    dip=contar_palabras(texto)
    #print(dip)
    imprime_diccionario(dip,minimo)
    
if __name__=="__main__":
    #archivo="/home/andromeda/Juan/capitulo4.txt" 
    #main(archivo) 
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--archivo', dest='archivo', help='nombre de archivo',required=True)
    parser.add_argument('-m','--minimo', dest='minimo', help='minimo de repeticiones',required=False,type=int,default=3)
    args=parser.parse_args()
    minimo=args.minimo
    archivo=args.archivo
    main(archivo,minimo)