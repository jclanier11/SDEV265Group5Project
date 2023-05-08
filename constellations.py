import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk  # Getting Image and Image TK from PIL


class Constellation:
    def __init__(self, name1, name2, abbr, on_meridian, zodiac, startMonth, endMonth):
        self.name1 = name1
        self.name2 = name2
        self.abbr = abbr
        self.on_meridian = on_meridian
        self.zodiac = zodiac
        self.startMonth = startMonth  # first best viewing month
        self.endMonth = endMonth  # last best viewing month


Aqr = Constellation("Aquarius", "The Water Bearer",
                    "Aqr", "Oct. 10, 9 pm", True, "09", "10")
Ari = Constellation("Aries", "The Ram", "Ari",
                    "Dec. 10, 9 pm", True, '11', '12')
Cnc = Constellation("Cancer", "The Crab", "Cnc",
                    "Mar. 15, 9 pm", True, '03', '04')
Cap = Constellation(
    "Capricornus", "The Sea Goat, the Goat, Capricorn", "Cap", "Sept. 20, 9 pm", True, '08', '09')
Gem = Constellation("Gemini", "The Twins", "Gem",
                    "Feb. 20, 9 pm", True, '02', '03')
Leo = Constellation("Leo", "The Lion", "Leo",
                    "Apr. 10, 9 pm", True, '03', '04')
Lib = Constellation("Libra", "The Scales, the Balance",
                    "Lib", "Jun. 20, 9 pm", True, '06', '07')
Psc = Constellation("Pisces", "The Fish", "Psc",
                    "Nov. 10, 9 pm", True, '10', '11')
Sgr = Constellation("Sagittarius", "The Archer",
                    "Sgr", "Aug. 20, 9 pm", True, '07', '08')
Sco = Constellation("Scorpius", "The Scorpion", "Sco",
                    "Jul. 20, 9 pm", True, '07', '08')
Tau = Constellation("Taurus", "The Bull", "Tau",
                    "Jan. 15, 9 pm", True, '01', '02')
Vir = Constellation("Virgo", "The Maiden", "Vir",
                    "May 25, 9 pm", True, '05', '06')

constObjList = [Aqr, Ari, Cnc, Cap, Gem, Leo, Lib, Psc, Sgr,
                Sco, Tau, Vir]  # List of constellation objects available


def generateInfoWindow(constellation):
    """Takes the 'constellation' object parameter from the 'command' parameter of the button in the constellation list window and
    generates a window with the information for that constellation object."""
    information = tk.Toplevel()  # Sets new window
    information.geometry("600x750")  # Sets window size
    information.title("Information")  # Sets window title

    # frame = tk.Frame(information, width=600, height=400)
    # frame.pack()
    # frame.place(anchor='center', relx=0.5, rely=0.5)
    # img = ImageTk.PhotoImage(Image.open("images/Aquarius_IAU-596px.png"))
    # label = tk.Label(frame, image=img)
    # label.pack()

    # maybe have the label creations outside of the function, and then have the function just

    imageFrame = tk.Frame(information, width=500, height=500)
    imageFrame.pack()

    # opening constellation image
    img = Image.open('images/'+constellation.name1+'.png')

    # resizing and placing image into frame
    constellImg = ImageTk.PhotoImage(img.resize((500, 555), Image.ANTIALIAS))
    imgLabel = tk.Label(imageFrame, image=constellImg)
    imgLabel.pack()

    name1Label = tk.Label(information)
    name1Label.pack()

    name2Label = tk.Label(information)
    name2Label.pack()

    abbrLabel = tk.Label(information)
    abbrLabel.pack()

    meridianLabel = tk.Label(information)
    meridianLabel.pack()

    zodiacLabel = tk.Label(information)
    zodiacLabel.pack()

    monthsLabel = tk.Label(information)
    monthsLabel.pack()

    # populating labels with text
    name1Label['text'] = "Name: " + constellation.name1
    name2Label['text'] = "Alternatively known as: " + constellation.name2
    abbrLabel['text'] = "Constellation Abbreviation: " + constellation.abbr
    meridianLabel['text'] = "Date Constellation is on the Meridian: " + \
        constellation.on_meridian

    # statement to change text5 label text based on if constellation is included in zodiac
    if constellation.zodiac == True:
        zodiacLabel['text'] = "Constellation is a Zodiac Constellation"
    else:
        zodiacLabel['text'] = "Constellation is not a Zodiac Constellation"

    monthsLabel['text'] = "Best Months to View: " + \
        str(constellation.startMonth) + " - "+str(constellation.endMonth)

    information.mainloop()
