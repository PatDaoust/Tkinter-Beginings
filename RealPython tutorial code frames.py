# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:30:49 2021

@author: catal
"""

import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_b.pack()
frame_a.pack()

window.mainloop()


# to get name from user
window = tk.Tk()
entry = tk.Entry()
label = tk.Label(text="What is your name?")
name = entry.set()

entry.pack()
label.pack()
window.mainloop()