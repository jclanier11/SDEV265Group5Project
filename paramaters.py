import tkinter as tk
import tkinter.ttk as ttk

from tkinter import messagebox

window = tk.Tk()
window.config(width=300, height=200)
window.title("Paramaters")


def selections():
    location = locale.get()
    time = hour.get()


locale = ttk.Combobox(
    state="readonly",
    values=["Berlin", "Moscow", "New York", "Singapore", "Soeul", "Tokyo", "Washington D.C."])
locale.place(x=50, y=50)

hour = ttk.Combobox(
    state="readonly",
    values=[])

button = ttk.Button(text="Display locale", command=selections)
button.place(x=50, y=100)


window.mainloop()
