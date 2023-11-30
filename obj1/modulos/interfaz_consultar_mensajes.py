'''
Created on 28 nov. 2023

@author: Carlos, Brian
'''

from tkinter import *
import csv
from atbash_cesar import cifrar_atbash, cifrar_cesar

def leer_mensajes_desde_archivo():
    mensajes = []
    try:
        with open("mensajes.csv", "r") as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                mensajes.append(fila)
    except FileNotFoundError:
        mostrar_error("El archivo mensajes.csv no existe.")

    return mensajes

def mostrar_mensajes_descifrados(mensajes):
    raiz_recibidos = Tk()
    raiz_recibidos.title("Mensajes recibidos")
    raiz_recibidos.config(bg="blue", relief="groove", bd=40)
    raiz_recibidos.geometry("800x600+200+100")

    etiqueta_mensajes = Label(raiz_recibidos, text="Mensajes Recibidos", font=('Arial', 16), bg='blue', fg='white')
    etiqueta_mensajes.pack(pady=10)

    frame_mensajes = Text(raiz_recibidos, width=70, height=20)
    frame_mensajes.pack(padx=10, pady=10, expand=True, fill="both")

    if not mensajes:
        mostrar_error("No hay mensajes disponibles.")
    else:
        for mensaje in mensajes:
            destino = mensaje["destinatario"]
            contenido = descifrar_mensaje(mensaje)
            remitente = mensaje["usuario"]

            if destino == "todos":
                frame_mensajes.insert(END, f"#{remitente}: {contenido}\n")
            else:
                frame_mensajes.insert(END, f"{remitente}: {contenido}\n")

        frame_mensajes.insert(END, f"Total de Mensajes: {len(mensajes)}")

        scrollbar = Scrollbar(frame_mensajes, command=frame_mensajes.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        frame_mensajes.config(yscrollcommand=scrollbar.set)
    
    boton_ver_mensajes = Button(raiz_recibidos, text="Ver mensajes recibidos", command=raiz_recibidos.destroy)
    boton_ver_mensajes.pack()

    raiz_recibidos.mainloop()

def descifrar_mensaje(mensaje):
    codificador = mensaje["codificador"]
    mensaje_cifrado = mensaje["mensaje"]
    if codificador == "C":
        clave = int(mensaje["clave"])
        mensaje_descifrado = cifrar_cesar(mensaje_cifrado, -clave)
    else:
        mensaje_descifrado = cifrar_atbash(mensaje_cifrado)
    return mensaje_descifrado

def consultar_mensajes():
    mensajes = leer_mensajes_desde_archivo()
    mostrar_mensajes_descifrados(mensajes)

def mostrar_error(mensaje):
    ventana_error = Tk()
    ventana_error.title("Error")
    ventana_error.config(bg="red", relief="groove", bd=40)
    ventana_error.geometry("400x150+300+200")

    etiqueta_error = Label(ventana_error, text=mensaje, font=('Arial', 16), bg='red', fg='white')
    etiqueta_error.pack(pady=20)

    boton_aceptar = Button(ventana_error, text="Aceptar", command=ventana_error.destroy)
    boton_aceptar.pack()

    ventana_error.mainloop()

# Llamar a la función consultar_mensajes() desde tu programa principal