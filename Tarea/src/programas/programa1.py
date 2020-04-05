# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    texto=re.sub(r"( )*\*\*\*(.|\n)*\*\*\*\n",'', texto) #esto anda para varias lineas,  no pudimos usar \s puesto que incluye a \n
    texto=re.sub(r'( )*//(.)*\n', '', texto) 
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
