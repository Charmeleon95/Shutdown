import os
import time as tm
import tkinter as tk
from tkinter import Label
import string
import datetime

def checker(time):
    for digit in time:
        if digit not in string.digits:
            var.set('only numbers in input please')

    if int(time)>220:
        var.set('dont think soo its hella long')
    else:
     n_time=int(time)*60 #defult is second converting to minutes
     timer_f(n_time)

def timer_f(time):
    while (time != 0) & (stop == False):
        timer = str(datetime.timedelta(seconds=time))
        timer = "shutdown in:  " + timer
        var.set(timer)
        base.update()
        tm.sleep(1)
        time = time - 1
        stop_countdown()
        #base.after(1000, timer_f(time))
    if time==0 & (stop == False):
        os.system("shutdown /p")




def stop_countdown():
 stop=True
 base.update()



stop=False
base = tk.Tk()
var=tk.StringVar()
var.set('enter time in minutes and press the button')

timeunit='minutes' #time unit def would be minutes

canvas = tk.Canvas(base, height=500, width=900)
canvas.pack()

frame=tk.Frame(base, bg='#424242')
frame.place(relwidth=1, relheight=1)

top_label=tk.Label(frame, text="welcome to the shutdown software (better name incoming some time some day)", bg="yellow")
top_label.place(relx=0.25, rely=0.03, relwidth=0.5, relheight=0.05)

timer_label=tk.Label(frame, textvariable = var, bg="gray", font=("Courier", 10))
timer_label.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.35)

bot_label=tk.Label(frame, text=(f"enter ammount of time in {timeunit} to shut down your pc"), bg="gray")
bot_label.place(relx=0.02, rely=0.6, relwidth=0.36, relheight=0.06)

entery=tk.Entry(frame ,bg="gray")
entery.place(relx=0.4, rely=0.6, relwidth=0.25, relheight=0.06)

button_start=tk.Button(frame, text="shutdown in written time", bg="gray", command=lambda: checker(entery.get()))
button_start.place(relx=0.56, rely=0.8, relwidth=0.25, relheight=0.08)



button_stop=tk.Button(frame, text="stop countdown", bg="gray")
button_stop.place(relx=0.15, rely=0.8, relwidth=0.25, relheight=0.08)


base.mainloop()

""""
os.system("shutdown /p")
"""