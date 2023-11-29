from tkinter import*
import csv

from interfaz_iniciar_sesion import verificar_datos

def recuperacion_contraseña(usuario="Placeholder"):
    raiz_recuperacion_contraseña=Tk()
    raiz_recuperacion_contraseña.title('RECUPERACION DE CLAVE')
    raiz_recuperacion_contraseña.geometry('1000x500')
    raiz_recuperacion_contraseña.resizable(0,0)
    raiz_recuperacion_contraseña.config(bg='blue', relief='groove', bd=25)

    frame_recuperacion_contraseña=Frame()
    frame_recuperacion_contraseña.pack()
    frame_recuperacion_contraseña.config(width='1000', height='500', bg='sky blue', relief='sunken', bd=35)



    intentos=3
    #INTRODUCIR AL TEXT LA FUNCION QUE RETORNE LA PREGUNTA AL USUARIO ASIGNADO CSV
    comentario_recuperacion_contraseña=Label(frame_recuperacion_contraseña, text=None).place(x=100 ,y=50 )
    comentario_recuperacion_contraseña=Label(frame_recuperacion_contraseña, text='Introduzca la respuesta:', font=('Arial', 12)).place(x=100 ,y=150 )
    
    
    
    
    comentario_intentos=Label(frame_recuperacion_contraseña, text="Tiene " + str(intentos) +" intentos restantes").place(x=300,y=150)
    
    
    
    
    respuesta_de_usuario_recuperacion_contraseña= Entry(frame_recuperacion_contraseña, width=80)
    respuesta_de_usuario_recuperacion_contraseña.place(x=100,y=200)
    
    
    
    
    
    print(verificar_datos(usuario)[2])
    texto_pregunta=Label(frame_recuperacion_contraseña,text=verificar_datos(usuario)[2])
    texto_pregunta.place(x=150,y=240)
    
    boton_recuperar= Button(frame_recuperacion_contraseña,text="Recuperar contraseña",command=lambda:contraseña_correcta(verificar_datos(usuario)[1]) if checkear_respuesta(usuario,respuesta_de_usuario_recuperacion_contraseña.get())else intentos-1
    
    
    boton_recuperar.place(x=150,y=200)
    
    
    raiz_recuperacion_contraseña.mainloop()
    
    
    
    
    
    
    
    
    
def checkear_respuesta(usuario,entrada_respuesta):
    
    datos=verificar_datos(usuario)
    
    contraseña=datos[1]
    respuesta=datos[3]  
    contraseña_valida=False
    
    if respuesta==entrada_respuesta:
        
        contraseña_valida=True
    
        
    return contraseña_valida    
        
          
        
    
    
def contraseña_correcta(contraseña):
    print()    
    
def contraseña_incorrecta(intentos):
    print()    
    
    
    
    
    
    
    
    
    

    
    
        












recuperacion_contraseña()