# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    texto=re.sub(r"( )*\*\*\*(.|\n)*\*\*\*\n",'', texto) #programa 1
    texto=re.sub(r'( )*//(.)*\n', '', texto) 
    
    texto = re.sub(r'funcion\s[\w_]*\((.)*\{',"",texto) #sacamos la primera linea que no tiene funciones
    
    nobool = len(re.findall(r'(\+|-[^>]|\*|/)', texto, flags=0))
    booleanas = len(re.findall(r'(==|&&|[^-]>|<|>=|<=)', texto, flags=0))
    texto= "booleanas: "+str(booleanas)+"\nno booleanas: "+str(nobool)
    
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
