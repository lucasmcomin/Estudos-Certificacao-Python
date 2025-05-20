"""
Learn practical skills related to:

dealing with observable variables,
working with the Entry widget,
constructing complex interfaces with many cooperating Button widgets.

Scenario:

Have you ever used an ordinary pocket calculator? We prefer to ask you first as we're aware of the fact that these devices went out of fashion some time ago 
and they were replaced with computer and smartphone's applications.

This is exactly what we want you to implement - a simple, four-function "pocket" calculator. Feel free to equip it with many extra functions, but adding, 
subtracting, multiplying and dividing is a must - there is no calculator without these operations.

Moreover, the calculator needs a change sign function, a decimal point button and the clear button. We don't have to mention that your calculator should be 
resistant to zero-division attempts, in which case it should display an error message instead of producing any garbage result or raising an exception.

The screenshots we present below are just a suggestion. You can design the UI in a different way, and it will be good as long as your calculator works properly. 
We aren't able to collect all strict requirements in one place - we can only say that each time you have doubts about how to implement a particular behavior, you should just pick up a real pocket calculator and check how it works in the specific context.

See how we've implemented our GUI (initial state, presenting a result, and handling zero-division attempt) - do you like it?

Calculator at initial state Calculator presenting a result Calculator after zero-divide attempt



Here are some of our assumptions:

respond only to mouse clicks; keyboard presses can be silently ignored,
the display's width is 10 - use a fixed-width font to work with it,
you are not allowed to fill the display with more than 10 characters (including the decimal point and minus sign if it is needed); if the result needs more characters to be presented, you should display an error message,
you are allowed to remove some less significant digits located after the decimal point to shorten the result in effect,
if the result has no significant digits after the decimal point, the point should not appear on the display.
"""


import tkinter as tk
from tkinter import Entry


expression = ""


#sign funtion, changes the signal of expressions and numbers
def change_sign():
    global expression
    if expression!="":

        try:
            result = - (eval(expression))
            display["text"] = result
            expression = str(result)
        except:
            display["text"] = "Error!"



#insert digits on the calculator display
def insert_display(widget):
    global expression

    #this block block entrance of 2 operators or 2 dots consequently.
    if expression != "":
        if not expression[len(expression)-1].isdigit() and not widget["text"].isdigit():
            if widget["text"] != ".":
                expression = expression[:-1]
            elif expression[len(expression)-1]  == ".":
                expression = expression[:-1]

    expression += widget["text"]
    display["text"] = expression

#clean
def clear_display():
    global expression
    expression = ""
    display["text"] = "0"


#calculate the expression in display
def calculate():
    global expression
    if expression!="":

        #trows and exception if some errors occur, like division by zero or some incorrect expressions
        try:
            result = eval(expression)
            display["text"] = result
            expression = str(result)
        except:
            display["text"] = "Error!"


calculadora = tk.Tk()
calculadora.title("Calculadora")


display = tk.Label(calculadora, width=23, background="white", text="0", anchor="e")
display.grid(row=0, column=0, columnspan=5)

button_7 = tk.Button(calculadora, text="7", command = lambda: insert_display(button_7))
button_7.grid(row=1, column=0)

button_8 = tk.Button(calculadora, text="8", command = lambda: insert_display(button_8))
button_8.grid(row=1, column=1)

button_9 = tk.Button(calculadora, text="9", command = lambda: insert_display(button_9))
button_9.grid(row=1, column=2)

button_add = tk.Button(calculadora, text="+", width=1, command = lambda: insert_display(button_add))
button_add.grid(row=1, column=4)

button_4 = tk.Button(calculadora, text="4",command = lambda: insert_display(button_4))
button_4.grid(row=2, column=0)

button_5 = tk.Button(calculadora, text="5", command = lambda: insert_display(button_5))
button_5.grid(row=2, column=1)

button_6 = tk.Button(calculadora, text="6", command = lambda: insert_display(button_6))
button_6.grid(row=2, column=2)

button_sub = tk.Button(calculadora, text="-", width=1, command = lambda: insert_display(button_sub))
button_sub.grid(row=2, column=4)

button_1 = tk.Button(calculadora, text="1", command = lambda: insert_display(button_1))
button_1.grid(row=3, column=0)

button_2 = tk.Button(calculadora, text="2", command = lambda: insert_display(button_2))
button_2.grid(row=3, column=1)

button_3 = tk.Button(calculadora, text="3", command = lambda: insert_display(button_3))
button_3.grid(row=3, column=2)

button_equals = tk.Button(calculadora, text="=",width=2, command=calculate)
button_equals.grid(row=3, column=3)

button_mul= tk.Button(calculadora, text="*", width=1, command = lambda: insert_display(button_mul))
button_mul.grid(row=3, column=4)

button_c = tk.Button(calculadora, text="C", command=clear_display)
button_c.grid(row=4, column=0)

button_0 = tk.Button(calculadora, text="0", command = lambda: insert_display(button_0))
button_0.grid(row=4, column=1)

button_dot = tk.Button(calculadora, text=".", width=1, command = lambda: insert_display(button_dot))
button_dot.grid(row=4, column=2)

button_pos_neg = tk.Button(calculadora, text="+/-", width=2, command=change_sign)
button_pos_neg.grid(row=4, column=3)

button_divided = tk.Button(calculadora, text="/", width=1, command = lambda: insert_display(button_divided))
button_divided.grid(row=4, column=4)





calculadora.mainloop()
