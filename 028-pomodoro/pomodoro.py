from tkinter import Tk, Canvas, PhotoImage, Button, NORMAL, DISABLED

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TICK = "✔"
TIMER_START = "00:00"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

current_rep = 0
timer = ""


def reset_timer():
    global current_rep, timer
    win.after_cancel(timer)
    current_rep = 0
    start.config(state=NORMAL)
    canvas.itemconfig(action, text="Timer", fill=GREEN)
    canvas.itemconfig(timer_text, text=TIMER_START)
    canvas.itemconfig(ticks, text="")


def start_timer():
    global current_rep
    start.config(state=DISABLED)
    current_rep += 1
    if current_rep > 8:
        reset_timer()
    elif current_rep == 8:
        canvas.itemconfig(ticks, text=f"{canvas.itemcget(ticks, 'text')}{TICK}")
        canvas.itemconfig(action, text="Break", fill=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif current_rep % 2 == 0:
        canvas.itemconfig(ticks, text=f"{canvas.itemcget(ticks, 'text')}{TICK}")
        canvas.itemconfig(action, text="Break", fill=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        canvas.itemconfig(action, text="Work", fill=GREEN)
        count_down(WORK_MIN * 60)


def count_down(count):
    time_str = f"{int(count / 60)}:{count % 60:02}"
    canvas.itemconfig(timer_text, text=time_str)
    if count > 0:
        global timer
        timer = win.after(1000, count_down, count - 1)
    else:
        start_timer()


win = Tk()
win.title("Pomodoro")
win.config(padx=100, pady=20, background=YELLOW)

win.after(1000, )
canvas = Canvas(width=210, height=340, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
img = canvas.create_image(105, 160, image=tomato_img)
# Note: x & y are positional arguments; *args
action = canvas.create_text(105, 20, text="Timer", fill=GREEN, font=(FONT_NAME, 24, "bold"))
timer_text = canvas.create_text(105, 180, text=TIMER_START, fill="white", font=(FONT_NAME, 28, "bold"))
ticks = canvas.create_text(105, 310, fill=GREEN, font=(FONT_NAME, 24, "bold"))
canvas.grid(row=0, column=1)
start = Button(text="Start", font=(FONT_NAME, 16, "bold"), background="white", state=NORMAL, command=start_timer)
start.grid(row=1, column=0)
reset = Button(text="Reset", font=(FONT_NAME, 16, "bold"), background="white", command=reset_timer)
reset.grid(row=1, column=2)

win.mainloop()
