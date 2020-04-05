# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    # Implementar programa
    #paso el texto por el programa 1 para borrarle los comentarios
    texto = re.sub("( )*\*\*\*(.|\\n)*\*\*\*(\\n)*", '', texto)
    texto = re.sub("( )*//(.)*\\n", '', texto)

    i = len(re.findall(' si ', texto, flags=0))

    k = len(re.findall(' para cada ', texto, flags=0))

    j = len(re.findall(' para ', texto, flags=0))
    j = j-k #para descontar los "para cada"

    l = len(re.findall(' mientras ', texto, flags=0))

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
