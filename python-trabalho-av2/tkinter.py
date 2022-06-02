from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Calculadora")
        self.msg["font"] = ("Verdana", "10", "italic")
        self.botao1 = Button(self.widget1, text="1", width=5)
        self.botao1["text"] = "x"
        self.botao1["font"] = ("Verdana", "10", "italic")
        self.botao1["width"] = 5
        self.botao1["command"] = self.produto
        self.botao1.pack()
        
    def produto(self):
        if self.msg["text"] == "Calculadora":
            self.msg["text"] = "CALCULADORA", prod
        else:
            self.msg["text"] = "Calculadora"
            
    def soma(self):
        if self.msg["text"] == "Calculadora":
            self.msg["text"] = "CALCULADORA", adicao
        else:
            self.msg["text"] = "Calculadora"
        
A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))
prod = A * B
adicao = A + B

root = Tk()
Application(root)
root.mainloop()