#!/usr/bin/python3
import argparse
import lector
import contar_palabra

def obten_cita(texto,inicio,cuenta):
    lista=texto.split(" ")
    longitud=len(lista)
    if ((inicio+cuenta)<longitud):
      lista_palabras=lista[inicio:inicio+cuenta]
      cita=" ".join(lista_palabras)
    else:
      cita=""
    return cita
    
def main( archivo, inicio,cuenta ):
    texto=lector.leer_archivo(archivo)
    cita=obten_cita(texto,inicio,cuenta)
    print("Cita: ",cita)
    stopwords=lector.leer_stopwords("/home/andromeda/gilberto/spanish_stopwords.txt")
    contar_palabra.contar(cita,stopwords)
    
if __name__ == "__main__":
  parser= argparse.ArgumentParser()
  parser.add_argument('-a','--archivo', dest='archivo', help="nombre de archivo", required=True)
  #parser.add_argument('-s','--stopwords', dest='archivo_stopwords', help="nombre de archivo stopwords", required=False,default= "spanish_stopwords.txt")
  parser.add_argument('-i','--inicio', dest='inicio', help="numero donde iniciara la cita", required=True,default=9,type=int)
  parser.add_argument('-c','--cuenta', dest='cuenta', help="conteo", required=True, default= 10,type=int)
  args=parser.parse_args()
  archivo= args.archivo
 # archivo_sw= args.archivo_stopwords
  inicio=args.inicio
  cuenta=args.cuenta
  main(archivo,inicio,cuenta)