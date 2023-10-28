'''
Created on 12 oct. 2023

@author: agusn
'''

import doctest
from funciones_auxiliares import reemplazador_ñ



def cesar_encoder(contraseña,clave):
    """
    >>> cesar_encoder("hola", 5)
    'mtqf'
    >>> cesar_encoder("aña",42)
    'qdyq'
    >>> cesar_encoder("5644", 3)
    '8977'
    >>> cesar_encoder("que onda", -3)
    'nrb lkax'
    >>> cesar_encoder("3", -4)
    '9'
    >>> cesar_encoder("AÑA", -4)
    'WJEW'
    >>> cesar_encoder("hola buenos dias", 50000)
    'jqnc dwgpqu fkcu'
    >>> cesar_encoder("HOLA QUE TAL", -50000)
    'FMJY OSC RYJ'
    >>> cesar_encoder("al_GORIT-m0s_1", 5)
    'fq_LTWNY-r5x_6'
    >>> cesar_encoder("chau", -5)
    'xcvp'
    
    """
    contraseña=reemplazador_ñ(contraseña)
    
    
    contraseña_codificada=""
    letras_invalidas="áéíóúÁÉÍÓÚ"

    for letra in contraseña:
        if letra.islower() and not letra in letras_invalidas:
            
            unicode=ord(letra)
            contraseña_codificada+=chr(97+(unicode+clave-97)%26).lower()
            
        elif letra.isupper() and not letra in letras_invalidas:
            
            unicode=ord(letra)
            contraseña_codificada+=chr(65+(unicode+clave-65)%26).upper()
            
            
        elif letra.isdigit():
            
            unicode_int=int(ord(letra))
            contraseña_codificada+=chr((unicode_int+clave-48)%10+48)
            
            
            
            
            
            
        else:
            contraseña_codificada+=letra
                
            
            

    
    return contraseña_codificada

print(doctest.testmod())



#Funcion creada por Agustin Reyes
#Esta funcion tiene el proposito de desplazar los caracteres ingresados a la derecha o izquierda en el abecedario o
#la serie de numeros del 0 al 9 y devolver un string con estos caracteres.
# La cantidad de espacios y el sentido en que se desplazan es determinado por la clave ingresada.
# Caracteres que no sean digitos o letras del abecedario permanecen sin cambios.
