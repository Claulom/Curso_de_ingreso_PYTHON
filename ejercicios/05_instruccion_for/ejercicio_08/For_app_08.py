import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        numeros = prompt("", "Ingrese un número")
        numeros_int = int(numeros)
        mensaje = "Es primo"

        for i in range(2, int(numeros_int/2) + 1): 
            if numeros_int % i == 0:
                mensaje = "No es primo"
                break
        alert("", mensaje)
              

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()