from tkinter import *
from enhanced_pomodoro_timer import continuous_timer

# initialising the main widget, or the gui window
window = Tk()
Input_box = Entry(window)
window.title("Enhanced Pomodoro Timer")
window.geometry("400x400")

## to create anything on tkinter you need to 1. define it 2. call it

display_time = Label(text="hi")







display_time.pack()






















'''
def show():
    Label = Label(window, text = work_time.get()).pack()



work_time = IntVar()
work_time.set(25)

options = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
work_time_selection = OptionMenu(window, work_time, *options)
work_time_selection.pack()
start_timer_button = Button(window, text="Start timer", command=show).pack()
'''


window.mainloop()