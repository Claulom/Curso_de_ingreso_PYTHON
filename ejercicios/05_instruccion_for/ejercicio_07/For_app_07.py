import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        cantidad_numeros_divisores = 0

        numeros = prompt("", "Ingrese un número")
        numeros_int = int(numeros)

        for i in range(1, numeros_int, 1): 
            if numeros_int % i == 0:
                cantidad_numeros_divisores += 1
                print("Los numeros divisores de", str(numeros), "son: ", i)
              
        print("","La cantidad de numeros total es:", str(cantidad_numeros_divisores) )
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()