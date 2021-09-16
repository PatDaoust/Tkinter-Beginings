# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:21:48 2021

@author: catal
"""

import tkinter as tk
from random import randint

# for i in range(20):
#     print(randint(0, 6))

# goal= simulate dice roll
# roll button bount to randint()
# label to display randint() result

window = tk.Tk()
window.title("D6 Dice Roll")


def rollD6():
    """simulates rolling a D6"""
    roll_result = randint(0, 6)
    label["text"] = str(roll_result)


button = tk.Button(text="Roll", width=20, relief=tk.RAISED, borderwidth=4, command=rollD6)
label = tk.Label(text="roll to see your result")  # TODO f string text

button.pack()
label.pack()

window.mainloop()
