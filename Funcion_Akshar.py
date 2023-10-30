'''
Created on 25 oct. 2023

@author: Carlos reyes y Guillermo Gallardo
'''
def caracteres_especiales():
    return {
        "á": "Z", "é": "V", "í": "R", "ó": "M", "ú": "N",
        "Á": "z", "É": "v", "Í": "r", "Ó": "m", "Ú": "n",
        "ñ": "ni", "Ñ": "NI",
        "0": "9", "1": "8", "2": "7", "3": "6", "4": "5",
        "5": "4", "6": "3", "7": "2", "8": "1", "9": "0"
    }

def Cifrado_Atbash(mensaje):
    """
    Esta función se dedica a leer los caracteres de un mensaje y aplicar en cada uno el cifrado de Atbash.

    Las siguientes pruebas aplican Atbash al mensaje ingresado:

    >>> Cifrado_Atbash("Hola Mundo 12345")
    'sLOZ nFMWL 87654'

    >>> Cifrado_Atbash("Somos el grupo Losanges!!")
    'hLNLH VO TIFKL oLHZMTVH!!'

    >>> Cifrado_Atbash("Bienvenido al código Atbash de nuestro proyecto!")
    'yRVMEVMRWL ZO XMWRTL zGYZHS WV MFVHGIL KILBVXGL!'

    >>> Cifrado_Atbash("¿Qué prueba te gustaría realizar primero?")
    '¿jFV KIFVYZ GV TFHGZIRZ IVZORAZI KIRNVIL?'

    >>> Cifrado_Atbash("hoy es un lindo día para programar")
    'SLB VH FM ORMWL WRZ KZIZ KILTIZNZI'

    >>> Cifrado_Atbash("hay muchos ñandues que cazar")
    'SZB NFXSLH niZMWFVH JFV XZAZI'

    >>> Cifrado_Atbash("@@@!!??**42")
    '@@@!!??**57'

    >>> Cifrado_Atbash("Algoritmos y Programación 1")
    'zOTLIRGNLH B kILTIZNZXRMM 8'

    >>> Cifrado_Atbash("El mejor GRUPO DEL MUNDO@!")
    'vO NVQLI tifkl wvo nfmwl@!'

    >>> Cifrado_Atbash("En las montañas , los niños juegan")
    'vM OZH NLMGZniZH , OLH MRniLH QFVTZM'
    """
    especiales = caracteres_especiales()
    
    resultado = ""
    
    for  caracter in mensaje:
        if caracter in especiales:
            resultado += especiales[caracter]
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
    print(Cifrado_Atbash("Hola mundo"))