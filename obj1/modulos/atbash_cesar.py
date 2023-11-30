# Función para cifrar un mensaje usando el cifrado César
def cifrar_cesar(contraseña, clave):
    """
    >>> cesar_encoder("holaááá", 5)
    'mtqfááá'
    >>> cesar_encoder("aña", 42)
    'qdyq'
    >>> cesar_encoder("5644", 3)
    '8977'
    >>> cesar_encoder("que onda", -3)
    'nrb lkax'
    >>> cesar_encoder("3", -4)
    '9'
    >>> cesar_encoder("AÑA", -4)
    'WJEW'
    >>> cesar_encoder("hola buenos diás", 50000)
    'jqnc dwgpqu fkáu'
    >>> cesar_encoder("HOLA QUE TAL", -50000)
    'FMJY OSC RYJ'
    >>> cesar_encoder("al_GORIT-m0s_1", 5)
    'fq_LTWNY-r5x_6'
    >>> cesar_encoder("chau", -5)
    'xcvp'
    """
    contraseña = reemplazar_ñ(contraseña)

    contraseña_codificada = ""
    letras_invalidas = "áéíóúÁÉÍÓÚ"
    ABECEDARIO=26
    for letra in contraseña:
        if letra.islower() and letra not in letras_invalidas:
            unicode = ord(letra)
            contraseña_codificada += chr(97 + (unicode + clave - 97) % ABECEDARIO).lower()
        elif letra.isupper() and letra not in letras_invalidas:
            unicode = ord(letra)
            contraseña_codificada += chr(65 + (unicode + clave - 65) % ABECEDARIO).upper()
        elif letra.isdigit():
            unicode_int = int(ord(letra))
            contraseña_codificada += chr((unicode_int + clave - 48) % 10 + 48)
        else:
            contraseña_codificada += letra

    return contraseña_codificada

def reemplazar_ñ(palabra):
    nuevo_string = ""
    for letra in palabra:
        if letra == "ñ":
            nuevo_string += "ni"
        elif letra == "Ñ":
            nuevo_string += "NI"
        else:
            nuevo_string += letra

    return nuevo_string
# Función para cifrar un mensaje usando el cifrado Atbash
def caracteres_especiales():
    return {
        "á": "Z", "é": "V", "í": "R", "ó": "M", "ú": "N",
        "Á": "z", "É": "v", "Í": "r", "Ó": "m", "Ú": "n",
        "ñ": "ni", "Ñ": "NI",
        "0": "9", "1": "8", "2": "7", "3": "6", "4": "5",
        "5": "4", "6": "3", "7": "2", "8": "1", "9": "0"
    }

def cifrar_atbash(mensaje):
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