from tkinter import *
raiz2=Tk()
raiz2.title('TP Grupal Parte 1 - Grupo: Losange')
raiz2.iconbitmap('losange.ico')
raiz2.geometry('1500x1080')
raiz2.config(bg='blue', relief='groove',bd=45 )
raiz2.resizable(1,1)

miFrame2=Frame()
miFrame2.pack()
miFrame2.config(width='1400', height='1000', bg='sky blue',relief='sunken', bd=35)

def codigo_boton():
    
    raiz=Tk()
    raiz.title('TP Grupal Parte 1 - Grupo: Losange')
    raiz.iconbitmap('losange.ico')
    raiz.geometry('1080x720')
    raiz.config(bg='blue', relief='groove',bd=45 )
    raiz.resizable(1,1)

    miFrame=Frame()
    miFrame.pack(side='left')
    miFrame.config(bg='sky blue',relief='sunken', bd=35)

    metodo1=Button(miFrame, text='Cifrado César')
    metodo1.grid(row=0, column=0, padx=10, pady=15)

    metodo2=Button(miFrame, text='Cifrado Atbash')
    metodo2.grid(row=2, column=0, padx=10, pady=5)

    cuadro_metodo1=Text(miFrame, width=150 , height=9)
    cuadro_metodo1.grid(row=0, column=1, padx=10, pady=5)

    cuadro_metodo2=Text(miFrame, width=150 , height=9)
    cuadro_metodo2.grid(row=2, column=1, padx=10, pady=5)

    scroll=Scrollbar(miFrame, command=cuadro_metodo1.yview,)
    scroll.grid(row=0 , column=2, sticky='nsew')
    scroll2=Scrollbar(miFrame, command=cuadro_metodo2.yview,)
    scroll2.grid(row=2 , column=2, sticky='nsew')

    cuadro_metodo1.config(yscrollcommand=scroll.set)
    cuadro_metodo2.config(yscrollcommand=scroll2.set)

    def borrar_1():
        cuadro_metodo1.delete("1.0", "end")
        cuadro_resultado1.delete("1.0", "end")
    
    def borrar_2():
        cuadro_metodo2.delete("1.0", "end")
        cuadro_resultado2.delete("1.0", "end")

    limpieza_1=Button(miFrame, text='LIMPIAR', command=borrar_1)
    limpieza_1.grid(row=1, column=0, padx=10, pady=5)

    limpieza_2=Button(miFrame, text='LIMPIAR', command=borrar_2)
    limpieza_2.grid(row=3, column=0, padx=10, pady=5)

    cuadro_resultado1=Text(miFrame, width=150 , height=9)
    cuadro_resultado1.grid(row=1, column=1, padx=10, pady=5)

    cuadro_resultado2=Text(miFrame, width=150 , height=9)
    cuadro_resultado2.grid(row=3, column=1, padx=10, pady=5)

    scroll3=Scrollbar(miFrame, command=cuadro_resultado1.yview,)
    scroll3.grid(row=1, column=2, sticky='nsew')
    scroll4=Scrollbar(miFrame, command=cuadro_resultado2.yview,)
    scroll4.grid(row=3 , column=2, sticky='nsew')

    cuadro_resultado1.config(yscrollcommand=scroll3.set)
    cuadro_resultado2.config(yscrollcommand=scroll4.set)

    raiz.mainloop()

comentario_inicial=Label(miFrame2, text='Bienvenido a la aplicacion de mensajes secretos del grupo Losange. Para continuar presione continuar, de lo contrario cierre la ventana',relief='sunken',bg='sky blue', fg='purple', font=('comic sans ms',16)).place(x=25, y=25)
boton_inicial=Button(miFrame2, text='CONTINUAR', fg='red', font='sans',command=codigo_boton).place(x=600, y=80)

miImagen2=PhotoImage(file='chico.png')
foto_grupo=Label(image=miImagen2, width='800', height='450').place(x=310, y=180)

raiz2.mainloop()