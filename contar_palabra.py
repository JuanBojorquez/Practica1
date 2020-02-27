#!/usr/bin/python3
import lector
import argparse

def contar_palabras_unicas(dp):
#Pasa el valor total del arreglo de palabras que nunca se repitieron.
    total=len(set(dp))
    return total

def contar(texto,stopwords):
'''
En este metodo se crearon 2 diccionarios, 1 para palabras stopwords 
y el otro para el otro tipo de palabras.
Ademas se contaron las palabras utilizadas, si se repetia se sumaba o si era una palabra unica 
'''
    lista_palabras= texto.split(" ")
    total_palabras=len(lista_palabras)
    dpc = dict()
    dps = dict()
    
    for palabra in lista_palabras:
        p=palabra.lower().strip(".,")
        if p in stopwords:
            if p in dps:
                dps[p]+=1
            else:
                dps[p] = 1
        else:
            if p in dpc:
                dpc[p]+=1
            else:
                dpc[p]=1
                
    sumapc=suma_diccionario(dpc)
    sumaps=suma_diccionario(dps) 
    pcu=contar_palabras_unicas(dpc)
    pcs=contar_palabras_unicas(dps)
    total_pu=pcu+pcs
    print("Total de palabras clave unicas: ",pcu)
    print("Total de palabras stopwords unicas:", pcs)
    print("Total de palabras unicas: ",total_pu)
    print("Total de palabras:", total_palabras)
    print("Palabras clave: ", sumapc)
    print("Palabras stopwords: ",sumaps)
    
def suma_diccionario(dp):
#Se suman todas las palabras que se encuentran en el diccionario.
    suma=0
    for k,v in dp.items():
        suma+=v
    return suma
        
    
def main(archivo,archivo_stopwords):
  texto = lector.leer_archivo(archivo)
  stopwords= lector.leer_stopwords(archivo_stopwords)
  print(stopwords)
  contar(texto,stopwords)
  
  
  
if __name__ == "__main__":
  parser= argparse.ArgumentParser()
  parser.add_argument('-a','--archivo', dest='archivo', help="nombre de archivo", required=True)
  parser.add_argument('-s','--stopwords', dest='archivo_stopwords', help="nombre de archivo stopwords", required=False,default= "spanish_stopwords.txt")
  args=parser.parse_args()
  archivo= args.archivo
  archivo_sw= args.archivo_stopwords
  main(archivo,archivo_sw)