#Importo librerías
from tkinter import *
import tkinter
from urllib3 import *
import urllib.request

urllib.request.urlretrieve('https://cdn-icons-png.flaticon.com/512/346/346399.png', "icono-calculadora.png")
colordark = "#171717"
weix2 = 1


colordow = colordark

class Calculadora:
    def __init__(self) -> None:
        
        #Creo la ventana
        self.root = Tk()
        #root.geometry("274x328")
        self.root.config(bg=colordow, padx=3, pady=4)
        self.root.title("Calculadora :D")

        #CONFIGURO VENTANA Y SUS VERTICALES Y HORIZONTALES
        #self.root.minsize(width=268, height=369)
        
        #Configuro el icono de la ventana:
        self.root.iconphoto(False,tkinter.PhotoImage(file='icono-calculadora.png'))

        #####################################################################
        
        self.i = 99999
        
        #####################################################################
        
        # Ingresar (por botones o teclado)

        self.entry = Entry(self.root, font="Sans", bg="seagreen")
        self.entry.grid(row=0, columnspan=4, sticky=W+E, ipady=2, pady=(4, 10))

        operar = ""

        #Valores graficos de los botones de numeros:
        
        self.color_btn_num = "#777"
        self.fg_btn_num = "#0f0f0f"
        
        self.tmñ_btn_num_x = 7
        self.tmñ_btn_num_y = 3
        
        self.padx_num = 1
        self.pady_num = 1
        
        self.font_num = "Sans"

        #Valores graficos de los botones de las operaciones:
        
        self.color_btn_oper = "#555"
        self.fg_btn_oper = "#ddd"
        
        self.tmñ_btn_oper_x = 7
        self.tmñ_btn_oper_y = 3
        
        self.padx_oper = 1
        self.pady_oper = 1
        
        self.font_oper = "Sans"
        
        #Valores graficos de los botones de los parentesis:
        self.color_btn_par = "#006"
        self.fg_btn_par = "#aaf"
        
        self.tmñ_btn_par_x = 7
        self.tmñ_btn_par_y = 3
        
        self.padx_par = 1
        self.pady_par = 1
        
        self.font_par = "Sans"
        
        #Valores graficos del boton de igual:
        self.color_btn_igual = "#88f"
        self.fg_btn_igual = "#000"
        
        self.tmñ_btn_igual_x = 7
        self.tmñ_btn_igual_y = 3
        
        self.padx_igual = 1
        self.pady_igual = 1
        
        self.font_igual = "Sans"
        
        #Valores graficos del boton de punto:
        self.color_btn_punto = "#1080B7"
        self.fg_btn_punto = "#000"
        
        self.tmñ_btn_punto_x = 7
        self.tmñ_btn_punto_y = 3
        
        self.padx_punto = 1
        self.pady_punto = 1
        
        self.font_punto = "Sans"
        
        
        
        #Botones De NumerosS

        self.btnUno = Button(self.root, text="1", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("1")).grid(row=1, column=0, sticky=W+E, padx=self.padx_num, pady= self.pady_num)
        self.btnDos = Button(self.root, text="2", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("2")).grid(row=1, column=1, sticky=W+E, padx=self.padx_num, pady= self.pady_num)
        self.btnTres = Button(self.root, text="3", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("3")).grid(row=1, column=2, sticky=W+E, padx=self.padx_num, pady= self.pady_num)

        self.btnCuatro = Button(self.root, text="4", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("4")).grid(row=2, column=0, sticky=W+E, padx=self.padx_num, pady= self.pady_num)
        self.btnCinco = Button(self.root, text="5", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("5")).grid(row=2, column=1, sticky=W+E, padx=self.padx_num, pady= self.pady_num)
        self.btnSeis = Button(self.root, text="6", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("6")).grid(row=2, column=2, sticky=W+E, padx=self.padx_num, pady= self.pady_num)

        self.btnSiete = Button(self.root, text="7", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("7")).grid(row=3, column=0, sticky=W+E, padx=self.padx_num, pady= self.pady_num)
        self.btnOcho = Button(self.root, text="8", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("8")).grid(row=3, column=1, sticky=W+E, padx=self.padx_num, pady= self.pady_num)
        self.btnNueve = Button(self.root, text="9", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("9")).grid(row=3, column=2, sticky=W+E, padx=self.padx_num, pady= self.pady_num)

        self.btnCero = Button(self.root, text="0", font=self.font_num, fg=self.fg_btn_num, bg=self.color_btn_num, width=self.tmñ_btn_num_x, height=self.tmñ_btn_num_y, command=lambda:self.get_char("0")).grid(row=4, column=0, sticky=E+W, padx=self.padx_num, pady= self.pady_num)

        #Otros botones

        self.btnBorrar = Button(self.root, text="AC", bg="#B7B100", command=lambda:self.clear_entry()).grid(row=0, column=4, sticky=W+E)
        self.btnBorrar_uno = Button(self.root, text="⟸", command=lambda:self.clear_uno()).grid(row=1, column=3, columnspan=2, sticky=W+E)

        self.btnSum = Button(self.root, text="+", font=self.font_oper, fg=self.fg_btn_oper, bg=self.color_btn_oper, width=self.tmñ_btn_oper_x, height=self.tmñ_btn_oper_y, command=lambda:self.get_char("+")).grid(row=2, column=3, sticky=W+E, padx=self.padx_oper, pady=self.pady_oper)
        self.btnRestar = Button(self.root, text="-", font=self.font_oper, fg=self.fg_btn_oper, bg=self.color_btn_oper, width=self.tmñ_btn_oper_x, height=self.tmñ_btn_oper_y, command=lambda:self.get_char("-")).grid(row=3, column=3, sticky=W+E, padx=self.padx_oper, pady=self.pady_oper)
        self.btnMulti = Button(self.root, text="x", font=self.font_oper, fg=self.fg_btn_oper, bg=self.color_btn_oper, width=self.tmñ_btn_oper_x, height=self.tmñ_btn_oper_y, command=lambda:self.get_char("x")).grid(row=4, column=3, sticky=W+E, padx=self.padx_oper, pady=self.pady_oper)
        self.btnIgual = Button(self.root, text="=", font=self.font_igual, fg=self.fg_btn_igual, bg=self.color_btn_igual, width=self.tmñ_btn_igual_x, height=self.tmñ_btn_igual_y, command=self.operate).grid(row=5, column=0, columnspan=2, sticky=W+E, padx=self.padx_igual, pady=self.pady_igual)

        self.btnDividir = Button(self.root, text="÷", font=self.font_oper, fg=self.fg_btn_oper, bg=self.color_btn_oper, width=self.tmñ_btn_oper_x, height=self.tmñ_btn_oper_y, command=lambda:self.get_char("÷")).grid(row=4, column=2, sticky=W+E, padx=self.padx_oper, pady=self.pady_oper)
        self.btnPotencia = Button(self.root, text="▫", font=self.font_oper, fg=self.fg_btn_oper, bg=self.color_btn_oper, width=self.tmñ_btn_oper_x, height=self.tmñ_btn_oper_y, command=lambda:self.get_char("▫")).grid(row=3, column=4, sticky=W+E, padx=self.padx_oper, pady=self.pady_oper)
        self.btnPar1 = Button(self.root, text="(", font=self.font_par, fg=self.fg_btn_par, bg=self.color_btn_par, width=self.tmñ_btn_par_x, height=self.tmñ_btn_par_y, command=lambda:self.get_char("(")).grid(row=5, column=2, sticky=W+E, padx=self.padx_par, pady=self.pady_par)
        self.btnPar2 = Button(self.root, text=")", font=self.font_par, fg=self.fg_btn_par, bg=self.color_btn_par, width=self.tmñ_btn_par_x, height=self.tmñ_btn_par_y, command=lambda:self.get_char(")")).grid(row=5, column=3, sticky=W+E, padx=self.padx_par, pady=self.pady_par)
        self.btnPunto = Button(self.root, text=".", font=self.font_punto, fg=self.fg_btn_punto, bg=self.color_btn_punto, width=self.tmñ_btn_punto_x, height=self.tmñ_btn_punto_y, command=lambda:self.get_char(".")).grid(row=4, column=1, sticky=W+E, padx=self.padx_punto, pady=self.pady_punto)

    #Función para insertar un caracter en el entry:
    def get_char(self, n):
        self.entry.insert(self.i, n)
        #i+=1


    #Función para calcular la operación del entry y mostrarla en pantalla:
    def operate(self):
        try:
            operar = self.entry.get()
            operar = operar.replace("x", "*").replace("÷", "/").replace("▫", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(",", ".").replace("Error", "")
            operar = eval(operar)
            operar = str(operar)
            self.clear_entry()
            self.entry.insert(0, operar)
        except:
            self.clear_entry()
            self.entry.insert(0,"Error")

    #Función para borrar todo el texto del entry:
    def clear_entry(self):
        self.entry.delete(0, END)

    #Función para borrar un caracter del entry
    def clear_uno(self):
        entry_state = self.entry.get()
        if "Error" in entry_state:
            self.clear_entry()
        else:
            if len(entry_state):
                entry_new_state = entry_state[:-1]
                self.clear_entry()
                self.entry.insert(0,entry_new_state)
            else:
                self.clear_entry()
                self.entry.insert(0, "Error")



#Llamar a la clase
ventana = Calculadora()
#Actualizar constantemente la ventana :D
ventana.root.mainloop()

#Eso fue todo :D