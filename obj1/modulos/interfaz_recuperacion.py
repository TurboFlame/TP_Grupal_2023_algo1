from tkinter import *
from interfaz_iniciar_sesion import*
import csv

'''
Autor: LEONEL
'''
def obtener_todo(usuario):
    pregunta_importante = ""
    with open('obj1/modulos/registro.csv', 'r') as archivo:
        lineas = csv.reader(archivo)
        for linea in lineas:
            if linea[0] == usuario:
                lista_de_todo=[]
                lista_de_todo=linea
    return lista_de_todo

'''
Autor: LEONEL
'''
def actualizar_intentos(usuario, nuevos_intentos):
    registros = []
    with open('obj1/modulos/registro.csv', 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            if datos[0] == usuario:
                datos[4] = str(nuevos_intentos)
            registros.append(','.join(datos))
    
    with open('obj1/modulos/registro.csv', 'w') as archivo:
        archivo.write('\n'.join(registros))

'''
Autor: LEONEL
'''
def verificar_y_mostrar(entry_respuesta, resultado_label, usuario, intentos_label):
    respuesta_usuario = entry_respuesta.get()
    de_todo= obtener_todo(usuario)
    respuesta_correcta = de_todo[3]
    print(de_todo)
    print(de_todo[3])
    intentos = int(de_todo[4])
    contraseña_correcta=de_todo[1]
    pregunta=de_todo[1]

    if intentos >= 3:
        mensaje = "Usuario bloqueado. Demasiados intentos fallidos."
        resultado_label.config(text=mensaje, fg='red')  
    elif respuesta_usuario == respuesta_correcta:
        mensaje = "Respuesta correcta. Contraseña: " + contraseña_correcta
        intentos_label.config(text="")
    else:
        mensaje = "Respuesta incorrecta"
        intentos += 1
        actualizar_intentos(usuario, intentos)

    intentos_label.config(text="Intentos fallidos: " + str(intentos))
    resultado_label.config(text=mensaje)

'''
Autor: GUILLOTE
'''
def crear_interfaz_recuperacion(usuario):
    raiz_inicio = Tk()
    raiz_inicio.title('Iniciar Sesión')
    raiz_inicio.geometry('1000x500')
    raiz_inicio.config(bg='LightSkyBlue2', relief='ridge', bd=35)

    frame_inicio = Frame(raiz_inicio, bg='Snow1', bd=5, relief='sunken')
    frame_inicio.pack(expand=True)

    frame_interno = Frame(frame_inicio, bg='Snow2')
    frame_interno.grid(row=0, column=0, padx=10, pady=10)

    label_pregunta = Label(frame_interno, text=verificar_datos(usuario)[2] + ':', font=('Arial', 16), bg='Snow2')
    label_pregunta.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    entry_respuesta = Entry(frame_interno, font=('Arial', 14))
    entry_respuesta.grid(row=0, column=1, padx=10, pady=10)

    resultado_label = Label(frame_interno, text="", font=('Arial', 14), bg='Snow2')
    resultado_label.grid(row=2, columnspan=2, pady=10)

    intentos_label = Label(frame_interno, text="Intentos fallidos: 0", font=('Arial', 14), bg='Snow2')
    intentos_label.grid(row=3, columnspan=2, pady=10)

    boton_verificar = Button(frame_interno, text="Verificar", command=lambda: verificar_y_mostrar(entry_respuesta, resultado_label, usuario, intentos_label), font=('Arial', 14), fg='black', padx=10, pady=5)
    boton_verificar.grid(row=1, columnspan=2, pady=10)

    raiz_inicio.mainloop()