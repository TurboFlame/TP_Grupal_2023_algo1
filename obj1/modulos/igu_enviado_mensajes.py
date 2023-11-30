'''
Created on 25 nov. 2023

@author: agusn
'''



import csv
from tkinter import *
from interfaz_registro import retroceder




def interfaz_enviado_mensajes(usuario=None, raiz=None):
    
    
    if raiz!=None:
        raiz.withdraw()
        
    
    
    raiz_enviado=Tk()
    raiz_enviado.title("Programa ultra secreto Losange: Enviar mensajes")
    raiz_enviado.config(bg="red",relief="groove",bd=40)
    raiz_enviado.geometry("700x800")


    frame_mensajes=Frame(raiz_enviado)
    frame_mensajes.grid_propagate(False)
    raiz_enviado.resizable(0,0)
    frame_mensajes.config(bg='aquamarine1', relief='ridge', bd=55,width=760,height=760)
    frame_mensajes.pack()


    texto_destinatario=Label(frame_mensajes,text="Ingrese un destinatario",width=19,height=1,bg="pink",anchor="w")
    texto_destinatario.grid(row=0,column=0,pady=20,padx=20)

    texto_mensaje=Label(frame_mensajes,text="Ingrese\nsu\nmensaje",bg="pink",anchor="w",width=7,height=3)
    texto_mensaje.grid(row=1,column=0,pady=30,padx=20)

    texto_clave=Label(frame_mensajes,text="Ingrese una\nclave (solo\npara cifrado\ncesar",bg="pink")
    texto_clave.grid(row=2,column=0,pady=30,padx=30)
    
    
    global texto_mensaje_enviado
    
    texto_mensaje_enviado=Label(frame_mensajes,text="Interfaz de enviado de mensajes",bg="pink",fg="blue")
    texto_mensaje_enviado.grid(row=4,column=1,pady=30)



    

    entrada_destinatario=Text(frame_mensajes,width=30,height=2)
    entrada_destinatario.grid(row=0,column=1,pady=20,padx=45)  

    entrada_mensaje=Text(frame_mensajes,width=30,height=3) 
    entrada_mensaje.grid(row=1,column=1,pady=10,padx=45)

    entrada_clave=Text(frame_mensajes,width=15,height=2)
    entrada_clave.grid(row=2,column=1,pady=20,padx=45)


    clave_codificacion=StringVar(raiz_enviado)

    Radiobutton(frame_mensajes,text="Cifrado Atbash",value="A",bg="pink",variable=clave_codificacion).grid(column=0,row=3)

    Radiobutton(frame_mensajes,text="Cifrado César",value="C",bg="pink",variable=clave_codificacion).grid(column=1,row=3)





    boton_enviar=Button(frame_mensajes,text="Enviar mensaje",command=lambda: agregar_mensaje(entrada_destinatario.get("1.0", "end-1c"),entrada_mensaje.get("1.0", "end-1c"),clave_codificacion.get(),entrada_clave.get("1.0", "end-1c"),usuario))
    boton_enviar.grid(row=4,column=0,pady=160)

    boton_retroceder=Buttonboton_enviar=Button(frame_mensajes,text="Retroceder",command=lambda:retroceder(raiz,raiz_enviado))
    boton_retroceder.place(x=330,y=570)
    

    raiz_enviado.mainloop()
    
    
 
    

def agregar_mensaje(destinatario,mensaje,codificador,clave,usuario):    
    
    

    
    
    
    
    
    
    if chequeo_usuario(destinatario):
        
        with open("mensajes.csv","a",newline="") as archivo_mensajes:
            lector=csv.writer(archivo_mensajes)
            
            
            if codificador=="A":
                lector.writerow([destinatario,mensaje,usuario,codificador])
                
            else:
                lector.writerow([destinatario,mensaje,usuario,codificador+clave])
                    
                
                
            
            
            
             
            
            
            
            
def chequeo_usuario(usuario):
    
    coincidencia=False
    
    with open("registro.csv","r",newline="") as archivo_usuarios:
        lector=csv.reader(archivo_usuarios)
        coincidencia=False
        linea=next(lector,None)
        
        while linea is not None and not coincidencia:
            
            
            if linea[0]==usuario:
                coincidencia=True
            else:
                linea=next(lector,None)
                
                    
            
       
    cambiar_texto(coincidencia)        
            
    return coincidencia       
        
        
        
        
        
    
def cambiar_texto(resultado):
    
    
    if resultado:
        texto_mensaje_enviado.config(text="Se envio el mensaje",fg="green") 
    else:
        texto_mensaje_enviado.config(text="No se envio el mensaje",fg="red")
           
    



