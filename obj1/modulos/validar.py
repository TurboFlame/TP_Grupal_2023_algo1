def validar_usuario(usuario):
    """
    Valida un usuario según los siguientes criterios:

    - Longitud entre 5 y 15 caracteres.
    - Puede contener letras, números y los siguientes caracteres especiales: "_", "-", ".", ",".
    - No puede haber caracteres no permitidos.
    - No puede haber caracteres repetidos adyacentes.

    >>> validar_usuario("usuario123")
    True

    >>> validar_usuario("user-name")
    True

    >>> validar_usuario("user.name")
    True

    >>> validar_usuario("user,123")
    True

    >>> validar_usuario("user!123")
    False

    >>> validar_usuario("user---name")
    False

    >>> validar_usuario("user1234567890123")
    False

    >>> validar_usuario("user_123")
    False

    >>> validar_usuario("user_name")
    False

    >>> validar_usuario("user..name")
    False

    >>> validar_usuario("user-123")
    True
    """
    caracteres_validos = "_-.,"
    longitud_usuario = 5 <= len(usuario) <= 15

    caracteres = {}
    i = 0
    while longitud_usuario and i < len(usuario):
        caracter = usuario[i]
        if not (caracter.isalnum() or caracter in caracteres_validos):
            longitud_usuario = False
        if caracter not in caracteres:
            caracteres[caracter] = 1
        else:
            if i > 0 and caracter == usuario[i - 1]:
                longitud_usuario = False  # Caracteres repetidos adyacentes
            caracteres[caracter] += 1
        i += 1

    resultado = longitud_usuario
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
def validar_clave(clave):
    """
    Valida una clave según los siguientes criterios:
    
    - Longitud entre 4 y 8 caracteres.
    - Al menos una letra mayúscula.
    - Al menos una letra minúscula.
    - Al menos un número.
    - Al menos un caracter de los siguientes: "_", "-", "#", "*".
    - No puede haber caracteres repetidos adyacentes.

    >>> validar_clave("Abc_123")
    True

    >>> validar_clave("abc123")
    False

    >>> validar_clave(""Alprob-8"")
    False

    >>> validar_clave("aB1*")
    True

    >>> validar_clave("12345")
    False

    >>> validar_clave("aB1*_")
    False

    >>> validar_clave("Aa1*_")
    True

    >>> validar_clave("Algor_&1")
    False

    >>> validar_clave("aA1*")
    False

    >>> validar_clave("Aa1*#")
    True

    >>> validar_clave("Aa1*#A")
    False
    """
    caracteres_validos = "_-#*"

    validar = 4 <= len(clave) <= 8
    minus = False
    mayus = False
    numeros = False
    caracteres = {}
    contador = 0
    while validar and contador < len(clave):
        char = clave[contador]
        if char == " ":
            validar = False
        elif char.isalnum() or char in caracteres_validos:
            
            if char.isupper():
                    mayus = True
            elif char.islower():
                    minus = True
            elif char.isnumeric():
                numeros = True

            if char not in caracteres:
                caracteres[char] = 1
            else:
                if contador > 0 and char == clave[contador - 1]:
                    validar = False  
                caracteres[char] += 1

        contador += 1

    resultado = validar and minus and numeros and mayus
    return resultado
print(validar_clave("Aa1*#A"))

if __name__ == "__main__":
    import doctest
    doctest.testmod()