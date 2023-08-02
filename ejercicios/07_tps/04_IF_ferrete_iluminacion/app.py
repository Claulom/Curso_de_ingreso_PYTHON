import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Claudio
Apellido: Lombao
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        precio = 800
        cantidad = int(self.combobox_cantidad.get())
        proveedor = self.combobox_marca.get()
        precio_total = precio * cantidad
        precio_final = precio_total * 0.5      

        """
        PRECIO = 800
        descuento = 0
        mensaje = ""

        cantidad = int(self.combobox_cantidad.get())
        proveedor = self.combobox_marca.get()
        precio_total = precio * cantidad
        precio_final = precio_total * descuento 
        
        if cantidad >= 6:
            descuento = 50
        elif cantidad == 5:
        descuento = 30
        if proveedor == "ArgentinaLuz"
            descuento = 40
        elif cantidad == 4:
            descuento = 20
            if proveedor == "ArgentinaLuz" or proveedor == "FelipeLamparas"
            descuento = 25
            elif cantidad == 3:
            descuento = 5
            if proveedor == "ArgentinaLuz"
            descuento = 15
            elif proveedor == "FelipeLamparas"
            descuento = 10

            descParaAplicar = precio_total * descuento / 100
            precioConDesc = precio_total - descParaAplicar  
            
            
            
            SALIDA
            alert("Recibo", mensaje)
           """


        if  cantidad >= 6:
                descuento_50 = precio_total * 0.5
                alert("Hola", "Usted tiene un descuento del 50% por haber comprado 6 o más lamparitas, el total es $" + str(descuento_50))
        #elif cantidad == 3 or cantidad == 5 and proveedor == "ArgentinaLuz":
        elif cantidad == 5 and proveedor == "ArgentinaLuz":
                descuento_40 = precio_total * 0.4
                alert("Hola", "Usted tiene un descuento del 40% por haber comprado 5 lamparitas de ArgentinaLuz, el total es $" + str(descuento_40))

        elif cantidad == 5 and proveedor != "ArgentinaLuz":
                descuento_30 = precio_total * 0.3
                alert("Hola", "Usted tiene un descuento del 30% por haber comprado 5 lamparitas, el total es $" + str(descuento_30))

        elif cantidad == 4 and proveedor == "ArgentinaLuz" or proveedor == "FelipeLamparas":
                descuento_25 = precio_total * 0.25
                alert ("Hola", "Usted tiene un descuento del 25% por haber comprado 4 lamparitas, el total es $" + str(descuento_25))

        elif cantidad == 4 and proveedor != "ArgentinaLuz" or proveedor != "FelipeLamparas":
                descuento_20 = precio_total * 0.2
                alert ("Hola", "Usted tiene un descuento del 20% por haber comprado 4 lamparitas, el total es $" + str(descuento_20))

        elif cantidad == 3 and proveedor == "ArgentinaLuz":
                descuento_15 = precio_total * 0.15 
                alert ("Hola", "Usted tiene un descuento del 15% por haber comprado 3 lamparitas, el total es $" + str(descuento_15))

        elif cantidad == 3 and proveedor == "FelipeLamparas":
                descuento_10 = precio_total * 0.1 
                alert ("Hola", "Usted tiene un descuento del 15% por haber comprado 3 lamparitas, el total es $" + str(descuento_10))

        elif cantidad == 3 and proveedor != "ArgentinaLuz" or proveedor != "FelipeLamparas":
                descuento_5 = precio_total * 0.05
                alert ("Hola", "Usted tiene un descuento del 5% por haber comprado 3 lamparitas, el total es $" + str(descuento_5)) 

        if precio_final >= 4000:
                descuento_5 = precio_total * 0.05
                desc_55 = precio_final + descuento_5
                alert("Hola", "Tenes un decuento adicional, tu total es" + str(desc_55))

        """ elif cantidad >= 6 and precio_total >= 8000:
            descuento_55 = precio_total + 4000 * 0.55
            alert("Hola", "Usted tiene un descuento del 50% por haber comprado 6 o más lamparitas, el total es $" + str(descuento_55))  """
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()