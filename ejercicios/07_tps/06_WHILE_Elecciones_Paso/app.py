'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        cantidad_votos = 0
        total_edades = 0
        contador_candidatos = 0
        nombre_candidato_con_mas_votos = ""
        mayor_cantidad_votos = -1 
        nombre_candidato_menos_votos = ""
        edad_candidato_menos_votos = 0
        menor_cantidad_votos = float('inf')
        
       
        while True:
            nombre = prompt("", "Ingrese su nombre")   
            while nombre == None or not nombre.isalpha(): 
                question("", "¿Desea ingresar otro candidato?")
                nombre = prompt("Ingreso", "Re Ingrese su nombre")

            edad = prompt("Ingreso", "Ingrese su edad")
            while edad == None or not edad.isdigit() or int(edad) < 25:  
                edad = int(prompt("Ingreso", "Re Ingrese su edad"))

            votos = prompt("","Ingrese la cantidad de votos mayor a 0")
            while int(votos) < 0:
                votos = int(prompt("","Ingrese la cantidad de votos mayor a 0"))
                cantidad_votos += votos
                
            if int(votos) > int(mayor_cantidad_votos):
                nombre_candidato_con_mas_votos = nombre
                mayor_cantidad_votos = votos
            elif int(votos) < menor_cantidad_votos:
                nombre_candidato_menos_votos = nombre
                edad_candidato_menos_votos = edad
                menor_cantidad_votos = votos
                
            cantidad_votos += int(votos)
            total_edades += int(edad)
            contador_candidatos += 1

            promedio_edades = total_edades / contador_candidatos 

            if contador_candidatos < 0 or nombre == None or edad == None or votos == None: 
                question("", "¿Debe ingresar un candidato?")
            else: 
                print("Candidato y edad con menos votos: ", nombre_candidato_menos_votos + "" + str(edad_candidato_menos_votos))
                print("Candidato con mas votos: ", nombre_candidato_con_mas_votos)
                print("Cantidad de votos total: ", str(cantidad_votos))
                print("El promedio de edades es: ", str(promedio_edades))

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
