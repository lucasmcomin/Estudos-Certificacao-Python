import tkinter as tk
import random
from tkinter import messagebox
import time


def start(event):

    
    timer_start()
    janela_principal.unbind("<Button-1>")
    print("to aqui")


def timer_start():
    global id
    global clock
    clock+=1
    label["text"] = str(clock)
    id = label.after(1000, timer_start)

def timer_stop():
    label.after_cancel(id)


def clicar(event):
    
    global count
    global btn_number
    btn = event.widget

    if btn["text"] == str(btn_number[count]):
        btn.config(state=tk.DISABLED)
        count+=1
   
    if count == len(btn_number):
        timer_stop()
        messagebox.showinfo(message=f"Seu tempo foi de {clock} segundos", title="Time")
        


janela_principal = tk.Tk()
janela_principal.title("Clicker")
janela_principal.geometry("480x290")

janela_principal.bind("<Button-1>", start)

clock = 0
btn_number = []

iterator = 0
while iterator < 25:
    number = random.randint(1, 999)
    if number not in btn_number:
        btn_number.append(number)
        button = tk.Button(janela_principal, text=str(btn_number[iterator]), width=8, height=2)
        button.grid(row=(iterator // 5), column=(iterator % 5))
        button.bind("<Button-1>", clicar)
        iterator+=1
    
count = 0
btn_number.sort()

label = tk.Label(janela_principal, text="0", pady=25)
label.grid(row=5, column=2)


janela_principal.mainloop()



