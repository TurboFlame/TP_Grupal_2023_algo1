from tkinter import *

def crear_ventana():
    ventana = Tk()
    ventana.title("ventana de recuperacion")
    
    
    marco = Frame(ventana)
    marco.pack(padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana() 