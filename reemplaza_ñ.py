'''
Created on 22 oct. 2023

@author: agusn
'''



def reemplazador_ñ(palabra):
    nuevo_string=""
    for letra in palabra:
        if letra=="ñ":
            nuevo_string+="ni"
        elif letra=="Ñ":
            nuevo_string+="NI"
        else:
            nuevo_string+=letra    
                
    return nuevo_string
#Agustin Reyes
#El proposito de esta funcion es recibir un string y devolverlo luego de 
#intercambiar los caracteres "ñ" o "Ñ" por "ni" o "NI" respectivamente.



