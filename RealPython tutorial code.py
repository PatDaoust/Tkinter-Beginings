# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:25:20 2021

@author: catal
"""

import tkinter as tk

# create window
window = tk.Tk()

# create widget
greeting = tk.Label(text="Python rocks")

# add widget to window
greeting.pack()

# to make GIU window open
window.mainloop()
