# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:45:03 2021

@author: catal
"""

import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame2 = tk.Frame(master=window)

label_first_name = tk.Label(text="First Name:", master=frame)
entry_first_name = tk.Entry(master=frame, width=60)
label_last_name = tk.Label(text="Last Name:", master=frame)
entry_last_name = tk.Entry(master=frame, width=60)
label_address1 = tk.Label(text="Address Line 1:", master=frame)
entry_address1 = tk.Entry(master=frame, width=60)
label_address2 = tk.Label(text="Address Line 2:", master=frame)
entry_address2 = tk.Entry(master=frame, width=60)
label_city = tk.Label(text="City:", master=frame)
entry_city = tk.Entry(master=frame, width=60)
label_province = tk.Label(text="State/Province:", master=frame)
entry_province = tk.Entry(master=frame, width=60)
label_postal_code = tk.Label(text="Postal Code:", master=frame)
entry_postal_code = tk.Entry(master=frame, width=60)
label_country = tk.Label(text="Country:", master=frame)
entry_country = tk.Entry(master=frame, width=60)

button_clear = tk.Button(text="Clear", master=frame2, width=10, relief=tk.RAISED, borderwidth=4)
button_submit = tk.Button(text="Submit", master=frame2, width=10,relief=tk.RAISED, borderwidth=4)

frame.grid()
# TODO align labels right
label_first_name.grid(row=0, column=0, sticky="e")
entry_first_name.grid(row=0, column=1)
label_last_name.grid(row=1, column=0, sticky="e")
entry_last_name.grid(row=1, column=1)
label_address1.grid(row=2, column=0, sticky="e")
entry_address1.grid(row=2, column=1)
label_address2.grid(row=3, column=0, sticky="e")
entry_address2.grid(row=3, column=1)
label_city.grid(row=4, column=0, sticky="e")
entry_city.grid(row=4, column=1)
label_province.grid(row=5, column=0, sticky="e")
entry_province.grid(row=5, column=1)
label_postal_code.grid(row=6, column=0, sticky="e")
entry_postal_code.grid(row=6, column=1)
label_country.grid(row=7, column=0, sticky="e")
entry_country.grid(row=7, column=1)
frame2.grid(sticky="e")
button_clear.grid(row=8, column=0, padx=10, pady=10)
button_submit.grid(row=8, column=1, padx=10, pady=10)
# TODO align bottons right

window.mainloop()
