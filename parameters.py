import tkinter as tk
import tkinter.ttk as ttk
import starchartlist

window = tk.Tk() # creates the parameters window
window.geometry("400x200")
window.title("Parameters")


def selections():
    """Pulls the values from the user inputs in the parameters window and sends them to the star_chart.py file for the star chart generation
    as well as sending the month the listCurrentConstellations function in the starchartlist.py file to create the constellation list window."""
    loadingLabelText.set("Star chart is loading, this may take a moment...") # displays a loading status at the bottom of the parameters window
    window.update()
    location = locale.get() # get methods to pull the dropdown menu values to the sky_chart.py file
    year = t_year.get()
    month = t_month.get()
    day = t_day.get()
    hour = t_hour.get()
    with open("star_chart.py") as f: # runs the code in the star_chart.py file to generate the sky chart window
        exec(f.read())
    loadingLabelText.set("") # once the results window and star chart appear nearly together, the loading status is reset to display nothing
    starchartlist.listCurrentConstellations(month) # creates constellation list window

    

# contents of the parameters window
label = ttk.Label(text="City:", )
label.place(x=50, y=5)
locale = ttk.Combobox(
    state="readonly",
    values=["Beijing", "Berlin", "Hong Kong", "London", "Moscow", "Paris",
            "New York", "Seattle", "Singapore", "Seoul", "Tokyo"])
locale.current(newindex=0)
locale.place(x=50, y=25)

label = ttk.Label(text="Year:")
label.place(x=50, y=50)
t_year = ttk.Combobox(
    state="readonly",
    values=["2023", "2024"])
t_year.current(newindex=0)
t_year.place(x=50, y=70, width=60)

label = ttk.Label(text="Month:")
label.place(x=115, y=50)
t_month = ttk.Combobox(
    state="readonly",
    values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
t_month.current(newindex=0)
t_month.place(x=115, y=70, width=50)

label = ttk.Label(text="Day:")
label.place(x=170, y=50)
t_day = ttk.Combobox(
    state="readonly",
    values=["1", "10", "15", "20", "21", "25"])
t_day.current(newindex=0)
t_day.place(x=170, y=70, width=50)

label = ttk.Label(text="Hour:")
label.place(x=225, y=50)
t_hour = ttk.Combobox(
    state="readonly",
    values=["20:00", "21:00", "22:00", "23:00"])
t_hour.current(newindex=0)
t_hour.place(x=225, y=70, width=75)

button = ttk.Button(text="Create Star Chart", command=selections)
button.place(x=50, y=110)

loadingLabelText = tk.StringVar() # holds the value for the loading status message space at the bottom of the parameters window
loadingLabelText.set("")
loadingStatus = ttk.Label(textvariable=loadingLabelText)
loadingStatus.place(y=150, x=50)


window.mainloop()
