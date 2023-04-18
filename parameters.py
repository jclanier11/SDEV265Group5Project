import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.config(width=400, height=200)
window.title("Paramaters")


def selections():
    location = locale.get()
    year = t_year.get()
    month = t_month.get()
    day = t_day.get()
    hour = t_hour.get()
    with open("star_chart.py") as f:
        exec(f.read())


locale = ttk.Combobox(
    state="readonly",
    values=["Beijing", "Berlin", "Hong Kong", "London", "Moscow", "Paris",
            "New York", "Seattle", "Singapore", "Seoul", "Tokyo"])
locale.place(x=50, y=25)

t_year = ttk.Combobox(
    state="readonly",
    values=["2023", "2024"])
t_year.place(x=50, y=60, width=60)

t_month = ttk.Combobox(
    state="readonly",
    values=["01", "02", "03", "04", "05", "06", "07", "09", "10", "11", "12"])
t_month.place(x=115, y=60, width=50)

t_day = ttk.Combobox(
    state="readonly",
    values=["1", "21"])
t_day.place(x=170, y=60, width=50)

t_hour = ttk.Combobox(
    state="readonly",
    values=["20:00", "21:00", "22:00", "23:00"])
t_hour.place(x=225, y=60, width=75)

button = ttk.Button(text="Display Selections", command=selections)
button.place(x=50, y=100)


window.mainloop()
