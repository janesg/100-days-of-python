from tkinter import *

FONT = ("Arial", 14, "bold")
BG_COLOUR = "cyan"


def butt_clicked():
    lab3.config(text=f"{round(float(user_input.get()) * 1.609344, 2)}")


win = Tk()
win.title("Mile to Km Converter")
win.minsize(width=300, height=130)
win.config(padx=20, pady=20, background=BG_COLOUR)

user_input = Entry(width=10, font=FONT, background="white")
user_input.grid(row=0, column=1)
lab1 = Label(text="Miles", font=FONT, padx=20, background=BG_COLOUR)
lab1.grid(row=0, column=2)
lab2 = Label(text="is equal to", font=FONT, background=BG_COLOUR)
lab2.grid(row=1, column=0)
lab3 = Label(text="0", font=FONT, background=BG_COLOUR)
lab3.grid(row=1, column=1)
lab4 = Label(text="Km", font=FONT, padx=20, background=BG_COLOUR)
lab4.grid(row=1, column=2)
butt1 = Button(text="Calculate", font=FONT, background="white", command=butt_clicked)
butt1.grid(row=2, column=1)

win.mainloop()
