# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
#    texto = re.sub(r"( )*\*\*\*(.|\n)*\*\*\*\n", '',texto)  # esto anda para varias lineas,  no pudimos usar \s puesto que incluye a \n
#    texto = re.sub(r'( )*//(.)*\n', '', texto)
#    texto = re.sub(r'funcion\s[\w_]*\((.)*\{' ,'', texto)  # tomamos primera linea que tiene función
#
#    var = re.findall(r'\w*\s*:\s*\w*\s*=\s*(?: |\w|\(|\)||\+|-|\*|/)*', texto, flags=0)
#
#    for x in var:
#        print(x)
    texto = re.sub(r'funcion\s*(.)*\n','',texto)
#    print(s)
    #x = re.finditer(r"\w*\s*:\s*(Real|Entero|Booleano)(\s)*=(\s*)(\w)*(\n|\(\w*\))",texto,re.S)
    x = re.finditer(r"\w*\s*:\s*(Real|Entero|Booleano)(\s)*=(\s*)[^\n]*",texto,re.S)
    devolver = '';
    for match in x:
        devolver_aux = re.sub(r'(\s)*:(\s)*(Real|Entero|Booleano)(\s)*=(\s*)',',',match.group())
        #devolver_aux = re.sub(r'\n','',match.group())
        devolver_aux = re.sub(r'\s*->(.)*','',devolver_aux)
        devolver  =devolver+'('+devolver_aux + ')\n'
        #print(match.group())
    devolver = re.sub(r'\n\n(\n)*','',devolver)
#    devolver = list(devovler)
#    devolver = devolver[:-1]
    devolver = devolver.rstrip("\n")
    return (devolver)

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