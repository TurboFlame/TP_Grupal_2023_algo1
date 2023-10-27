"""
Las siguientes pruebas aplican atbash al valor ingresado
created on 24/10/2023 
@author: Carlos
>>> atbash("Hola Mundo 12345")
"sLOZ nFMWL 87654"

>>> atbash("Somos el grupo Losanges!!")
"hLNLH VO TIFKL oLHZMTVH¡¡"

>>> atbash("Bienvenido al codigo atbash de nuestro proyecto!")
"yRVMEVMRWL ZO XLWRTL ZGYZHS WV MFVHGIL KILBVXGL¡"

>>> atbash("Qué prueba te gustaría realizar primero?")
"jFé KIFVYZ GV TFHGZIíZ IVZORAZI KIRNVIL¿"

>>> atbash("hoy es un lindo día para programar")
"SLB VH FM ORMWL WíZ KZIZ KILTIZNZI"
"""

def atbash(mensaje):
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?"
    alfabeto_inverso = "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba9876543210¡¿"
    cifrado = ""

    for char in mensaje:
            if char in alfabeto:
                indice = alfabeto.index(char)
                cifrado += alfabeto_inverso[indice]
            else:
                cifrado += char

    return cifrado

if __name__ == "__main__":
    import doctest
    doctest.testmod()

