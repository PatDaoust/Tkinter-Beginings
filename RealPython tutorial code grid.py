# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:19:16 2021

@author: catal
"""

import tkinter as tk

window = tk.Tk()

for i in range(3):

    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()
