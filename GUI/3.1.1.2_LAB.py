import tkinter as tk
from tkinter import messagebox


def calcular():
    if (termo_1.get().isdigit()) and (termo_2.get().isdigit()):
        resultado = 0
        print(operador_selecionado.get())
        match (operador_selecionado.get()):
        
            case 0:
                resultado = float(termo_1.get()) + float(termo_2.get())
                messagebox.showinfo(title="Resultado", message=f"Resultado: {resultado}")
            case 1:
                resultado = float(termo_1.get()) - float(termo_2.get())
                messagebox.showinfo(title="Resultado", message=f"Resultado: {resultado}")

            case 2: 
                resultado =  float(termo_1.get()) * float(termo_2.get())
                messagebox.showinfo(title="Resultado", message=f"Resultado: {resultado}")

            case 3:
                if (float(termo_2.get()) != 0):
                    resultado =  float(termo_1.get()) / float(termo_2.get())
                    messagebox.showinfo(title="Resultado", message=f"Resultado: {resultado}")
                else:
                    messagebox.showerror(title="Erro", message="Erro! Divisição por 0 não é permitida. ")
                    termo_2.focus()
    
    else:
        messagebox.showwarning(title="Atenção", message="Por favor, digite apenas números!")
        if (not termo_1.get().isdigit()):
            termo_1.focus()

        if (not termo_2.get().isdigit()):
            termo_2.focus()



janela_principal = tk.Tk()
janela_principal.title("Calculadora")
janela_principal.geometry("430x150")
operador_selecionado = tk.IntVar()
operador_selecionado.set(0)

operador_adicao = tk.Radiobutton(janela_principal, text = "+", variable=operador_selecionado, value=0)
operador_adicao.grid(column=1, row=0)

operador_subtracao = tk.Radiobutton(janela_principal, text = "-", variable=operador_selecionado, value=1)
operador_subtracao.grid(column=1, row=1)

termo_1 = tk.Entry(janela_principal,)
termo_1.grid(column=0, row=2)

operador_multiplicacao= tk.Radiobutton(janela_principal,text = "*",variable=operador_selecionado, value=2)
operador_multiplicacao.grid(column=1, row=2)

termo_2 = tk.Entry(janela_principal,)
termo_2.grid(column=2, row=2)

operador_divisao = tk.Radiobutton(janela_principal,text = "/", variable=operador_selecionado, value=3)
operador_divisao.grid(column=1, row=3)

botao_resultado = tk.Button(janela_principal,text="Resultado", command=calcular) 
botao_resultado.grid(column=1, row=4)

janela_principal.mainloop()


            


