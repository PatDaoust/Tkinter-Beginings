# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:25:20 2021

@author: catal
"""

import tkinter as tk

# create window
window = tk.Tk()

# create frame widget
frame_a = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
frame_b = tk.Frame(master=window, relief=tk.RAISED, borderwidth=10)

# create label widget
greeting = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
greeting = tk.Label(
    text="Hello, Tkinter",
    fg="gray",  # Set the text color to gray
    bg="aqua",  # Set the background color to turquoise
    width=10,
    height=10,
    master=frame_a
)

# create button widget, can style like a label
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    master=frame_a
)

# use label to tell user what to put in entry widget
label_for_entry = tk.Label(text="Name", master=frame_b)
# create entry widget
entry = tk.Entry(master=frame_b)
# same text entered to entry
entry_name = entry.get()
# delete 1st to 3rd char of entry (built on string slicing)
entry.delete(0, 4)
# to insert string at index
entry.insert(0, "Python")

# create text box widget
text_box = tk.Text()
# get(start_index, end_index), index format "line.char"
text_box.get("1.0", tk.END)
# text_box.delete(start_index, stop_index)
# to insert at given index
text_box.insert("1.0", "Hello")
# to insert into a new line
text_box.insert("2.0", "\nWorld")

# to create label within frame
label = tk.Label(master=frame_a, text="kittens")

# add widgets to window
frame_b.pack()
frame_a.pack()
greeting.pack()
label.pack()
button.pack()
label_for_entry.pack()
entry.pack()
text_box.pack()


frame_b.pack()

# make GIU window open
window.mainloop()

# # close window
# window.destroy()

# test note
print("test note")
