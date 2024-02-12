import random
import pyperclip
from tkinter import *
from tkinter import messagebox

FONT = ("Arial", 10, "normal")


def generate_password():
    # Adapted from Day 5 Pwd Generator
    num_letters = random.randint(12, 14)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    letters = [chr(i) for i in range(97, 123)]
    letters.extend([letter.upper() for letter in letters])
    numbers = [chr(i) for i in range(48, 58)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Initialise all pwd characters to know value
    pwd = ['£'] * num_letters

    # Set the numbers and symbols first
    random_ints = random.sample(range(0, len(pwd)), (num_numbers + num_symbols))

    for i in range(0, len(random_ints)):
        if i < num_numbers:
            pwd[random_ints[i]] = numbers[random.randint(0, len(numbers) - 1)]
        else:
            pwd[random_ints[i]] = symbols[random.randint(0, len(symbols) - 1)]

    for i in range(0, len(pwd)):
        if pwd[i] == '£':
            pwd[i] = letters[random.randint(0, len(letters) - 1)]

    pword.delete(0, END)
    pword.insert(0, "".join(pwd))
    pyperclip.copy(pword.get())


def add_data():

    site = website.get()
    nm = name.get()
    password = pword.get()

    if len(site) == 0 or len(nm) == 0 or len(password) == 0:
        messagebox.showerror(title="Invalid Data", message="One or more fields has been left blank")
    else:
        if messagebox.askokcancel(title=site, message=f"Details entered:\nEmail: {nm}\nPassword: {password}\nOk to save ?"):
            with open("./pwd_data.txt", mode="a") as f:
                f.write(f"{site} | {nm} | {password}\n")

            website.delete(0, END)
            name.delete(0, END)
            pword.delete(0, END)
            website.focus()


win = Tk()
win.title("Password Manager")
win.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

lab1 = Label(text="Website:", font=FONT)
lab1.grid(row=1, column=0, sticky=E)
website = Entry(width=38, font=FONT)
website.grid(row=1, column=1, columnspan=2, sticky=W)
website.focus()

lab2 = Label(text="Email/Username:", font=FONT)
lab2.grid(row=2, column=0, sticky=E)
name = Entry(width=38, font=FONT)
name.grid(row=2, column=1, columnspan=2, sticky=W)

lab3 = Label(text="Password:", font=FONT)
lab3.grid(row=3, column=0, sticky=E)
pword = Entry(width=26, font=FONT)
pword.grid(row=3, column=1, sticky=W)
gen_pword = Button(text="Generate Password", font=FONT, command=generate_password)
gen_pword.grid(row=3, column=2)

add = Button(text="Add", width=22, font=FONT, command=add_data)
add.grid(row=4, column=1, sticky=W)

win.mainloop()
