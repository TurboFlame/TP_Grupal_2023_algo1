from tkinter import *

import csv


def verificar_datos(usuario):
    resultado = False
    pregunta = ""
    contraseña_correcta = ""
    lista_retornable=[None,None,None,None,None]
    with open('obj1/modulos/registro.csv', 'r') as archivo:
        lineas = csv.reader(archivo)
        for linea in lineas:    
            if linea[0] == usuario:
                resultado = True
                lista_retornable=linea
        
        lista_retornable.append(resultado)
        print(lista_retornable)
    return lista_retornable




def verificar(entry_usuario_inicio, entry_contraseña_inicio, resultado_label_inicio, boton_recuperar_inicio, boton_registrarse_inicio):
    usuario = entry_usuario_inicio.get()
    contraseña = entry_contraseña_inicio.get()
    datos=[None,None,None,None,None]
    datos = verificar_datos(usuario)
    usuario_datos=datos[0]
    contraseña_datos=datos[1]
    pregunta_datos=datos[2]
    respuesta_datos=datos[3]
    resultado=datos[4]
    
    if usuario==usuario_datos and contraseña != contraseña_datos:
        resultado_label_inicio.config(text="Datos Incorrectos", fg="red")
        boton_recuperar_inicio.grid()
        boton_registrarse_inicio.grid_remove()
        resultado=False
        
        
    elif usuario_datos != usuario:
        resultado_label_inicio.config(text="Usuario No Registrado", fg="red")
        resultado_label_inicio.grid()
        resultado=False
        boton_registrarse_inicio.grid()
        boton_recuperar_inicio.grid_remove()
    return(resultado,usuario) 

