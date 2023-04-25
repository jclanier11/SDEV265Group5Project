import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk  # Getting Image and Image TK from PIL

import parameters
import starchartlist


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
                    "Aqr", "Oct. 10, 9 pm", True, 9, 10)
Ari = Constellation("Aries", "The Ram", "Ari", "Dec. 10, 9 pm", True, 11, 12)
Cnc = Constellation("Cancer", "The Crab", "Cnc", "Mar. 15, 9 pm", True, 3, 4)
Cap = Constellation(
    "Capricornus", "The Sea Goat, the Goat, Capricorn", "Cap", "Sept. 20, 9 pm", True, 8, 9)
Gem = Constellation("Gemini", "The Twins", "Gem", "Feb. 20, 9 pm", True, 2, 3)
Leo = Constellation("Leo", "The Lion", "Leo", "Apr. 10, 9 pm", True, 3, 4)
Lib = Constellation("Libra", "The Scales, the Balance",
                    "Lib", "Jun. 20, 9 pm", True, 6, 7)
Psc = Constellation("Pisces", "The Fish", "Psc", "Nov. 10, 9 pm", True, 10, 11)
Sgr = Constellation("Sagittarius", "The Archer",
                    "Sgr", "Aug. 20, 9 pm", True, 7, 8)
Sco = Constellation("Scorpius", "The Scorpion", "Sco",
                    "Jul. 20, 9 pm", True, 7, 8)
Tau = Constellation("Taurus", "The Bull", "Tau", "Jan. 15, 9 pm", True, 1, 2)
Vir = Constellation("Virgo", "The Maiden", "Vir", "May 25, 9 pm", True, 5, 6)

constObjList = [Aqr, Ari, Cnc, Cap, Gem, Leo, Lib, Psc, Sgr,
                Sco, Tau, Vir]  # List of constellation objects available

results = tk.Toplevel(bg='#000028')  # Sets new window and adds color
results.geometry("500x600")  # Sets window size
results.title("Results")  # Sets window title

# Photo above text
# Sets photo to be used

# ------vvvvvvvv------ Constellation Image goes below ------vvvvvvvv------
image1 = Image.open("assets/aquarius-cons-m.jpg")
resized_image = image1.resize((125, 175), Image.ANTIALIAS)  # Resizing photo
test = ImageTk.PhotoImage(resized_image)  # Defines photo for use in label
label1 = tk.Label(results, image=test, bg="#000028")  # Label for photo
label1.image = test  # placing photo in label
label1.place(relx=0.33, rely=0.05, relwidth=0.33,
             relheight=0.33)  # Label location placement


# Frame for text and button
lower_frame = tk.Frame(results, bd=5, bg="#000028")
lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75,
                  relheight=0.5, anchor='n')  # Frame location placement


# ------------------ Aqr info populates, working to get the information to populate based on selection ------------------------
# Page text

# maybe have the label creations outside of the function, and then have the function just
def generateInfoWindow(constellation):
    # assign the text attribute values to the constellation object attributes that were passed
    # We'll also have to put in this function the loops that will pull the extra data
    # out of the constellations.txt file based on the constellation object's acronym
    # for the extra info

    text1 = tk.Label(lower_frame,
                     bg="#000028", fg='white')  # Placing name1
    text2 = tk.Label(lower_frame, text="Alternatively known as: " +
                     Constellation.name2, bg="#000028", fg='white')  # Placing name2
    text3 = tk.Label(lower_frame, text="Constellation Abbreviation: " +
                     Constellation.abbr, bg="#000028", fg='white')  # Placing abbr
    text4 = tk.Label(lower_frame, text="Date Constellation is on the Meridian: " +
                     Constellation.on_meridian, bg="#000028", fg='white')  # Placing on_meridian

    text1[text] = "Name:" + constellation.name1


# statement to change text5 label text based on if constellation is included in zodiac
if Aqr.zodiac == True:
    text5 = tk.Label(
        lower_frame, text="Constellation is a Zodiac Constellation", bg="#000028", fg='white')
else:
    text5 = tk.Label(
        lower_frame, text="Constellation is not a Zodiac Constellation", bg="#000028", fg='white')

text6 = tk.Label(lower_frame, text="Best Months to View: "+str(Aqr.startMonth) +
                 " - "+str(Aqr.endMonth), bg="#000028", fg='white')  # Placing viewing months


# Formatting space for text placement
text1.pack(padx=(20, 5))
text2.pack(padx=5)
text3.pack(padx=5)
text4.pack(padx=5)
text5.pack(padx=5)
text6.pack(padx=5)

results.mainloop()
