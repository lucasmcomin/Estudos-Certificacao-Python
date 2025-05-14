import tkinter as tk
from tkinter import messagebox
from random import randint
import time

pontos = 0

def move(event):
    
    pos_x = randint(0, janela_principal.winfo_width() -80)
    pos_y = randint(0, janela_principal.winfo_height() - 30)
    time.sleep(0.2)
    botao_catch.place(x=pos_x, y=pos_y)

def clicou():
    global pontos
    pontos = pontos+1
    messagebox.showinfo(title="Ganhou!", message=f"Você Ganhou!!!!!! Você tem {pontos} pontos")

pontos = 0
janela_principal = tk.Tk()
janela_principal.title("Catch me if you can!!")
janela_principal.geometry("1025x712")
janela_principal.update_idletasks()
botao_catch = tk.Button(janela_principal, text="Catch me!", command=clicou)
botao_catch.place(x=10, y=10, width=80, height=30)
botao_catch.bind("<Enter>", move)
janela_principal.mainloop()
