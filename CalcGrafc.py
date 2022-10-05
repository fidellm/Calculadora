#Importo librerías
from tkinter import *
import tkinter
from urllib3 import *
import urllib.request

urllib.request.urlretrieve('https://cdn.icon-icons.com/icons2/923/PNG/512/calculator_icon-icons.com_72046.png', "icono.png")
colordark = "#171717"
weix2 = 1


colordow = colordark


#Creo ventana
root = Tk()
#root.geometry("274x328")
root.config(bg=colordow)
root.title("Calculadora :D")

#CONFIGURO VENTANA Y SUS VERTICALES Y HORIZONTALES
root.minsize(width=268, height=369)
root.iconphoto(False,tkinter.PhotoImage(file='icono.png'))

#Columna 0

root.columnconfigure(0, weight=weix2)
root.rowconfigure(0, weight=weix2)

root.columnconfigure(0, weight=weix2)
root.rowconfigure(1, weight=weix2)

root.columnconfigure(0, weight=weix2)
root.rowconfigure(2, weight=weix2)

root.columnconfigure(0, weight=weix2)
root.rowconfigure(3, weight=weix2)

root.columnconfigure(0, weight=weix2)
root.rowconfigure(4, weight=weix2)

root.columnconfigure(0, weight=weix2)
root.rowconfigure(5, weight=weix2)

root.columnconfigure(0, weight=weix2)
root.rowconfigure(6, weight=weix2)


#Columna 1

