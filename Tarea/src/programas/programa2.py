# -*- coding: utf-8 -*-
import re
import sys

#import programa1
#no funciona

def programa(texto):
    #paso el texto por el programa 1 para borrarle los comentarios
    texto = re.sub("( )*\*\*\*(.|\\n)*\*\*\*(\\n)*", '', texto)
    texto = re.sub("( )*//(.)*\\n", '', texto)

    i=0
    sis = re.findall('( )*si ', texto, flags=0)
    for x in sis:
        i = i+1

    k=0
    pcs = re.findall('( )*para cada ', texto, flags=0)
    for x in pcs:
        k = k+1

    j=0 #reconoce tambien los "para cada"
    paras = re.findall('( )*para ', texto, flags=0)
    for x in paras:
        j = j+1
    j = j-k #para descontar los "para cada"

    l=0
    mientrass = re.findall('( )*mientras ', texto, flags=0)
    for x in mientrass:
        l = l+1
    texto = "si: " + str(i) + "\npara: " + str(j) + "\npara-cada: " + str(k) + "\nmientras: " + str(l)
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
