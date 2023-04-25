import tkinter as tk
import tkinter.ttk as ttk
import parameters as param
import constellations as const


def listCurrentConstellations(month):

    window = tk.Tk()
    window.config(width=100, height=200)
    window.title("Constellation List")

    header = tk.Label(
        text='More information for the current \nZodiac constellations in the Sky Chart:')
    header.pack(padx=5, pady=5)

    inSkyChartConstObjects = []
    for constellation in const.constObjList:
        if constellation.startMonth >= month:
            if month <= constellation.endMonth:
                inSkyChartConstObjects.append(constellation)

    for constellation in inSkyChartConstObjects:
        tk.Button(text=constellation.name1,
                  command=const.generateInfoWindow(constellation))

    window.mainloop()
