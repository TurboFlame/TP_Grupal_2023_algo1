from tkinter import *
from validar import validar_usuario, validar_clave
import csv

'''
Autor: BRIAN, REYES
'''
def usuario_existente(nombre_usuario): #funcion para verificar si el usuario ya está registrado
    usuarios_existentes = {}
    
    try:
        with open('obj1/modulos/registro.csv', 'r') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                usuarios_existentes[fila[0]] = True
                   

    except FileNotFoundError:
        pass  # maneja el caso en el que el archivo no existe

    return nombre_usuario in usuarios_existentes

def guardar_registro(entrada_usuario, entrada_contraseña, pregunta, entrada_respuesta, label_registro):
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    pregunta_seleccionada = pregunta.get()
    respuesta = entrada_respuesta.get()

    if not validar_usuario(usuario):
        label_registro.config(text="Nombre de usuario inválido", fg='red')
    elif usuario_existente(usuario):
        label_registro.config(text="El usuario ya está en uso", fg='red')
    elif not validar_clave(contraseña):
        label_registro.config(text="Contraseña inválida", fg='red')
    else:
        with open('obj1/modulos/registro.csv', 'a', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow([usuario, contraseña, pregunta_seleccionada, respuesta,0])

        label_registro.config(text="Registro correcto", fg='green')
        
#funion para guardar las preguntas para recuperar contraseña en un archivo csv
def guardar_preguntas_en_csv(preguntas, archivo='preguntas.csv'):
    with open('preguntas.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Pregunta'])
        for pregunta in preguntas:
            writer.writerow([pregunta])

def crear_ventana_registro(raiz=None):
    
    
    if not raiz==None:
        raiz.withdraw()
    
    raiz_usuario = Tk()
    raiz_usuario.title('Registro de Usuario')
    raiz_usuario.geometry('1000x500')
    raiz_usuario.config(bg='LightSkyBlue2', relief='ridge', bd=35, width=300, height=150)

    frame_principal = Frame(raiz_usuario, bg='Snow2', bd=5, relief='sunken', width=400, height=300)
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

    # Guardar las preguntas en el archivo preguntas.csv
    guardar_preguntas_en_csv(opciones_pregunta)

    pregunta_desplegable = OptionMenu(frame_interno, pregunta, *opciones_pregunta)
    pregunta_desplegable.config(font=('Arial', 14))
    pregunta_desplegable.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    label_respuesta = Label(frame_interno, text='Respuesta:', font=('Arial', 16), bg='Snow2')
    label_respuesta.grid(row=3, column=0, padx=10, pady=10, sticky='e')

    entrada_respuesta = Entry(frame_interno, font=('Arial', 14))
    entrada_respuesta.grid(row=3, column=1, padx=10, pady=10)

    label_registro = Label(frame_interno, text='', font=('Arial', 16), bg='Snow2', fg='red')
    label_registro.grid(row=7, column=0, columnspan=5, pady=10)

    boton_registrar = Button(frame_interno, text="Registrarse", command=lambda: guardar_registro(entrada_usuario, entrada_contraseña, pregunta, entrada_respuesta, label_registro), font=('Arial', 14))
    boton_registrar.grid(row=5, column=0, columnspan=10, pady=10)
    
    boton_atras = Button(frame_interno, text="Retroceder", command=lambda: retroceder(raiz, raiz_usuario), font=('Arial', 14), fg='blue')
    boton_atras.grid(row=5, column=0, columnspan=10, pady=10, sticky='w')
    
    

    raiz_usuario.mainloop()


def retroceder(raiz_abrir,raiz_cerrar):
    raiz_cerrar.withdraw()
    raiz_abrir.deiconify()
    
    
    





if __name__ == "__main__":
    crear_ventana_registro()
