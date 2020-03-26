# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    # texto=re.sub("\*\*\*(...)*\*\*\*", '', texto) tas re gil fran, esto no andaba
    #texto=re.sub("\*\*\*(.)*\*\*\*\n", '', texto) esto es para sólo una linea
    texto=re.sub("( )*\*\*\*(.|\\n)*\*\*\*(\\n)*", '', texto) #esto anda para varias lineas
    texto=re.sub("( )*//(.)*\\n", '', texto) 
    return texto

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
