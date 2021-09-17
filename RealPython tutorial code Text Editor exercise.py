# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:41:41 2021

@author: catal
"""

# whole window should have a minimum height of 800 pixels

# in frame1, not auto-resizing:
# A Button widget called btn_open for opening a file for editing
# A Button widget called btn_save for saving a file

# in frame2, auto-resizing:
# A TextBox widget called txt_edit for creating and editing the text file
# minimum width of 800 pixels
# .rowconfigure() and .columnconfigure() to 800, weight of 1.

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def saveFile():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_box_text.get("1.0", tk.END)
        output_file.write(text)


def openFile():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_box_text.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        file_text = input_file.read()
        text_box_text.insert("1.0", file_text)


# initialize window
window = tk.Tk()
window.title("Text Editor")
window.rowconfigure(0, weight=1, minsize=100)
window.columnconfigure(0, weight=1, minsize=100)
window.columnconfigure(1, weight=100, minsize=100)

# create frame for buttons and buttons
frame_buttons = tk.Frame(master=window)
button_open = tk.Button(master=frame_buttons,
                        text="Open",
                        relief=tk.RAISED,
                        borderwidth=5,
                        command=openFile)
button_save = tk.Button(master=frame_buttons,
                        text="Save As",
                        relief=tk.RAISED,
                        borderwidth=5,
                        command=saveFile)

# create frame for text box and text box
frame_text = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
text_box_text = tk.Text(master=frame_text, bg="#B00B69")

# grid all the widgets
frame_buttons.grid(row=0, column=0, sticky="N")
button_open.grid(padx=8, pady=8)
button_save.grid(padx=8, pady=8)
frame_text.grid(row=0, column=1, sticky="nsew")
text_box_text.pack(fill=tk.BOTH)

# start main event loop
window.mainloop()
