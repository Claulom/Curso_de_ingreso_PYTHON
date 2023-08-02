'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        bandera = True
        cantidad_postulantes = 0
        cantidad_postulantes_no_binarios = 0
        nombre_postulante_jr_menor = ""
        tecnologia_mas_postulante = ""
        total_edad_F = 0
        cantidad_femeninos = 0
        total_edad_M = 0
        cantidad_masculinos = 0
        total_edad_NB = 0
    
        for i in range(0, 10, 1):
            nombre = prompt("", "Ingrese su nombre")
            while nombre == None or not nombre.isalpha()  : 
                nombre = prompt("Ingreso", "Re Ingrese su nombre")

            edad = prompt("Ingreso", "Ingrese su edad")
            while edad == None or not edad.isdigit() or int(edad) < 18:  
                edad = prompt("Ingreso", "Re Ingrese su edad, No se encuentra en el rango")

            genero = prompt("F-M-NB", "¿Cual es su genero?: F-M-NB")
            while genero == None or not genero.isalpha() or genero != ("F") and genero != ("M") and genero != ("NB"):
                genero = prompt("F-M-NB", "¿Vuelva a ingresar su genero?: F-M-NB")  

            tecnologia = prompt("PYTHON - JS - ASPNET", "Que tecnologia maneja?: PYTHON - JS - ASP.NET")
            while tecnologia == None or not tecnologia.isalpha() or tecnologia != ("PYTHON") and tecnologia != ("JS") and tecnologia != ("ASPNET"):
                tecnologia = prompt("PYTHON - JS - ASP.NET", "¿Vuelva a ingresar que tecnologia maneja?: PYTHON - JS - ASPNET")

            puesto = prompt("Jr - Ssr - Sr", "Para que puesto se postula?: Jr - Ssr - Sr")
            while puesto == None or not puesto.isalpha() or puesto != ("Jr") and puesto != ("Ssr") and puesto != ("Sr"):
                puesto = prompt("F-M-NB", "¿Vuelva a ingresar para que puesto se postula?: Jr - Ssr - Sr")

            if genero == ("NB") and (tecnologia == "ASPNET" or tecnologia == "JS") and (int(edad) > 25 and int(edad) < 40) and (puesto == "Ssr"): #A
                cantidad_postulantes_no_binarios += 1

            if puesto == ("Jr"): #B
                nombre_postulante_jr_menor = edad
                edad > nombre_postulante_jr_menor
                nombre_postulante_jr_menor = nombre
            
            if genero == ("F"):
                total_edad_F += int(edad)
                cantidad_femeninos += 1
            elif genero == ("M"):
                total_edad_M += int(edad)
                cantidad_masculinos += 1
            else:
                genero == ("NB")
                total_edad_NB += int(edad)
                
            if bandera: #D
                tecnologia_mas_postulante = tecnologia
                bandera = False
            else: 
                tecnologia < tecnologia_mas_postulante
                tecnologia_mas_postulante = tecnologia 

            cantidad_postulantes += 1 
    
        if cantidad_femeninos < 0 or cantidad_masculinos < 0 or cantidad_postulantes_no_binarios < 0:
                alert("Error", "Debe existir al menos un de cada genero")
        else:
            promedio_edad_F =  total_edad_F  / cantidad_femeninos
            promedio_edad_M =  total_edad_M / cantidad_masculinos 
            promedio_edad_NB = total_edad_NB / cantidad_postulantes_no_binarios
        
            porcentaje_NB = cantidad_postulantes_no_binarios / cantidad_postulantes
            porcentaje_F = cantidad_femeninos / cantidad_postulantes
            porcentaje_M = cantidad_masculinos / cantidad_postulantes
        
        print("Cantidad de postulantes de genero no binario (NB) \n que programan en ASP.NET o JS cuya edad este entre 25 y 40,\n que se hayan postulado para un puesto Ssr. ",  cantidad_postulantes_no_binarios)
        print("Nombre del postulante Jr con menor edad",  nombre_postulante_jr_menor)
        print("Promedio de edades por género.", "F", promedio_edad_F, "M", promedio_edad_M, "NB", promedio_edad_NB)
        print("Tecnologia con mas postulantes",  tecnologia_mas_postulante)
        print("Porcentaje de postulantes de cada genero",  "F", porcentaje_F, "M", porcentaje_M, "NB", porcentaje_NB)


        """  print(promedio_edades) """
        """  """
        """ promedio_edades = total_edades / cantidad_postulantes  """
        """ 
            total_edades += int(edad) """
        pass 


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
