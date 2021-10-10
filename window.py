#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Label, Place, messagebox


window = tk.Tk()
window.title('My Window')
window.geometry('500x500')

fetch_type = tk.StringVar()
# l = tk.Label(window, bg='white', width=20, text='empty')
# l.pack()

# def print_selection():
#     l.config(text='you have selected ' + var.get())

def Word_enter_button():
    #messagebox.showinfo("say hello there", "Hello World")
    entered_word = E1.get()
    Label(window, text=entered_word, font = ('Century 12')).pack(side=tk.LEFT, pady=10)

r1 = tk.Radiobutton(window, text='Get Definition and Year', variable=fetch_type, value='single')
r1.pack()
r2 = tk.Radiobutton(window, text='Get all possible words', variable=fetch_type, value='all')
r2.pack()


L1 = tk.Label(window, text="Enter word:")
L1.pack(side=tk.LEFT)
L1.place(x=50, y=150)

E1 = tk.Entry(window, bd=1)
E1.pack(side=tk.LEFT)
E1.place(x=130, y=150)

B1 = tk.Button(window, text="Enter", command= Word_enter_button)
B1.place(x = 300, y=150)







window.mainloop()