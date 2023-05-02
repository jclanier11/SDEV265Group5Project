import tkinter as tk
import constellations


def listCurrentConstellations(month):
    """In response to the user submitting parameters (selection() function in parameters.py)
    in the first window, this function compares the month the user chose to the startMonth
    and endMonth attributes in the constellations.Constellation class objects. It then
    generates a window and populates it with a list of the constellations that match the user's 
    month selection."""

    # starting the new popup window
    constList = tk.Toplevel()
    constList.config(width=200, height=200)
    constList.title("Constellation List")

    # creating the header above the buttons
    header = tk.Label(constList,
                      text='Star Chart takes a few seconds to load, please be patient!\n'
                      '\n Here are the constellations that are best viewed' '\n in the month you chose:')
    header.pack()

    # empty list to hold the Constellation objects that match the user's month selection
    inSkyChartConstObjects = []

    # leading_zeroes = ["01", "02", "03", "04", "05", "06", ""]
    # if str(month) ==
    # 'for' loop to iterate the list of Constellation objects in constellation.py and compare to user's month selection
    for const in constellations.constObjList:
        if const.startMonth == month or month == const.endMonth:
            # adding matching months to the list
            inSkyChartConstObjects.append(const)

    # 'for' loop to generate a button for each of the matching constellations. The command for each button will open the
    # information window and pass that constellation as an argument to the generateInfoWindow() function to populate
    # the window with the information for that constellation
    buttonList = []
    for constell in inSkyChartConstObjects:

        button = tk.Button(constList, text=constell.name1,
                           command=lambda arg1=constell: constellations.generateInfoWindow(arg1))
        buttonList.append(button)

    for button in buttonList:
        button.pack()

    constList.mainloop()


if __name__ == "__main__":
    listCurrentConstellations(month)
