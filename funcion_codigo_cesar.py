'''
Created on 12 oct. 2023

@author: agusn
'''





def cesar_encoder(contraseña,clave):
    
    contraseña_codificada=""
    
    
    
    
    #Esta funcion recibe un string y una clave. Por cada caracter determina si es mayuscula, minuscula o digito.
    #Luego, recorre su unicode para devolver un caracter movido la cantidad de espacios especificada por
    #la clave para colocarlo en un nuevo string. Luego, retorna el nuevo string.
    for letra in contraseña:
        #Se necesita crear un caso especial para la "ñ"
        if letra.islower():
            
            unicode=ord(letra)

            
            while unicode+clave>122:
                unicode-=26
            
            contraseña_codificada+=chr(unicode+clave).lower()
            
            
            #Se necesita crear un caso especial para la "Ñ"
        elif letra.isupper():
            unicode=ord(letra)

            
            while unicode+clave>90:
                unicode-=26
            
            contraseña_codificada+=chr(unicode+clave).upper()
            
            
        elif letra.isdigit():
            
            unicode_int=int(ord(letra))

            
            while unicode_int+clave>57:
                unicode-=9
            
            contraseña_codificada+=chr(unicode_int+clave).upper()
            

    
    return contraseña_codificada



