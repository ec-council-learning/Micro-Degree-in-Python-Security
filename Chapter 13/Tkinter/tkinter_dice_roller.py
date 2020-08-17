#!/usr/bin/env python3

from random_dice_roller import multiDie

from tkinter import *
from tkinter import messagebox

window = Tk()

# Initialize
window.title("Dice roller")  # Window title
window.geometry("200x125")  # Windows size


# Actions
def click_d4():
    result = multiDie(1, 4)
    messagebox.showinfo("Dice roll result", result)


def click_d6():
    result = multiDie(1, 1)
    messagebox.showinfo("Dice roll result", result)


def click_d8():
    result = multiDie(1, 5)
    messagebox.showinfo("Dice roll result", result)


def click_d10():
    result = multiDie(1, 2)
    messagebox.showinfo("Dice roll result", result)


def click_d12():
    result = multiDie(1, 6)
    messagebox.showinfo("Dice roll result", result)


def click_d20():
    result = multiDie(1, 7)
    messagebox.showinfo("Dice roll result", result)


def click_d100():
    result = multiDie(1, 3)
    messagebox.showinfo("Dice roll result", result)


# Buttons
d4 = Button(window, text="1d4", command=click_d4)
d4.grid()  # Default position

d6 = Button(window, text="1d6", command=click_d6)
d6.grid()

d8 = Button(window, text="1d8", command=click_d8)
d8.grid()

d10 = Button(window, text="1d10", command=click_d10)
d10.grid(column=3, row=0)  # Force position

d12 = Button(window, text="1d12", command=click_d12)
d12.grid(column=3, row=1)

d20 = Button(window, text="1d20", command=click_d20)
d20.grid(column=3, row=2)

d100 = Button(window, text="1d100", command=click_d100)
d100.grid(column=2, row=3)

# Run program
window.mainloop()
