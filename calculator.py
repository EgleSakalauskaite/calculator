from tkinter import *
import tkinter as tk
import tkinter.font as font
import parser
root = Tk()

i = 0
def get_variables(n):
    global i
    display.insert(i, n)
    i+=1
def get_operators(operator):
    global i
    display.insert(i, operator)
    i+=len(operator)
def all_clear():
    display.delete(0, END)
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        all_clear()
        display.insert(0, result)
    except Exception:
        all_clear()
        display.insert(0, 'Error')
def undo():
    entire_string = display.get()
    if len(entire_string)>0:
        new_string = entire_string[:-1]
        all_clear()
        display.insert(0, new_string)
    else:
        all_clear()

def factorial():
    whole_string = display.get()
    counter = int(whole_string)
    fact = 1
    try:
        while counter > 0:
            fact *= counter
            counter -= 1
            all_clear()
            display.insert(0, fact)
    except Exception:
        all_clear()
        display.insert(0, "Error")

root.title('Swag calculator')
display = Entry(root, font=('Calibri', 16))
display.grid(row=0, columnspan=6, ipady=10, sticky = W+E)
pixelVirtual = tk.PhotoImage(width=1, height=1)
myfont = font.Font(size=12)

Button(root, text='1', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(1)).grid(row=1, column=0)
Button(root, text='2', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(2)).grid(row=1, column=1)
Button(root, text='3', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(3)).grid(row=1, column=2)
Button(root, text='4', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(4)).grid(row=2, column=0)
Button(root, text='5', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(5)).grid(row=2, column=1)
Button(root, text='6', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(6)).grid(row=2, column=2)
Button(root, text='7', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(7)).grid(row=3, column=0)
Button(root, text='8', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(8)).grid(row=3, column=1)
Button(root, text='9', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(9)).grid(row=3, column=2)

Button(root, text='AC',  bg="DarkOrange1", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: all_clear()).grid(row=4, column=0)
Button(root, text='0', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_variables(0)).grid(row=4, column=1)
Button(root, text='=', image=pixelVirtual, width=30, height=30, compound="c", command=lambda: calculate()).grid(row=4, column=2)

Button(root, text='+', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('+')).grid(row=1, column=3)
Button(root, text='-', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('-')).grid(row=2, column=3)
Button(root, text='*', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('*')).grid(row=3, column=3)
Button(root, text='/', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('/')).grid(row=4, column=3)

Button(root, text='pi', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('*3.1416')).grid(row=1, column=4)
Button(root, text='%', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('%')).grid(row=2, column=4)
Button(root, text='(', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('(')).grid(row=3, column=4)
Button(root, text='^2', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('**2')).grid(row=4, column=4)

Button(root, text='<-', bg="DarkOrange1", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: undo()).grid(row=1, column=5)
Button(root, text='x!', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: factorial()).grid(row=2, column=5)
Button(root, text=')', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators(')')).grid(row=3, column=5)
Button(root, text='sr', bg="slate gray", image=pixelVirtual, width=30, height=30, compound="c", command=lambda: get_operators('**(1/2)')).grid(row=4, column=5)

root.mainloop()