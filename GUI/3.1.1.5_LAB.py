from tkinter import Tk, Button, Canvas, messagebox


phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

counter = 0

def quit():
    answer = messagebox.askyesno(message="Are you shure you want to quit?")

    if answer:
        janela_principal.destroy()


def switch_phase():

    global counter
    counter = counter % 4
    phase = phases[counter]

    if phase[0]:
        canvas.itemconfig(red_signal, fill="red")
    else:
        canvas.itemconfig(red_signal, fill="gray")
    
    if phase[1]:
        canvas.itemconfig(yellow_signal, fill="yellow")
    else:
        canvas.itemconfig(yellow_signal, fill="gray")

    if phase[2]:
        canvas.itemconfig(green_signal, fill="green")
    else:
        canvas.itemconfig(green_signal, fill="gray")  

    counter+=1


janela_principal = Tk()
janela_principal.title("Semáforo")
janela_principal.geometry("350x550")

canvas = Canvas(janela_principal, bg="gray35", width=300, height=450)
canvas.pack()

counter = 0
red_signal = canvas.create_oval(90, 20, 210, 140, width=5)
yellow_signal = canvas.create_oval(90, 160, 210, 280, width=5)
green_signal = canvas.create_oval(90, 300, 210, 420, width=5)


button_next = Button(text="Next", command=switch_phase)
button_next.pack()

button_quit = Button(text="Quit", command=quit, padx=13)
button_quit.pack()


janela_principal.mainloop()