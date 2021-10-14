import math
from tkinter import *

def Somar():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    print(n1+n2)
    resultado['text'] = n1+n2

def Subtrair():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    print(n1-n2)
    resultado['text'] = n1-n2

def Dividir():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    print(n1/n2)
    resultado['text'] = n1/n2

def Multiplicar():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    resultado['text'] = n1*n2

def raizQuadrada():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    raiz = math.sqrt(n1, n2)
    resultado['text'] = raiz

root = Tk()

root.geometry("500x300")
root.title("Calculadora")
root.configure(background='gray')

numero1 = Entry()
numero1.grid(row=0, column=0)

numero2 = Entry()
numero2.grid(row=1, column=0)

Button(text="Somar", command= Somar, background='green').grid(row=0, column=1)
Button(text="Subtrair", command= Subtrair, background='green').grid(row=0, column=2)
Button(text="Dividir", command= Dividir, background='green').grid(row=1, column=1)
Button(text="Multiplicar", command=Multiplicar, background='green').grid(row=1, column=2)
Button(text="Raiz Quadrada", command=raizQuadrada, background='green').grid(row=1, column=3)

resultado = Label(text="Resultado", background='green')
resultado.grid(row=3, column=0)

root.mainloop()
