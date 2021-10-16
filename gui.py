# Import the required Libraries
from tkinter import *
from tkinter import ttk

# Create an instance of Tkinter frame
win = Tk()
# Set the geometry of the Tkinter frame
win.geometry("1500x750")
background_image = PhotoImage("img/Screenshot (20).png")
label = Label(win, image=background_image)
label.place(x=0, y=0)

# Button
sadface = PhotoImage(file=r"img/sadface.png")
smiley = PhotoImage(file=r"img/smiley.png")
bottle = PhotoImage(file=r"img/bottle.png")
books = PhotoImage(file=r"img/books.png")
sunglasses = PhotoImage(file=r"img/sunglasses.png")

#images on canvas

# Function of Button
def find_and_display():
    print("Jesus Christl")



# Define a function to update the entry widget
def entry_update(text):
    entry.delete(0, END)
    entry.insert(0, text)


# Create an Entry Widget
entry = Entry(win, width=70, bg="lightblue")
entry.pack(pady=60)

# Create Multiple Buttons with different commands
button_dict = {}
option = ["Python", "Java", "Go", "C++"]
Button(win, text='Porsche', image=sadface, height=130, width=130, command=find_and_display).place(x=75,y=150)
Button(win, text='Porsche', image=smiley, height=130, width=130, command=find_and_display).place(x=375,y=150)
Button(win, text='Porsche', image=bottle, height=130, width=130, command=find_and_display).place(x=675,y=150)
Button(win, text='Porsche', image=books, height=130, width=130, command=find_and_display).place(x=975,y=150)
Button(win, text='Porsche', image=sunglasses, height=130, width=130, command=find_and_display).place(x=1275,y=150)


'''for i in option:
    def func(x=i):
        return entry_update(x)


    button_dict[i] = ttk.Button(win, text=i, command=func)
    button_dict[i].pack()'''

win.mainloop()
