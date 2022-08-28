from ctypes.wintypes import RGB
from tkinter import *

def pressButton(num):
    global labelText

    labelText = labelText + str(num)
    textDisplay.set(labelText)

def equals():
    
    global labelText

    try:

        total = str(eval(labelText))

        textDisplay.set(total)

        labelText = total

    except ZeroDivisionError:

        textDisplay.set('Err')

        labelText = ""

    except SyntaxError:

        textDisplay.set("Err")

        labelText = ""

def clear():
    
    global labelText

    textDisplay.set("")

    labelText = ""

window = Tk()
window.title("Row Pieculator")
window.geometry("335x488")

labelText = ""

textDisplay = StringVar()



label = Label(window, textvariable = textDisplay, font = ("consolas", 20), bg = "white", width = 21, height = 2, borderwidth=1, relief="groove")
label.pack(padx=4, pady=4)

frame = Frame(window)
frame.pack()

button1 = Button(frame, text = 1, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(1), relief="flat", bg = "#dbdbdb")
button1.grid(row = 0, column = 0)

button2 = Button(frame, text = 2, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(2), relief="flat", bg = "#dbdbdb")
button2.grid(row = 0, column = 1)

button3 = Button(frame, text = 3, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(3), relief="flat", bg = "#dbdbdb")
button3.grid(row = 0, column = 2)

button4 = Button(frame, text = 4, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(4), relief="flat", bg = "#dbdbdb")
button4.grid(row = 1, column = 0)

button5 = Button(frame, text = 5, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(5), relief="flat", bg = "#dbdbdb")
button5.grid(row = 1, column = 1)

button6 = Button(frame, text = 6, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(6), relief="flat", bg = "#dbdbdb")
button6.grid(row = 1, column = 2)

button7 = Button(frame, text = 7, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(7), relief="flat", bg = "#dbdbdb")
button7.grid(row = 2, column = 0)

button8 = Button(frame, text = 8, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(8), relief="flat", bg = "#dbdbdb")
button8.grid(row = 2, column = 1)

button9 = Button(frame, text = 9, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(9), relief="flat", bg = "#dbdbdb")
button9.grid(row = 2, column = 2)

button0 = Button(frame, text = 0, height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton(0), relief="flat", bg = "#dbdbdb")
button0.grid(row = 3, column = 0)

plus = Button(frame, text = '+', height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton('+'), relief="flat", bg = "#dbdbdb")
plus.grid(row = 0, column = 3)

minus = Button(frame, text = '-', height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton('-'), relief="flat", bg = "#dbdbdb")
minus.grid(row = 1, column = 3)

multiply = Button(frame, text = '*', height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton('*'), relief="flat", bg = "#dbdbdb")
multiply.grid(row = 2, column = 3)

divide = Button(frame, text = '/', height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton('/'), relief="flat", bg = "#dbdbdb")
divide.grid(row = 3, column = 3)

equal = Button(frame, text = '=', height = 2, width = 5, font = ("consolas", 19), command = equals, relief="flat", bg = "#dbdbdb")
equal.grid(row = 3, column = 2)

decimal = Button(frame, text = '.', height = 2, width = 5, font = ("consolas", 19), command = lambda: pressButton('.'), relief="flat", bg = "#dbdbdb")
decimal.grid(row = 3, column = 1)

clear = Button(window, text = "CE", height = 2, width = 22, font = ("consolas", 19), command = clear, relief="flat", bg = "#dbdbdb")
clear.pack(padx=5, pady=5)

window.resizable(0, 0)

window.mainloop()