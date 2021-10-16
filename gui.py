# Import the required Libraries
from tkinter import *
from tkinter import ttk
import main

# Create an instance of Tkinter frame
win = Tk()
win.title("tumoji")
# Set the geometry of the Tkinter frame
win.geometry("1500x750")
background_image = PhotoImage("img/Screenshot (20).png")
label = Label(win, image=background_image)
label.place(x=0, y=0)

# Button
sadface = PhotoImage(file=r"../../Desktop/tumoji/img/sadface.png")
smiley = PhotoImage(file=r"../../Desktop/tumoji/img/smiley.png")
bottle = PhotoImage(file=r"../../Desktop/tumoji/img/bottle.png")
books = PhotoImage(file=r"../../Desktop/tumoji/img/books.png")
sunglasses = PhotoImage(file=r"../../Desktop/tumoji/img/sunglasses.png")

# images on canvas
global a


# Function of Button
def find_and_display():
    print("Jesuuuuuuuuuuus")


def run(text_variable):
    study_playlist = "RDCLAK5uy_nZJzoZEBYRptA2XXskbxGTvKkevapT_F4"  # 📕
    party_playlist = "RDCLAK5uy_n4PuqfjXs63tz7E3lEs2av_rSBmuJqf-k"  # 🍾
    relax_playlist = "RDCLAK5uy_mdwsZFtQhJyGQPuQA612VoRPXp-OJfzx8"  # 😎
    romance_playlist = "RDCLAK5uy_l1oO11DBO4FD8U7bOrqUKK5Y_PkISUMQM"  # ❤️
    good_mood_playlist = "RDCLAK5uy_kvmdYWgmu7MBsrWUzv53AyF02ytmE18bo"  # 😂
    sad_mood_playlist = "PLLIVqphyPGcWicpB3eXYDpXFY5KuuQs6_"  # ☹️
    text = text_variable.get()
    firstLetter = text[0:1]
    text_variable.set("AI is looking for songs...")
    out = ""
    if firstLetter == "0":
        out = main.main(sad_mood_playlist)
    elif firstLetter == "1":
        out = main.main(good_mood_playlist)
    elif firstLetter == "2":
        out = main.main(party_playlist)
    elif firstLetter == "3":
        out = main.main(study_playlist)
    elif firstLetter == "4":
        out = main.main(relax_playlist)
    else:
        out =main.main(romance_playlist)

    text_variable.set(out)


# Define a function to update the entry widget
def entry_update(text):
    entry.delete(0, END)
    entry.insert(0, text)


def get_text_input():
    result = entry.get()
    print(result)


bla = StringVar()
# Create an Entry Widget
entry = Entry(win, width=70, bg="lightblue", textvariable=bla)
entry.pack(pady=60)

# Create Multiple Buttons with different commands
button_dict = {}
Button(win, text='Porsche', image=sadface, height=130, width=130, command=find_and_display).place(x=75, y=150)
Button(win, text='Porsche', image=smiley, height=130, width=130, command=find_and_display).place(x=375, y=150)
Button(win, text='Porsche', image=bottle, height=130, width=130, command=find_and_display).place(x=675, y=150)
Button(win, text='Porsche', image=books, height=130, width=130, command=find_and_display).place(x=975, y=150)
Button(win, text='Porsche', image=sunglasses, height=130, width=130, command=find_and_display).place(x=1275, y=150)
Button(win,
       text="Write comma-seperated numbers from 1-5 (that represent the emojis) into the textfield and continue here",
       height=10, width=80, command=lambda: run(bla)).place(x=400, y=400)

'''for i in option:
    def func(x=i):
        return entry_update(x)


    button_dict[i] = ttk.Button(win, text=i, command=func)
    button_dict[i].pack()'''

win.mainloop()