root.columnconfigure(1, weight=weix2)
root.rowconfigure(0, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(1, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(2, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(3, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(4, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(5, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(6, weight=weix2)

#Columna 2

root.columnconfigure(1, weight=weix2)
root.rowconfigure(0, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(1, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(2, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(3, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(4, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(5, weight=weix2)

root.columnconfigure(1, weight=weix2)
root.rowconfigure(6, weight=weix2)

#Columna 2

root.columnconfigure(2, weight=weix2)
root.rowconfigure(0, weight=weix2)

root.columnconfigure(2, weight=weix2)
root.rowconfigure(1, weight=weix2)

root.columnconfigure(2, weight=weix2)
root.rowconfigure(2, weight=weix2)

root.columnconfigure(2, weight=weix2)
root.rowconfigure(3, weight=weix2)

root.columnconfigure(2, weight=weix2)
root.rowconfigure(4, weight=weix2)

root.columnconfigure(2, weight=weix2)
root.rowconfigure(5, weight=weix2)

root.columnconfigure(2, weight=weix2)
root.rowconfigure(6, weight=weix2)

# Columna 3

root.columnconfigure(3, weight=weix2)
root.rowconfigure(0, weight=weix2)

root.columnconfigure(3, weight=weix2)
root.rowconfigure(1, weight=weix2)

root.columnconfigure(3, weight=weix2)
root.rowconfigure(2, weight=weix2)

root.columnconfigure(3, weight=weix2)
root.rowconfigure(3, weight=weix2)

root.columnconfigure(3, weight=weix2)
root.rowconfigure(4, weight=weix2)

root.columnconfigure(3, weight=weix2)
root.rowconfigure(5, weight=weix2)

root.columnconfigure(3, weight=weix2)
root.rowconfigure(6, weight=weix2)

# Columna 4

root.columnconfigure(4, weight=weix2)
root.rowconfigure(0, weight=weix2)

root.columnconfigure(4, weight=weix2)
root.rowconfigure(1, weight=weix2)

root.columnconfigure(4, weight=weix2)
root.rowconfigure(2, weight=weix2)

root.columnconfigure(4, weight=weix2)
root.rowconfigure(3, weight=weix2)

root.columnconfigure(4, weight=weix2)
root.rowconfigure(4, weight=weix2)

root.columnconfigure(4, weight=weix2)
root.rowconfigure(5, weight=weix2)

root.columnconfigure(4, weight=weix2)
root.rowconfigure(6, weight=weix2)


############################################



# Ingresar (por botones o teclado)

entry = Entry(root, bg="seagreen")
entry.grid(row=0, columnspan=4, sticky=W+E)

operar = ""

# Comandos

i = 99999

def get_char(n):
    global i
    entry.insert(i, n)
    #i+=1


def operate():
    try:
        operar = entry.get()
        operar = operar.replace("x", "*").replace("÷", "/").replace("▫", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(",", ".").replace("Error", "")
        operar = eval(operar)
        operar = str(operar)
        clear_entry()
        entry.insert(0, operar)
    except:
        clear_entry()
        entry.insert(0,"Error")

def clear_entry():
    entry.delete(0, END)

def clear_uno():
    entry_state = entry.get()
    if "Error" in entry_state:
        clear_entry()
    else:
        if len(entry_state):
            entry_new_state = entry_state[:-1]
            clear_entry()
            entry.insert(0,entry_new_state)
        else:
            clear_entry()
            entry.insert(0, "Error")


#Numeros

coln = "#D30015"

uno = Button(root, text="1", bg=coln, command=lambda:get_char("1")).grid(row=1, column=0, sticky=W+E)
dos = Button(root, text="2", bg=coln, command=lambda:get_char("2")).grid(row=1, column=1, sticky=W+E)
tres = Button(root, text="3", bg=coln, command=lambda:get_char("3")).grid(row=1, column=2, sticky=W+E)

cuatro = Button(root, text="4", bg=coln, command=lambda:get_char("4")).grid(row=2, column=0, sticky=W+E)
cinco = Button(root, text="5", bg=coln, command=lambda:get_char("5")).grid(row=2, column=1, sticky=W+E)
seis = Button(root, text="6", bg=coln, command=lambda:get_char("6")).grid(row=2, column=2, sticky=W+E)

siete = Button(root, text="7", bg=coln, command=lambda:get_char("7")).grid(row=3, column=0, sticky=W+E)
ocho = Button(root, text="8", bg=coln, command=lambda:get_char("8")).grid(row=3, column=1, sticky=W+E)
nueve = Button(root, text="9", bg=coln, command=lambda:get_char("9")).grid(row=3, column=2, sticky=W+E)

cero = Button(root, text="0", bg=coln, command=lambda:get_char("0")).grid(row=4, column=0, sticky=E+W)

#Otros botones

borrar = Button(root, text="AC", bg="#B7B100", command=lambda:clear_entry()).grid(row=0, column=4, sticky=W+E)
borrar_uno = Button(root, text="⟸", command=lambda:clear_uno()).grid(row=1, column=3, columnspan=2, sticky=W+E)

sum = Button(root, text="+", bg="#117368", command=lambda:get_char("+")).grid(row=2, column=3, sticky=W+E)
rest = Button(root, text="-", bg="#117368", command=lambda:get_char("-")).grid(row=3, column=3, sticky=W+E)
mult = Button(root, text="x", bg="#117368", command=lambda:get_char("x")).grid(row=4, column=3, sticky=W+E)
igual = Button(root, text="=", bg="#636363", command=operate).grid(row=5, column=0, columnspan=2, sticky=W+E)

div = Button(root, text="÷", bg="#117368", command=lambda:get_char("÷")).grid(row=4, column=2, sticky=W+E)
Pot = Button(root, text="▫", bg="#117368", command=lambda:get_char("▫")).grid(row=3, column=4, sticky=W+E)
par1 = Button(root, text="(", bg="#252525", command=lambda:get_char("(")).grid(row=5, column=2, sticky=W+E)
par2 = Button(root, text=")", bg="#252525", command=lambda:get_char(")")).grid(row=5, column=3, sticky=W+E)
punt = Button(root, text=".", bg="#1080B7", command=lambda:get_char(".")).grid(row=4, column=1, sticky=W+E)


#Actualizar constantemente la ventana :D
root.mainloop()

#Eso fue todo :D