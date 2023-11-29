from tkinter import*

def recuperacion_contraseña():
    raiz_recuperacion_contraseña=Tk()
    raiz_recuperacion_contraseña.title('RECUPERACION DE CLAVE')
    raiz_recuperacion_contraseña.geometry('1000x500')
    raiz_recuperacion_contraseña.resizable(0,0)
    raiz_recuperacion_contraseña.config(bg='blue', relief='groove', bd=25)

    frame_recuperacion_contraseña=Frame()
    frame_recuperacion_contraseña.pack()
    frame_recuperacion_contraseña.config(width='1400', height='1000', bg='sky blue', relief='sunken', bd=35)

    #INTRODUCIR AL TEXT LA FUNCION QUE RETORNE LA PREGUNTA AL USUARIO ASIGNADO CSV
    comentario_recuperacion_contraseña=Label(frame_recuperacion_contraseña, text=None).place(x=100 ,y=50 )
    comentario_recuperacion_contraseña=Label(frame_recuperacion_contraseña, text='Introduzca la respuesta:', font=('Arial', 12)).place(x=100 ,y=150 )
    respuesta_de_usuario_recuperacion_contraseña= Entry(frame_recuperacion_contraseña, width=80).place(x=100 ,y=200 )


    def boton_recuperacion_contraseña(respuesta):
        # INTRODUCIR FUNCION QUE RECORRA EL ARCHIVO CSV
        respuesta = False
        with open('obj1/modulos/registro.csv', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea_nueva = linea.strip()
                datos = linea_nueva.split(',')
                if datos[3] == respuesta:
                    resultado = True
                    #ABRIR INTEFAZ DE CODIGO CESAR Y ATBASH CON ENVIO DE CODIGOS
                else:
                    ventana_emergente()
        return resultado

    
    def ventana_emergente():
        raiz_recuperacion_contraseña.withdraw()
        raiz_ventana_emergente = Tk()
        raiz_ventana_emergente.title('TP Grupal Parte 1 - Grupo: Losange')
        raiz_ventana_emergente.iconbitmap('losange.ico')
        raiz_ventana_emergente.geometry('1000x500')
        raiz_ventana_emergente.config(bg='blue', relief='groove', bd=45)
        raiz_ventana_emergente.resizable(0, 0)

        frame_ventana_emergente = Frame(raiz_ventana_emergente)
        frame_ventana_emergente.pack()
        frame_ventana_emergente.config(bg='sky blue', relief='sunken', bd=35)

        mensaje_label = Label(frame_ventana_emergente, text='Tiene en total 3 intentos', font=('Arial', 12).place(x=100 ,y=400 ))

        def cierre_ventana_emergente():
            ventana_emergente.withdraw()

        boton_ventana_emergente=Button(frame_ventana_emergente, text='CONTINUAR', font='sans', command=cierre_ventana_emergente).place(x=300 ,y=400 )
        
    boton_recuperacion_contraseña=Button(frame_recuperacion_contraseña, text='CONTINUAR', font='sans', command=boton_recuperacion_contraseña).place(x=400 ,y=300 )


    raiz_recuperacion_contraseña.mainloop()

recuperacion_contraseña()