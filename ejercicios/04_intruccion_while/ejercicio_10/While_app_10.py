import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()


'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        mensaje = "Los valores ingresados son: "
        cant_negativo = 0
        cant_positivo = 0
        suma_pos = 0
        suma_neg = 0
        ceros = 0
       

        while True:  
            ingreso = prompt("Ingreso", "Ingrese un número")  
            if ingreso == None or ingreso == "":
                break
            ingreso_int = int(ingreso)
            if ingreso_int == 0:
                ceros += 1 
                mensaje 
            elif ingreso_int < 0 :
                    cant_negativo += 1
                    suma_neg += ingreso_int
                    mensaje 
            else: 
                ingreso_int > 0
                cant_positivo += 1
                suma_pos += ingreso_int
                mensaje
                        
        
        dif = cant_positivo - cant_negativo

        if ingreso == None:
            alert("", "Ingrese un valor")
        else:
            alert("", mensaje  + "\n" + "cantidad de Ceros, " + str(ceros)  + "\n" + " la cantidad de negativos, "  + str(cant_negativo) + "\n" + " la cantidad de positivos, "  + str(cant_positivo) + "\n" + " La suma de los valores negativos es: " + str(suma_neg) + "\n" + 
            " La suma de los valores positivos es: " + str(suma_pos) + "\n" + "La diferencia entre cantidades de positivos y negativos es: " + str(dif))
            
        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
