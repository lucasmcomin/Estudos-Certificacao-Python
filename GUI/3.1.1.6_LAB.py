"""Estimated time
30-45 minutes

Level of difficulty
Hard

Objectives
Learn practical skills related to:

dealing with the grid geometry manager,
defining and using callbacks,
identifying and servicing GUI events.
Scenario
Write a simple GUI program which pretends to play tic-tac-toe with the user. Don't be afraid, we don't want you to implement artificial intelligence algorithms. You can do it, if you want, but we prefer to concentrate on the user interface issues. If you really want to create an actual competitor, do it on your own.


To make your task a bit easier, let's simplify the game a bit. Here are our assumptions:.

the computer (i.e., your program) plays 'X', and Xes are always red,
the user (e.g., you) plays 'O', and Os are always green,
the board consists of 9 tiles, and the tile role is played by a button,
the first move belongs to the computer - it always puts its first 'X' in the middle of the board,
the user enters her/his move by clicking the chosen tile (clicking the tiles which are not free is ineffective)
the program checks if the game over conditions are met, and if the game is over, a message box is displayed announcing the winner,
otherwise the computer responds with its move and the check is repeated,
use random to generate the computer's moves."""


from tkinter import *
from tkinter import messagebox
import random
import time


strokes = ["", "", "", "", "", "", "", "", ""]


def clear_game():
    #clear all the strokes except the stroke in 4th position, that represents the central button
    for i in range(0, 9):
        if i != 4:
            strokes[i] = ""
    
    #clear all the buttons labels except the central button
    for button in buttons:
        if button.winfo_name() != "!button5":
            if (button.children != {}):
                button.winfo_children()[0].destroy()

            button["state"] = NORMAL
        
def record_position(button, signal):
    
    #add a signal "X" or "O" in a strokes position based in button variable name that was clicked
    match(button.winfo_name()):

        case "!button":
            strokes[0] = signal

        case "!button2":
            strokes[1] = signal
        
        case "!button3":
            strokes[2] = signal
        
        case "!button4":
            strokes[3] = signal

        case "!button5":
            strokes[4] = signal
        
        case "!button6":
            strokes[5] = signal

        case "!button7":
            strokes[6] = signal
        
        case "!button8":
            strokes[7] = signal

        case "!button9":
            strokes[8] = signal



def place(widget, signal, color):
    #add a label into a widget
    label = Label(widget, text=signal, font=("Arial, 65"), fg=color, relief="flat")
    label.place(x=40, y=14) 


def random_play():    
    run = True

    while(run):
        #randow stroke - op smibolizes a position in strokes
        op = random.randint(0, 8)
        #vverify if there isn´t a stroke in the random position
        if strokes[op]=="":
            #update button label at op position
            place(buttons[op], "X", "red")
            #record at stroke list
            record_position(buttons[op], "X")
            buttons[op]["state"] = DISABLED
            run = False


def win(signal):

    #verify all the possibilits to win the game acessing de strokes list 
        
    if strokes[0] == signal and strokes[1] == signal and strokes[2] == signal: #row 1
        return True
    elif strokes[0] == signal and strokes[4] == signal and strokes[8] == signal: # transversal starting from the row1, column 1
        return True
    elif strokes[0] == signal and strokes[3] == signal and strokes[6] == signal: #columnn 1
        return True
    elif strokes[6] == signal and strokes[7] == signal and strokes[8] == signal: #row 3
        return True
    elif strokes[6] == signal and strokes[4] == signal and strokes[2] == signal: # transversal starting from the row3, column 1
        return True 
    elif strokes[1] == signal and strokes[4] == signal and strokes[7] == signal: #column 2
        return True 
    elif strokes[3] == signal and strokes[4] == signal and strokes[5] == signal: #row 2
        return True
    elif strokes[2] == signal and strokes[5] == signal and strokes[8] == signal: #column 3
        return True

    return False


#click event for every button
def click(widget):
    
    #disable clicked button
    widget["state"] = DISABLED
    #put the Label with "0" text into the button that called this event function
    place(widget, "O", "green")

    #record and "O" in the strokes list
    record_position(widget, "O")

    #verify if the player wins
    if (win("O")):
        response = messagebox.askquestion(message="You win!!!!\nDo you want to play again?", title="Finish!!")
        if (response == 'yes'):
            #clear labels in buttons and clear the strokes list
            clear_game()
            return False
        else:
            root.destroy()
        
    #if the player does´t won, the computer will make a stroke
    random_play()

    #verify if the computer wins
    if (win("X")):
        response = messagebox.askquestion(message="I win!!!!!!!\nDo you want to play again?", title="Finish!!")
        if (response == 'yes'):
            #clear labels in buttons and clear strokes list
            clear_game()
            return False
        else:
            root.destroy()
       
    
    #verify if there's no more strokes
    if "" not in strokes:
        response = messagebox.askquestion(message="There is no winner!!\nDo you want to play again?", title="Finish!!")
        if (response == 'yes'):
            #clear labels in buttons and clear strokes list
            clear_game()
            return False
        else:
            root.destroy()


def main():
    global buttons
    global root

    #create root window
    root = Tk()
    root.title("Jogo da Velha")
    root.geometry("445x405")

    #add buttons that will compose the position options
    button1 = Button(root, width=15, height=7, command=lambda: click(button1))
    button1.grid(row=0, column=0)

    button2 = Button(root,width=15, height=7, command=lambda: click(button2))
    button2.grid(row=0, column=1)

    button3 = Button(root,width=15, height=7, command=lambda: click(button3))
    button3.grid(row=0, column=2)

    button4 = Button(root,width=15, height=7, command=lambda: click(button4))
    button4.grid(row=1, column=0)

    button5 = Button(root,width=15, height=7, state=DISABLED)
    button5.grid(row=1, column=1)
    place(button5, "X", "red")
    record_position(button5, "X")

    button6 = Button(root,width=15, height=7, command=lambda: click(button6))
    button6.grid(row=1, column=2)

    button7 = Button(root,width=15, height=7, command=lambda: click(button7))
    button7.grid(row=2, column=0)

    button8 = Button(root,width=15, height=7, command=lambda: click(button8))
    button8.grid(row=2, column=1)

    button9 = Button(root,width=15, height=7, command=lambda: click(button9))
    button9.grid(row=2, column=2)
    
    #create a list of buttons to manipulate after
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

    root.mainloop()


main()