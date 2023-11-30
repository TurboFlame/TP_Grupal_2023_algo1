from tkinter import *
import csv

def verificar_datos(usuario, contraseña):
    resultado = False
    with open('registro4.csv', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea_nueva = linea.strip()
            datos = linea_nueva.split(',')
            if datos[0] == usuario and datos[1] == contraseña:
                resultado = True
    return resultado

def verificar(entry_usuario_inicio, entry_contraseña_inicio, resultado_label_inicio, boton_recuperar_inicio):
    usuario = entry_usuario_inicio.get()
    contraseña = entry_contraseña_inicio.get()

    if verificar_datos(usuario, contraseña):
        resultado_label_inicio.config(text="Datos correctos", fg="green")
    else:
        resultado_label_inicio.config(text="Datos incorrectos", fg="red")
        resultado_label_inicio.grid()
        boton_recuperar_inicio.grid()

def crear_ventana_inicio():
    raiz_inicio = Tk()
    raiz_inicio.title('Iniciar Sesion')
    raiz_inicio.geometry('1000x500')
    raiz_inicio.config(bg='LightSkyBlue2', relief='ridge', bd=35, width=300, height=150)

    frame_inicio = Frame(raiz_inicio, bg='Snow1', bd=5, relief='sunken', width=400, height=300)
    frame_inicio.pack(expand=True)

    frame_interno = Frame(frame_inicio, bg='Snow2')
    frame_interno.grid(row=0, column=0, padx=10, pady=10)

    label_usuario_inicio = Label(frame_interno, text='Usuario:', font=('Arial', 16), bg='Snow2')
    label_usuario_inicio.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    entry_usuario_inicio = Entry(frame_interno, font=('Arial', 14))
    entry_usuario_inicio.grid(row=0, column=1, padx=10, pady=10)

    label_contraseña_inicio = Label(frame_interno, text='Contraseña:', font=('Arial', 16), bg='Snow2')
    label_contraseña_inicio.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    entry_contraseña_inicio = Entry(frame_interno, show='*', font=('Arial', 14))
    entry_contraseña_inicio.grid(row=1, column=1, padx=10, pady=10)

    boton_recuperar_inicio = Button(frame_interno, text="Recuperar Contraseña/Usuario", font=('Arial', 14))
    boton_recuperar_inicio.grid(row=4, column=0, columnspan=2, pady=10)
    boton_recuperar_inicio.grid_remove()

    boton_verificar_inicio = Button(frame_interno, text="Ingresar", command=lambda: verificar(entry_usuario_inicio, entry_contraseña_inicio, resultado_label_inicio, boton_recuperar_inicio), font=('Arial', 14))
    boton_verificar_inicio.grid(row=3, column=0, columnspan=2, pady=10)

    resultado_label_inicio = Label(frame_interno, text='', font=('Arial', 16), bg='Snow2', fg='red')
    resultado_label_inicio.grid(row=7, column=0, columnspan=5, pady=10)

    raiz_inicio.mainloop()

crear_ventana_inicio()