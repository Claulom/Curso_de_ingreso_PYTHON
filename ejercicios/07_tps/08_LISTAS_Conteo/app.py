import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        ingreso_numeros = 0

        while True:
            if ingreso_numeros == "" or ingreso_numeros == None:
                    break
            ingreso_numeros = prompt("Ingreso", "Ingrese un número")
            numeros = int(ingreso_numeros)
            self.lista.append(numeros)
                

    def btn_mostrar_estadisticas_on_click(self):
        suma_numeros_positivos = 0
        suma_numeros_negativos = 0
        cantidad_numeros_positivos = 0
        cantidad_numeros_negativos = 0
        cantidad_ceros_ingresados = 0
        minimo_numero_negativo = None
        maximo_numero_positivo = None
        promedio_numeros_negativos = 0

        for numero in self.lista:
            if numero < 0:
                suma_numeros_negativos += numero
                cantidad_numeros_negativos += 1
                if minimo_numero_negativo is None or numero < minimo_numero_negativo:
                    minimo_numero_negativo = numero
            elif numero > 0:
                suma_numeros_positivos += numero
                cantidad_numeros_positivos += 1
                if maximo_numero_positivo is None or numero > maximo_numero_positivo:
                    maximo_numero_positivo = numero
            else:
                cantidad_ceros_ingresados += 1

            if cantidad_numeros_negativos > 0:
                promedio_numeros_negativos = suma_numeros_negativos / cantidad_numeros_negativos

        mensaje = "Los numeros negativos son {0}, los numeros positivos son {1}, \n se ingresaron {2} numeros positivos y {3} negativos \n el numero minimo negativo es {4} y el numero maximo positivo es {5} \n el promedio de los numeros negativos es {6} \n, la cantidad de ceros ingresados es {7}".format(suma_numeros_negativos, suma_numeros_positivos, cantidad_numeros_positivos, cantidad_numeros_negativos, minimo_numero_negativo, maximo_numero_positivo, promedio_numeros_negativos,cantidad_ceros_ingresados)
        alert("", mensaje)
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
