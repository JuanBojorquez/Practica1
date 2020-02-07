#!/usr/bin/python3
import argparse

def leer_archivo( archivo ):
  try:
      with open(archivo,"r") as fh:
        texto = fh.read() 
        lineas = texto.splitlines()  
        texto_limpio = " ".join(lineas)
  except:
      texto_limpio=""
      print("Error Error Error Error Error Error Error Error Error Error")
  return texto_limpio
    

def contar_palabras( texto ):
    palabras = texto.split(" ") 
    dp = dict() 
    for palabra in palabras: 
        p = palabra.strip(",.") 
        if p in dp: 
           dp[p]+= 1
        else: 
          dp[p] = 1
    del(dp[""]) 
    return dp

def imprime_diccionario(dps, minimo):
    lista= [(k,v) for k,v in dps.items() if v >= minimo]
    lista_ordenada = sorted(lista, key= lambda x:x[1], reverse=True)
    for tupla in lista_ordenada:
        print(tupla[0],"= ",tupla[1])
    return

def leer_stopwords(archivo):
     try:
         with open(archivo,'r') as fh:
             lista=fh.readlines()
         lista_palabras=[palabra.strip("\n") for palabra in lista]
         lista_palabras[0]='a'
     except:
         print("Excepcion")
         lista_palabras=[]
     return set(lista_palabras)

def limpia_diccionario(dp, set_stopwords):
    ndp={}
    for k,v in dp.items():
        if k.lower() not in set_stopwords:
            ndp[k]=v
    return ndp

def main( archivo, minimo ):
    texto = leer_archivo( archivo )
    dip   = contar_palabras( texto )
    stop_words= leer_stopwords("/home/andromeda/gilberto/spanish_stopwords.txt")
    ndp = limpia_diccionario(dip,stop_words)
    #print(dip)
    imprime_diccionario(ndp,minimo)

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument('-a','--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument('-m','--minimo', dest='minimo', help="minimo de repeticiones", required=False,type=int,default=3)
    args=parser.parse_args()
    minimo= args.minimo
    archivo= args.archivo
    main(archivo,minimo)
