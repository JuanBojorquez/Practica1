#!/usr/bin/python3
import lector
import argparse

def contar(texto,stopwords):
  texto=lector.leer_archivo(archivo)
  lista_palabras=texto.split(" ")
  total_palabras=len(lista_palabras)
  dpc=dict()
  dps=dict()
  
  for palabra in lista_palabras:
    p=palabra.lower().strip(".,")
    if p in stopwords:
      if p in dps:
        dps[p]+=1
      else:
        dps[p]=1
    else:
      if p in dpc:
        dpc[p]+=1
      else:
        dpc[p]=1
    sumapc=suma_diccionario(dpc)
    sumaps=suma_diccionario(dps)
    print(total_palabras,sumapc,sumaps)
    pcu=contar_palabras_unicas(dpc)
    pcs=contar_palabras_unicas(dps)
    total_pu=pcu+pcs
    
def contar_palabras_unicas(dp):
  total=len(set(dp))
  return total

def suma_diccionario(dp):
  suma=0
  for k,v in dp.items():
    suma+=v
  return suma
    
def main( archivo, archivo_sw):
  texto=lector.leer_archivo(archivo)
  stopwords=lector.leer_stopwords(archivo)
  contar(texto,stopwords)
  
if __name__ == "__main__":
  parser= argparse.ArgumentParser()
  parser.add_argument('-a','--archivo', dest='archivo', help="nombre de archivo", required=True)
  parser.add_argument('-s','--stopwords', dest='archivo_sw', help="nombre de archivo", required=False, default='stop_words.txt')
  args=parser.parse_args()
  archivo_sw= args.archivo_sw
  archivo= args.archivo
  main(archivo,archivo_sw)