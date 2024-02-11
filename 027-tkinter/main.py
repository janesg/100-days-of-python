from tkinter import *


def butt_clicked():
    lab1.config(text=f"{user_input.get()}")


win = Tk()
win.title("Fabulosa App")
win.minsize(width=500, height=300)
win.config(padx=20, pady=20)

# Label
lab1 = Label(text="Some text", font=("Arial", 14, "italic"))
lab1.grid(row=0, column=0)
lab1.config(padx=20)
# Button
butt1 = Button(text="Click Me 1", command=butt_clicked)
butt1.grid(row=0, column=2)
butt2 = Button(text="Click Me 2", command=butt_clicked)
butt2.grid(row=1, column=1)
# Entry
user_input = Entry(width=20)
user_input.grid(row=2, column=3)

win.mainloop()
