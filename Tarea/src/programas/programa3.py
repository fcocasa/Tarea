# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    texto=re.sub('( )*\*\*\*(.|\\n)*\*\*\*(\\n)*', '', texto)
    texto=re.sub('( )*//(.)*\\n', '', texto)
    #borrado comentarios

    match = re.search(r'\w\s[\w_]\([\w\s_:<>,]\)',texto)
    if match:
        print("_______")
        print match.group()
        print("_______")

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
