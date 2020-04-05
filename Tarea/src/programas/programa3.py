# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
     texto=re.sub(r"( )*\*\*\*(.|\n)*\*\*\*\n",'', texto) #esto anda para varias lineas,  no pudimos usar \s puesto que incluye a \n
    texto=re.sub(r'( )*//(.)*\n', '', texto) 
    #borrado comentarios

    #match = re.search(r'\w\s[\w_]\([\w\s_:<>,]\)',texto)
    match = re.search(r'funcion\s[\w_]*\((.)*\{',texto)  #tomamos primera linea que tiene función, hasta el primer parentesis ")"
    nombreFuncion = re.sub(r'funcion ',"",match.group()) #sacamos funcion
    parametros = nombreFuncion
    retorno= nombreFuncion
    nombreFuncion = re.sub(r'\((.)*',"",nombreFuncion)  #sacamos param, y obtenemos nombreFunc
    parametros=re.sub(r'[\w_]*\(',"",parametros) #
    parametros=re.sub(r'\)(.)*',"",parametros)
    retorno =re.sub(r'(.)*\)',"",retorno) #sacamos desde funcion hasta fin de param ")"
    retorno =re.sub(r'\s->\s',"",retorno) #sacamos si es q tiene "->"
    retorno =re.sub(r'(\s)*\{',"",retorno) #sacamos desde funcion hasta ->
    
    texto=nombreFuncion
    if parametros!="":
        texto=texto+"\n"+parametros
    if retorno!="":
        texto=texto+"\n"+retorno
    

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
