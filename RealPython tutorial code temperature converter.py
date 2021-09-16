# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:13:32 2021

@author: catal
"""

import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")


def convertFtoC():
    temperature_F = int(entry_temperature_F.get())
    temperature_C = (temperature_F - 32) * 5 / 9
    label_result["text"] = str(temperature_C) + "°C"


frame = tk.Frame(master=window, padx=10, pady=10)
entry_temperature_F = tk.Entry(width=10, master=frame)
label_F = tk.Label(text="°F", master=frame)
label_result = tk.Label(text="temperature in °C", master=frame)
button_convert = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}", command=convertFtoC, relief=tk.RAISED, borderwidth=5, master=frame)

frame.grid()
entry_temperature_F.grid(row=0, column=0)
label_F.grid(row=0, column=1)
button_convert.grid(row=0, column=2, padx=10)
label_result.grid(row=0, column=3)

window.mainloop()
