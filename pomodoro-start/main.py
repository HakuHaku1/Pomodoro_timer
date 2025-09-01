from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
global timer
rep = 0

def reset_timer():

    window.after_cancel(timer)
    canva.itemconfig(minutes_count, text = "00:00")
    Label.config(timer_label, text= "START", fg= "white")
    indication.config(text= "")
    global rep
    rep = 0

def count_timer():
    global rep
    rep += 1

    if rep % 8 == 0:
        timer_label.config(text= "LONG BREAK", fg = YELLOW)
        countdown(LONG_BREAK_MIN * 60)
    elif rep % 2 == 0:
        timer_label.config(text= "SHORT BREAK", fg= GREEN)
        countdown(SHORT_BREAK_MIN * 60)

    else:
        timer_label.config(text = "WORKING MINUTES", fg= RED)

        countdown(WORK_MIN * 60)
    
def countdown(counts):
    mins = math.floor(counts / 60)
    secs = counts % 60
    if secs < 10:
        secs = f"0{secs}"
    
    if mins < 10:
        mins = f"0{mins}"

    canva.itemconfigure(minutes_count, text=f"{mins}:{secs}")

    if counts > 0:
        global timer
        timer = window.after(1000, countdown, counts -1)
    else:
        count_timer()
        mark = ""
        format = math.floor(rep/2)

        for _ in range(format):
            mark += "✔"
        indication.config(text= mark)
        
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=200, height=300)
window.config(padx=50, pady=50, bg=PINK)

timer_label = Label(window, text="TIMER", bg=PINK, fg="white", font=(FONT_NAME, 16, "bold"))
timer_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))  

canva = Canvas(window, width=200, height=250, highlightthickness=0, bg=PINK)
image = PhotoImage(file="tomato.png")
canva.create_image(100, 90, image=image)
minutes_count = canva.create_text(100, 150, text= "00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canva.grid(row=1, column=0, columnspan=2, pady=(0, 20))


indication = Label(window, bg=PINK, fg="green", font=(FONT_NAME, 14, "bold"))
indication.grid(row=1, column=0, columnspan=2, pady=(200, 0))  


start = Button(window, text="Start", highlightthickness= 0, command= count_timer )
start.grid(row=2, column=0, padx=10)
reset = Button(window, text="Reset", highlightthickness= 0, command= reset_timer)
reset.grid(row=2, column=1, padx=10)

window.mainloop()