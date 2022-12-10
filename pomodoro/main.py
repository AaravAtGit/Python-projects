from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 60
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    lable.config(text="Timer")
    Tick.config(text="")
    canvas.itemconfig(timer_text, text = "00:00")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_brek_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break_sec)
        lable.config(text="BREAK", fg=RED)
    elif reps % 2 != 0:
        countdown(work_sec)
        lable.config(text="WORK", fg=GREEN)
    elif reps % 2 == 0:
        countdown(short_brek_sec)
        lable.config(text="BREAK", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(reps // 2):
            mark += "✔"
        Tick.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("POMODORO")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)

tomato = PhotoImage(file="tomato.png")

canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(100, 112, fill="white", font=(FONT_NAME,35,"bold"), text="00:00")




lable = Label(text="Timer", fg=GREEN, font=(FONT_NAME,50,"bold"),bg=YELLOW,highlightthickness=0)
lable.grid(row=0,column=1)

Tick = Label(fg=GREEN, font=(FONT_NAME,20,"bold"),bg=YELLOW,highlightthickness=0)
Tick.grid(row=3,column=1)

BTN1 = Button(text="Start", command=start_timer)
BTN1.grid(row=2,column=0)

BTN2 = Button(text="Reset", command=reset_timer)

BTN2.grid(row=2,column=2)
canvas.grid(column=1,row=1)
window.mainloop()