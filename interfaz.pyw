from tkinter import *

# Función para cifrar un mensaje usando el cifrado César
def cesar_encoder(contraseña, clave):
    contraseña_codificada = ""
    
    for letra in contraseña:
        if letra.islower():
            unicode = ord(letra)
            while unicode + clave > 122:
                unicode -= 26
            while unicode + clave < 97:
                unicode += 26
            contraseña_codificada += chr(unicode + clave).lower()
        elif letra.isupper():
            unicode = ord(letra)
            while unicode + clave > 90:
                unicode -= 26
            while unicode + clave < 65:
                unicode += 26
            contraseña_codificada += chr(unicode + clave).upper()
        elif letra.isdigit():
            unicode_int = int(ord(letra))
            while unicode_int + clave > 57:
                unicode_int -= 9
            while unicode_int + clave < 48:
                unicode_int += 9
            contraseña_codificada += chr(unicode_int + clave)
    return contraseña_codificada

# Función para cifrar un mensaje usando el cifrado Atbash
def Cifrado_Atbash(mensaje):
    resultado = ""
    acentos = {
        'á': 'z', 'é': 'v', 'í': 'r', 'ó': 'm', 'ú': 'n',
        'Á': 'Z', 'É': 'V', 'Í': 'R', 'Ó': 'M', 'Ú': 'N'
    }
    
    for caracter in mensaje:
        if caracter in acentos:
            resultado += acentos[caracter]
        elif caracter.isalpha():
            if caracter.islower():
                resultado += chr(122 - ord(caracter) + 97)
            elif caracter.isupper():
                resultado += chr(90 - ord(caracter) + 65)
        else:
            resultado += caracter
    return resultado

# Función para mostrar la ventana principal
def mostrar_ventana_principal():
    raiz2.withdraw()
    raiz = Tk()
    raiz.title('TP Grupal Parte 1 - Grupo: Losange')
    raiz.iconbitmap('losange.ico')
    raiz.geometry('1500x800')
    raiz.config(bg='blue', relief='groove', bd=45)
    raiz.resizable(0, 0)

    miFrame = Frame(raiz)
    miFrame.pack()
    miFrame.config(bg='sky blue', relief='sunken', bd=35)

    mensaje_label = Label(miFrame, text='Ingrese un mensaje:', font=('Arial', 12))
    mensaje_label.grid(row=0, column=0, padx=10, pady=10)

    mensaje_entry = Entry(miFrame, width=40)
    mensaje_entry.grid(row=0, column=1, padx=10, pady=10)

    clave_label = Label(miFrame, text='Ingrese la clave (solo para Cifrado César):', font=('Arial', 12))
    clave_label.grid(row=1, column=0, padx=10, pady=10)

    clave_entry = Entry(miFrame)
    clave_entry.grid(row=1, column=1, padx=10, pady=10)

    # Barras de desplazamiento para los cuadros de texto
    
    cuadro_metodo1_scrollbar = Scrollbar(miFrame, orient=VERTICAL)
    cuadro_resultado2_scrollbar = Scrollbar(miFrame, orient=VERTICAL)

    cuadro_metodo1 = Text(miFrame, width=75, height=9, yscrollcommand=cuadro_metodo1_scrollbar.set)
    cuadro_metodo1.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
    cuadro_metodo1_scrollbar.config(command=cuadro_metodo1.yview)
    cuadro_metodo1_scrollbar.grid(row=2, column=2, sticky="ns")

    cuadro_resultado2 = Text(miFrame, width=75, height=9, yscrollcommand=cuadro_resultado2_scrollbar.set)
    cuadro_resultado2.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
    cuadro_resultado2_scrollbar.config(command=cuadro_resultado2.yview)
    cuadro_resultado2_scrollbar.grid(row=3, column=2, sticky="ns")

    def limpiar_cuadros():
        cuadro_metodo1.delete("1.0", "end")
        cuadro_resultado2.delete("1.0", "end")

    limpieza = Button(miFrame, text='Limpiar', command=limpiar_cuadros)
    limpieza.place(x=300, y=450)
    #limpieza.grid(row=4, column=0, padx=10, pady=10)

    def cifrar_mensaje_cesar():
        mensaje = mensaje_entry.get()
        clave = int(clave_entry.get())
        mensaje_cifrado = cesar_encoder(mensaje, clave)
        limpiar_cuadros()
        cuadro_metodo1.insert(END, mensaje_cifrado)

    def descifrar_mensaje_cesar():
        mensaje = cuadro_metodo1.get("1.0", "end-1c")
        clave = int(clave_entry.get())
        mensaje_descifrado = cesar_encoder(mensaje, -clave)
        cuadro_resultado2.insert(END, mensaje_descifrado)

    def cifrar_mensaje_atbash():
        mensaje = mensaje_entry.get()
        mensaje_cifrado = Cifrado_Atbash(mensaje)
        limpiar_cuadros()
        cuadro_metodo1.insert(END, mensaje_cifrado)

    def descifrar_mensaje_atbash():
        mensaje = cuadro_metodo1.get("1.0", "end-1c")
        mensaje_descifrado = Cifrado_Atbash(mensaje)
        cuadro_resultado2.insert(END, mensaje_descifrado)

    cifrar_cesar_button = Button(miFrame, text='Cifrar mensaje César', command=cifrar_mensaje_cesar)
    cifrar_cesar_button.grid(row=5, column=0, padx=10, pady=10)

    cifrar_atbash_button = Button(miFrame, text='Cifrar mensaje Atbash', command=cifrar_mensaje_atbash)
    cifrar_atbash_button.grid(row=5, column=1, padx=10, pady=10)

    descifrar_cesar_button = Button(miFrame, text='Descifrar mensaje César', command=descifrar_mensaje_cesar)
    descifrar_cesar_button.grid(row=6, column=0, padx=10, pady=10)

    descifrar_atbash_button = Button(miFrame, text='Descifrar mensaje Atbash', command=descifrar_mensaje_atbash)
    descifrar_atbash_button.grid(row=6, column=1, padx=10, pady=10)

    raiz.mainloop()
    
raiz2 = Tk()
raiz2.title('TP Grupal Parte 1 - Grupo: Losange')
raiz2.iconbitmap('losange.ico')
raiz2.geometry('1500x800')
raiz2.config(bg='blue', relief='groove', bd=45)
raiz2.resizable(0, 0)

miFrame2 = Frame()
miFrame2.pack()
miFrame2.config(width='1400', height='1000', bg='sky blue', relief='sunken', bd=35)

comentario_inicial = Label(miFrame2, text='Bienvenido a la aplicación de mensajes secretos del grupo Losange. Para continuar presione continuar, de lo contrario, cierre la ventana', relief='sunken', bg='sky blue', fg='purple', font=('comic sans ms', 16))
comentario_inicial.place(x=25, y=25)

boton_inicial = Button(miFrame2, text='CONTINUAR', fg='red', font='sans', command=mostrar_ventana_principal)
boton_inicial.place(x=600, y=80)

miImagen2 = PhotoImage(file='chico.png')
foto_grupo = Label(image=miImagen2, width='800', height='450')
foto_grupo.place(x=310, y=180)

nombres_frame = Frame(miFrame2, bg='sky blue', bd=5)
nombres_frame.place(x=450, y=600)
nombres = [
    "Agustin", "Leonel", "Carlos", "Brian", "Guillermo"
]

for nombre in nombres:
    nombre_label = Label(nombres_frame, text=nombre, font=('comic sans ms', 12), bg='sky blue', fg='black')
    nombre_label.pack(side=LEFT, padx=10)

raiz2.mainloop()
