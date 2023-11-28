from tkinter import *


from validar import validar_usuario #funcion validar usuario
from validar import validar_clave #funcion validar clave
import csv

def guardar_registro(entrada_usuario, entrada_contraseña, pregunta, entrada_respuesta, label_registro):
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    pregunta_seleccionada = pregunta.get()
    respuesta = entrada_respuesta.get()

 

    if validar_usuario(usuario) and validar_clave(contraseña):
        with open('obj1/modulos/registro.csv', 'a', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow([usuario, contraseña, pregunta_seleccionada, respuesta])

        label_registro.config(text="Registro correcto", fg='green')
    else:
        label_registro.config(text="Registro fallido", fg='red')

def crear_ventana_registro():
    raiz5 = Tk()
    raiz5.title('Registro de Usuario')
    raiz5.geometry('1000x500')
    raiz5.config(bg='LightSkyBlue2', relief='ridge', bd=35, width=300, height=150)

    frame_principal = Frame(raiz5, bg='Snow2', bd=5, relief='sunken', width=400, height=300)
    frame_principal.pack(expand=True)

    frame_interno = Frame(frame_principal, bg='Snow2')
    frame_interno.grid(row=0, column=0, padx=10, pady=10)

    label_usuario = Label(frame_interno, text='Usuario:', font=('Arial', 16), bg='Snow2')
    label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    entrada_usuario = Entry(frame_interno, font=('Arial', 14))
    entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

    label_contraseña = Label(frame_interno, text='Contraseña:', font=('Arial', 16), bg='Snow2')
    label_contraseña.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    entrada_contraseña = Entry(frame_interno, show='*', font=('Arial', 14))
    entrada_contraseña.grid(row=1, column=1, padx=10, pady=10)

    label_pregunta = Label(frame_interno, text='Pregunta:', font=('Arial', 16), bg='Snow2')
    label_pregunta.grid(row=2, column=0, padx=10, pady=10, sticky='e')

    opciones_pregunta = ['Seleccionar una pregunta', 'Nombre de tu mejor amigo/amiga', 'Nombre de tu mascota', 'Cantante preferido', 'Ciudad preferida',
                         'Apellido De Abuela Materna','Color Favorito','Deporte Favorito','Genero de Musica Favorito','Deporte Preferido','Cancion Favorita','Nombre de Tu Madre']
    pregunta = StringVar()
    pregunta.set(opciones_pregunta[0])

    pregunta_desplegable = OptionMenu(frame_interno, pregunta, *opciones_pregunta)
    pregunta_desplegable.config(font=('Arial', 14))
    pregunta_desplegable.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    label_respuesta = Label(frame_interno, text='Respuesta:', font=('Arial', 16), bg='Snow2')
    label_respuesta.grid(row=3, column=0, padx=10, pady=10, sticky='e')

    entrada_respuesta = Entry(frame_interno, font=('Arial', 14))
    entrada_respuesta.grid(row=3, column=1, padx=10, pady=10)
    
    
    label_registro = Label(frame_interno, text='', font=('Arial', 16), bg='Snow2', fg='red')
    label_registro.grid(row=7, column=0, columnspan=5, pady=10)   

    boton_registrar = Button(frame_interno, text="Registrarse", command=lambda: guardar_registro(entrada_usuario, entrada_contraseña, pregunta, entrada_respuesta,label_registro), font=('Arial', 14))
    boton_registrar.grid(row=5, column=0, columnspan=10, pady=10)

    raiz5.mainloop()
    
if __name__ == "__main__":
    crear_ventana_registro()
