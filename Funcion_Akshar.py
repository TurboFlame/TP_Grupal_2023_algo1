'''
Created on 26 oct. 2023
'''
Created on 24 oct. 2023

@author: Carlos Reyes Y Guillermo Gallardo
'''
def Cifrado_Atbash(mensaje):
    """
    #Esta funciona se dedica a leer los caracteres de un mensaje y aplicar en cada uno el cifrado de atbash
    #ademas tambien esta funcion usa un diccionario para tener en cuenta valores especiales como acentos y
    #la letra "ñ"
    
    Las siguientes pruebas aplican atbash al mensaje ingresado:
    
    >>> Cifrado_Atbash("Hola Mundo 12345")
    'sLOZ nFMWL 12345'

    >>> Cifrado_Atbash("Somos el grupo Losanges!!")
    'hLNLH VO TIFKL oLHZMTVH!!'

    >>> Cifrado_Atbash("Bienvenido al codigo atbash de nuestro proyecto!")
    'yRVMEVMRWL ZO XLWRTL ZGYZHS WV MFVHGIL KILBVXGL!'

    >>> Cifrado_Atbash("Qué prueba te gustaría realizar primero?")
    'jFV KIFVYZ GV TFHGZIRZ IVZORAZI KIRNVIL?'

    >>> Cifrado_Atbash("hoy es un lindo día para programar")
    'SLB VH FM ORMWL WRZ KZIZ KILTIZNZI'
    
    >>> Cifrado_Atbash("hay muchos ñandues que cazar")
    'SZB NFXSLH niZMWFVH JFV XZAZI'
    
    >>> Cifrado_Atbash("@@@!!??**42")
    '@@@!!??**42'
    
    >>> Cifrado_Atbash("Algoritmos y Programación 1")
    'zOTLIRGNLH B kILTIZNZXRMM 1'
    
    >>> Cifrado_Atbash("El mejor GRUPO DEL MUNDO@!")
    'vO NVQLI tifkl wvo nfmwl@!'
    
    >>> Cifrado_Atbash("En las montañas , los niños juegan")
    'vM OZH NLMGZniZH , OLH MRniLH QFVTZM'
    
    """
    resultado = ""
    acentos = { 'á': 'Z', 'é': 'V', 'í': 'R', 'ó': 'M', 'ú': 'N',
        'Á': 'z', 'É': 'v', 'Í': 'r', 'Ó': 'm', 'Ú': 'n','ñ':"ni","Ñ":"NI"}
    
    for caracter in mensaje:
        if caracter in acentos:
            resultado += acentos[caracter]
        elif caracter.isalpha():
            if caracter.islower():
                resultado += chr(122 - ord(caracter) + 65)
            elif caracter.isupper():
                resultado += chr(90 - ord(caracter) + 97)
        else:
            resultado += caracter
    return resultado
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(Cifrado_Atbash("HOLA MUNDO"))

@author: agusn
'''
